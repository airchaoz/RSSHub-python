from rsshub.utils import fetch

domain = 'https://snse.ecut.edu.cn/1289/list.htm'


def parse(post):
    item = dict()
    item['title'] = post.xpath('@title').extract_first()
    item['link'] = f"https://snse.ecut.edu.cn{post.xpath('@href').extract_first()}"
    item['description'] = parse_full_text(item['link'])
    return item


def parse_full_text(url):
    tree = fetch(f'{url}')
    return tree.xpath('//td[@class="article"]').get()


def ctx(category=''):
    tree = fetch(f'{domain}')
    # posts = tree.css('#wp_news_w6 > table > tbody > tr')
    posts = tree.xpath('//td[@class="content"]//tbody//a')
    return {
        'title': '东华理工大学-核科学与工程学院',
        'link': domain,
        'description': '东华理工大学-核科学与工程学院',
        'author': 'airchaoz',
        'items': list(map(parse, posts))
    }


a = ctx()
print(a)
