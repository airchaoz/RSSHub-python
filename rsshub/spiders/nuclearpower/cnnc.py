from rsshub.utils import fetch

domain = 'http://www.cnnc.com.cn'


def parse(post):
    item = dict()
    item['title'] = post.xpath('@title').extract_first()
    item['link'] = domain + post.xpath('@href').extract_first()
    item['description'] = parse_full_text(item['link'])
    return item


def parse_full_text(url):
    tree = fetch(f'{url}')
    content = "\n".join(tree.xpath('//div[@class="CONTENT"]').getall())
    return content


def ctx(category="300557"):
    tree = fetch(f'{domain}/cnnc/300555/{category}/index.html')
    # posts = tree.css('#wp_news_w6 > table > tbody > tr')
    posts = tree.xpath('//ul[@class="xwzxList"]//a')
    return {
        'title': '中国核工业集团',
        'link': f'{domain}cnnc/300555/{category}/index.html',
        'description': '中国核工业集团',
        'author': 'airchaoz',
        'items': list(map(parse, posts))
    }


if __name__ == '__main__':
    a = ctx()
