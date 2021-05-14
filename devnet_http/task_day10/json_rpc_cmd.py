from flask import Flask, request, Response
import json

node = Flask(__name__)
# 打开Debug
node.debug = True


# POST实现JSON RPC
@node.route('/eem', methods=['POST'])
def rpc_cmd():
    # 提取POST请求数据中的JSON数据
    client_post_data = request.json
    # 如果存在JSON数据,进行后续的操作
    if client_post_data:
        client_event = client_post_data.get('event')
        # 如果能够获取‘event’的值为ospf，进行下一部操作
        if client_event == 'ospf':
            client_status = client_post_data.get('event_detail')
            # 获取接口信息
            client_interface = client_post_data.get('interface')
            if client_status == 'DOWN' and client_interface == 'GigabitEthernet1':
                return Response(response=json.dumps({'cmd': 'interface gig2 \n shutdown '}),
                                status=200,
                                mimetype='application/json')
            elif client_status == 'FULL' and client_interface == 'GigabitEthernet1':
                return Response(response=json.dumps({'cmd': 'interface gig2 \n no shutdown '}),
                                status=200,
                                mimetype='application/json')
            else:
                return json.dumps({'result': {'error': 'no correct status in json!'}})
        else:
            return json.dumps({'result': {'error': 'no ospf status in json!'}})

    # 如果没有JSON数据, 就报错('error'), 'no json data'
    else:
        return json.dumps({'result': {'error': 'no json data'}})


if __name__ == "__main__":
    # 运行Flask在host='192.168.0.104', port=8080
    # 在linux上可以使用'0.0.0.0'
    node.run(host='0.0.0.0', port=8080)