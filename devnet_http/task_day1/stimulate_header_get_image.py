from builtins import *

import requests
from PIL import Image  # pip install Pillow
from io import BytesIO

headers = {
    'Host': '192.168.0.188:8000',
    'Proxy-Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'csrftoken=D65OBa94BpK9mJM3SrtNS0Jj9iI04qmAYcatOjREYSdajqwGfvk9lIwHDIotGS53; '
              'sessionid=epemg8fqihxuzqttfaz3f4yqjb7utvwv'}

r = requests.get('http://192.168.0.188:8000/static/images/logo.jpg', headers=headers, verify=False)

imgContent = r.content

# 在pycharm中展示图片
i = Image.open(BytesIO(r.content))
i.show()

# 下载并保存图片
imageFile = open('qyt_logo.jpg', 'wb')
imageFile.write(imgContent)
imageFile.close()
