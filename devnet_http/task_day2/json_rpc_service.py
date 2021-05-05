from flask import Flask, request, Response
import base64
import json
import os

node = Flask(__name__)
# 打开Debug
node.debug = True


# POST实现JSON RPC
@node.route('/cmd', methods=['POST'])
def rpc_cmd():
    # 提取POST请求数据中的JSON数据
    client_post_data = request.json
    # 如果存在JSON数据,进行后续的操作
    if client_post_data:
        # 如果有cmd、upload、download值
        client_cmd = client_post_data.get('cmd')
        if client_cmd:
            return Response(response=json.dumps({'result': os.popen(client_cmd).read()}),
                            status=200,
                            mimetype='application/json')
        else:
            return json.dumps({'result': {'error': 'no cmd in json!'}})

    # 如果没有JSON数据, 就报错('error'), 'no json data'
    else:
        return json.dumps({'result': {'error': 'no json data'}})


# POST实现JSON RPC
@node.route('/upload', methods=['POST'])
def rpc_upload():
    # 提取POST请求数据中的JSON数据
    client_post_data = request.json
    print(client_post_data)
    if client_post_data:
        # 如果存在JSON数据,进行后续的操作
        client_upload_name = client_post_data.get('upload')
        if client_upload_name:
            image_b64 = client_post_data.get('file')
            print(image_b64)
            with open(client_upload_name, 'w+') as f:
                image_decode = base64.b64decode(image_b64)
                print(image_decode)
                print(str(image_decode))
                # f.write(image_decode.decode(encoding='utf-8'))
            print('上传文件{0}保存成功！'.format(client_upload_name))
            return_data = {'message': 'Upload Success', 'upload_file': client_upload_name}
            return Response(response=json.dumps(return_data),
                            status=200,
                            mimetype='application/json')
        else:
            return {'error': 'upload key not found!'}
    else:
        return {'error': 'no json data'}


# POST实现JSON RPC
@node.route('/download', methods=['POST'])
def rpc_download():
    # 提取POST请求数据中的JSON数据
    client_post_data = request.json
    if client_post_data:
        # 如果存在JSON数据,进行后续的操作
        client_download_name = client_post_data.get('download')
        if client_download_name:
            try:
                with open(client_download_name, 'rb') as f:
                    read_data = f.read()
                    print(read_data)
                    bytes_b64code = base64.b64encode(read_data)
                return_data = {'download_file': client_download_name, 'file': bytes_b64code.decode()}

                return Response(response=json.dumps(return_data),
                                status=200,
                                mimetype='application/json')
            except Exception:
                return {'error': 'download file not exist'}
        else:
            return {'error': 'download key not found!'}
    else:
        return {'error': 'no json data'}


# 如果三个命令都没有
if __name__ == "__main__":
    # 运行Flask在host='192.168.1.200', port=8080
    # 在linux上可以使用'0.0.0.0'
    node.run(host='0.0.0.0', port=8080)
