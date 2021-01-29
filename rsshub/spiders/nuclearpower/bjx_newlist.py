from rsshub.utils import fetch

domain = 'https://hedian.bjx.com.cn/'


def parse(post):
    item = dict()
    item['title'] = post.xpath('/a/@title').extract_first()
    item['link'] = post.xpath('/a/@href').extract_first()
    item['pubDate'] = post.xpath('/span/text()').extract_first()
    item['description'] = parse_full_text(item['link'])
    return item


def parse_full_text(url):
    tree = fetch(f'{url}', coderule='gbk')
    content = tree.xpath('//div[@class="oiuxclelk"]/following-sibling::div[1]').get()
    if len(content) <= 40 or '下一页' in content:
        content = "\n".join(tree.xpath('//div[@class="oiuxclelk"]/following-sibling::p').getall())
    return content


def ctx(category='NewsList'):
    tree = fetch(f'{domain}{category}', coderule='gbk')
    # posts = tree.css('#wp_news_w6 > table > tbody > tr')
    posts = tree.xpath('//ul[@class="list_left_ul"]//a/parent::li')
    return {
        'title': '北极星核电网-要闻',
        'link': f'{domain}{category}',
        'description': '核电行业垂直门户网站',
        'author': 'airchaoz',
        'items': list(map(parse, posts))
    }
