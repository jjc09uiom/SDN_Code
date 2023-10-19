import json
import os
from default import myNetwork
from flowControl import *
from flask import Flask, request, jsonify, render_template
from mininet.node import OVSKernelSwitch, RemoteController, Host
from mininet.net import Mininet
from flask_cors import CORS

# cmd:ryu-manager simple_switch.py ./gui_topology/gui_topology.py --observe-links ryu-manager
# ~/032002401/ryu/ryu/app/simple_switch.py ~/032002401/ryu/ryu/app/gui_topology/gui_topology.py --observe-links
app = Flask(__name__, template_folder='templates')
CORS(app, supports_credentials=True)
net = Mininet(
    topo=None,
    build=False,
    ipBase='10.0.0.0/8'
)
# 控制器地址
ip = '127.0.0.1'
# wsgi固定端口不用改
port = '8080'
flowCon = flowControl(ip=ip, port=port)


def return_img_stream(img_local_path):
    import base64
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream


@app.route('/default', methods=['POST', 'GET'])  # √
def default():
    os.system('sudo mn -c')
    global net
    net = myNetwork()
    os.system("gnome-terminal -e 'bash -c \"sudo ryu-manager ~/032002401/ryu/ryu/app/simple_switch.py  "
              "~/032002401/ryu/ryu/app/gui_topology/gui_topology.py --observe-links; exec bash\"'")
    return render_template('index.html')


@app.route('/seepicture', methods=['POST', 'GET'])  # √
def ping():
    global net
    if request.method == 'POST':
        raw_data = request.data
        json_data = json.loads(raw_data.decode())
        ping = json_data["pingall"]
        if ping:
            net.pingAll(0.05)
        return jsonify(json_data)


@app.route('/addhost', methods=['POST', 'GET'])  # √
def add_host():
    global net
    if request.method == 'POST':
        # bytes 类型
        data = request.get_json(silent=True)
        resp = jsonify(data)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        host = data["host"]
        switch = data["switch"]
        hip = data["ip"]
        h = net.addHost(host, cls=Host, ip=hip)
        h.cmd("ifconfig %s-eth0 %s" % (host, hip))
        s = net.get(switch)
        net.addLink(s, h)
        h1 = net.get('h1')
        hosts = [h1, h]
        net.ping(hosts, '5')
        return resp


@app.route("/delhost", methods=['GET', 'POST'])  # √
def delete_host():
    global net
    if request.method == 'POST':
        data = request.get_json(silent=True)
        host = data["host"]
        h = net.get(host)
        net.delHost(h)
        return data


@app.route("/addswitch", methods=['GET', 'POST'])  # √
def add_switch():
    global net
    if request.method == 'POST':
        data = request.get_json(silent=True)
        resp = jsonify(data)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        switch = data["switch"]
        net.addSwitch(name=switch, cls=OVSKernelSwitch)
        c0 = net.addController(name='c0',
                               controller=RemoteController,
                               protocol='tcp',
                               port=6633)
        net.get(switch).start([c0])
        return resp


@app.route("/delswitch", methods=['GET', 'POST'])  # √
def delete_switch():
    global net
    if request.method == 'POST':
        data = request.get_json(silent=True)
        switch = data['switch']
        s = net.get(switch)
        net.delSwitch(s)
        return data


@app.route("/addlink", methods=['GET', 'POST'])  # √  s1-s2
def add_link():
    global net
    if request.method == 'POST':
        data = request.get_json(silent=True)
        resp = jsonify(data)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        host1 = data["host1"]
        host2 = data['host2']
        hs1 = net.get(host1)
        hs2 = net.get(host2)
        net.addLink(hs1, hs2)
        return data


@app.route("/dellink", methods=['GET', 'POST'])  # √
def delete_link():
    global net
    if request.method == 'POST':
        data = request.get_json(silent=True)
        resp = jsonify(data)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        host1 = data["host1"]
        host2 = data['host2']
        hs1 = net.get(host1)
        hs2 = net.get(host2)
        net.delLinkBetween(hs1, hs2)
        return data


@app.route('/seeswitch', methods=['GET', 'POST'])  # √
def see_switch():
    switches = flowCon.get_switch()
    flows = []
    for switch in switches:
        text_dict = {}
        dpid_str = str(switch)
        id = switches.index(switch)
        flow_dict = flowCon.get_flow(dpid_str)
        kv = {"dpid": switch}
        id = {"id": id}
        flow_dict.update(kv)
        flow_dict.update(id)
        adict = flow_dict.pop(dpid_str)
        for fw in adict:
            num = adict.index(fw)
            text_dict["text_" + str(num)] = fw
        flow_dict["flow"] = text_dict
        flows.append(flow_dict)
    flows = json.dumps(flows)
    return flows


@app.route('/checkflow', methods=['GET', 'POST'])  # √
def check():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        resp = jsonify(data)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        dpid = data["dpid"]
        jsona = flowCon.get_flow(dpid)
        return jsona


@app.route('/addflow', methods=['GET', 'POST'])  # √
def add_flows():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        resp = jsonify(data)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        # text
        flow = data["text"]
        flow = json.loads(flow)
        flowCon.post_add_flow(flow)
        return flow


@app.route('/delflow', methods=['GET', 'POST'])  # √
def delete_flows():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        resp = jsonify(data)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        dpid = data["dpid"]
        flowCon.post_clear_flow(dpid)
        return data


if __name__ == '__main__':
    app.run(host='0.0.0.0')
