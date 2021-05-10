from bs4 import BeautifulSoup
import requests
import urllib3


def get_homework_info(Username, Password):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = 'https://qytsystem.qytang.com/accounts/login/'
    username = str(Username)
    password = str(Password)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://qytsystem.qytang.com/accounts/login/',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
    }

    # 建立并保持会话
    client = requests.session()
    # 获取登录页面的内容
    qytang_home = client.get(url, verify=False)

    qytang_soup = BeautifulSoup(qytang_home.text, 'lxml')
    # 找到csrf令牌的值
    csrftoken = qytang_soup.find('input', attrs={'type': "hidden", "name": "csrfmiddlewaretoken"}).get('value')
    # 构建用户名, 密码和csrf值的POST数据
    login_data = {'username': username, 'password': password, "csrfmiddlewaretoken": csrftoken}
    # # POST提交数据到登录页面
    client.post(url, headers=header, data=login_data, verify=False)

    r = client.get('https://qytsystem.qytang.com/python_enhance/python_enhance_homework')

    home_work_soup = BeautifulSoup(r.text, 'lxml')

    # print(home_work_soup.prettify())
    # 格式化打印BeautifulSoup对象
    # print(home_work_soup.find_all('table', id='table-for-student'))

    dict_courses_num = {}
    dict_courses_level = {}

    home_work_list_info = home_work_soup.find('table', id='table-for-student').find('tbody').find_all('tr')

    for evey_home_info in home_work_list_info:
        info = evey_home_info.find_all('td')
        # 列表的1号位课程信息,7号为成绩
        if dict_courses_num.get(info[1].text):
            dict_courses_num[info[1].text] += 1
        else:
            dict_courses_num[info[1].text] = 1

        if dict_courses_level.get(info[7].text):
            dict_courses_level[info[7].text] += 1
        else:
            dict_courses_level[info[7].text] = 1

    return [dict_courses_num, dict_courses_level]
