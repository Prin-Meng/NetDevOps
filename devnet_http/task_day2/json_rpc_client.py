import requests
import base64

server_ip = '192.168.0.3'
server_port = '8080'
base_url = 'http://' + server_ip + ':' + server_port + '/'
exec_cmd_url = base_url + 'cmd'
upload_url = base_url + 'upload'
download_url = base_url + 'download'

upload_file_dir = './client_upload_file_dir/'
download_file_dir = './client_download_file_dir/'


def json_rpc_client_exec_cmd(exec_cmd):
    request_result = requests.post(exec_cmd_url, json=exec_cmd)
    return request_result.json()


def json_rpc_client_upload(file_name):
    with open(upload_file_dir + file_name, 'rb') as f:
        read_data = f.read()
        print(read_data)
        bytes_b64code = base64.b64encode(read_data)
        print(bytes_b64code.decode())
    request_result = requests.post(upload_url, json={'upload': file_name, 'file': bytes_b64code.decode()})
    return request_result.json()


def json_rpc_client_download(file_name):
    request_result = requests.post(download_url, json={'download': '{0}'.format(file_name)})
    # with open(download_file_dir + file_name, 'w+') as f:
    #     b4code_back = bytes(request_result.get('file'), 'GBK')
    #     file_info = base64.b64decode(b4code_back)
    #     f.write(file_info.decode())
    if request_result.json().get('download_file'):
        return file_name+'下载成功'
    else:
        return request_result.json()


if __name__ == "__main__":
    exec_cmd = {'cmd': 'ipconfig'}
    print(json_rpc_client_exec_cmd(exec_cmd).get('result'))
    exec_cmd = {'cmd': 'pwd1'}
    print(json_rpc_client_exec_cmd(exec_cmd).get('result'))
    exec_cmd = {'cmd1': 'ipconfig'}
    print(json_rpc_client_exec_cmd(exec_cmd).get('result'))

    print(json_rpc_client_upload('logo.jpg'))
    # print(json_rpc_client_download('logo.jpg'))
    # print(json_rpc_client_download('logo_long_new.png'))