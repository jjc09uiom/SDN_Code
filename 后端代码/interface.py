from flowControl import flowControl
import json

#控制器地址
ip='127.0.0.1'
#wsgi固定端口不用改
port='8080'
dpid='1'
fc=flowControl(ip=ip,port=port)
#打开流表json文件
with open("./flow.json") as file:
	str = file.read()
#转为json
data=json.loads(str)

choose = input('1:get_flow,2:add_flow,3:clear_flow')
while True:
    if choose == '1':
        fc.get_flow(dpid=dpid)
        exit()
    elif choose == '2':
        fc.post_add_flow(flow_data_json=data)       
        exit()
    elif choose == '3':
        fc.post_clear_flow(dpid=dpid)
        exit()
#fc.get_flow(dpid=dpid)

#fc.post_add_flow(flow_data_json=data)

#fc.post_clear_flow(dpid=dpid)
