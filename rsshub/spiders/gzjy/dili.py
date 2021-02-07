import requests


session = requests.Session()


def login():
    url = "http://gzjx.gdgzeg.com:8082/noteone/login"
    payload = {
        "username": "zg231",
        "password": "123456",
        "rememberMe": "false",
    }
    rsp = session.post(url, data=payload)
    # print(rsp.text)


def get_info():
    url = "http://gzjx.gdgzeg.com:8082/noteone/system/office/listAll"
    payload = {
        "officename": "",
        "uploadname": "",
        "schoolname": "",
        "xuebu": "",
        "kezu": "7",
        "nianji": "",
        "offtype": "",
        "startTime": "",
        "endTime": "",
        "pageSize": "30",
        "pageNum": "1",
        "orderByColumn": "id",
        "isAsc": "desc"
    }
    rsp = session.post(url, data=payload)
    # print(rsp.json()['rows'])
    return rsp.json()['rows']


def parse(post):
    item = dict()
    item['title'] = post['officename']
    item['link'] = "127.0.0.1"
    item['pubDate'] = post['createTime']
    item['description'] = ''
    return item


def ctx():
    login()
    posts = get_info()
    return {
        'title': '光正教学资源平台',
        'link': f'http://gzjx.gdgzeg.com:8082/noteone/login',
        'description': '核电行业垂直门户网站',
        'author': 'airchaoz',
        'items': list(map(parse, posts))
    }


if __name__ == '__main__':
    ctx()
