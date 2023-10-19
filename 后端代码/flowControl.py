import requests

class flowControl:
    def __init__(self, ip, port):
        self.ip=ip
        self.port=port

    #查看指定dpid交换机流表
    def get_flow(self, dpid):
        url = 'http://' + self.ip + ':' + self.port + '/stats/flow/'+dpid
        re_switch_flow = requests.get(url=url).json()
        
        #print(re_switch_flow)
        return re_switch_flow
        []
    # 向控制器发送添加流表项的请求
    def post_add_flow(self, flow_data_json):
        url = 'http://localhost:8080/stats/flowentry/add'

        # 如果正确添加，则返回200OK
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, json=flow_data_json, headers=headers)
        if response.status_code == 200:
            return 1
        else:
            return 0

    # 清除指定dpid控制器的流表
    def post_clear_flow(self, dpid):
        url = 'http://' + self.ip + ':' + self.port + '/stats/flowentry/clear/' + dpid
        response = requests.delete(url=url)
        if response.status_code == 200:
            # print('Successfully Delete!')
            return 1
        else:
            # print('Fail!')
            return 0

    # 查看交换机id
    def get_switch(self):
        url = 'http://' + self.ip + ':' + self.port + '/stats/switches'
        re_switch = requests.get(url=url).json()
        return re_switch                          # 返回列表
