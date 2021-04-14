import base64

with open('snmpv2_get_file.py', 'rb') as f:
    read_data = f.read()
    bytes_b64code = base64.b64encode(read_data)
    send_obj = {'upload_file': bytes_b64code.decode()}
    # print(send_obj)

    b4code_back = bytes(bytes_b64code.decode(), 'utf8')
    signature = base64.b64decode(b4code_back)
    print(signature.decode())