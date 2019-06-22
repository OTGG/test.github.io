from lxml import etree

def use_xpath_get_content(content = None,string_xpath = None):
    html = etree.parse(content , etree.HTMLParser())
    result = html.xpath(string_xpath)
    return result