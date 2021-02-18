from flask import Response
import requests
from parsel import Selector

DEFAULT_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/69.0.3497.100 Safari/537.36'}


class XMLResponse(Response):
    def __init__(self, response, **kwargs):
        if 'mimetype' not in kwargs and 'contenttype' not in kwargs:
            if response.startswith('<?xml'):
                kwargs['mimetype'] = 'application/xml'
        return super().__init__(response, **kwargs)


def fetch(url: str, headers=None, proxies: dict = None, coderule: str = ""):
    if headers is None:
        headers = DEFAULT_HEADERS
    # if coderule is None:
    #     coderule = 'utf-8'
    try:
        res = requests.get(url, headers=headers, proxies=proxies)
        res.raise_for_status()
    except Exception as e:
        print(f'[Err] {e}')
    else:
        if coderule == "":
            html = res.text
        else:
            html = res.content.decode(coderule)
        tree = Selector(html)
        return tree
