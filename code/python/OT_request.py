# -*- coding: utf-8 -*-
import requests
import codecs
import os
import logging
import re

def get_request(url,
                max_redirects=30,
                proxy=None,
                fname=None,
                fname_404=None,
                retry=3,
                timeout=10,
                is_get_real_url=False):
    """
    请求
    :param url:
    :param max_redirects:
    :param proxy:
    :param fname:
    :param fname_404:
    :param retry:
    :param timeout:
    :return:
    """

    ret = False
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 " \
                            "(KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"

    s = requests.session()
    s.max_redirects = max_redirects

    s.proxies = proxy

    while retry > 0:
        try:

            r = s.request(url=url,
                          method="GET",
                          headers=headers,
                          timeout=timeout

                          )

            if r.reason == "OK":

                if fname:
                    if r.url != url:

                        # exists redirect
                        if is_get_real_url:
                            content = "<html><head><title>%s</title></head>" \
                                      "<body>%s</body></html>" % (r.url, url)
                        else:
                            content = r.content


                    else:
                        content = r.content

                    with codecs.open(fname, mode='wb') as fw:
                        fw.write(content)
                    ret = True
                else:
                    ret = r

                retry = 0

            elif r.reason == "Not Found":
                if fname_404:
                    with codecs.open(fname_404, mode='ab') as fw:
                        fw.write("%s%s" % (url, os.linesep))
                retry = 0

            else:

                logging.info("[url]: retry:%d %s, %s" % (retry, url, r.reason))
                retry = retry - 1

        except Exception as e:


            e = str(e)


            if  is_get_real_url:
                ret = parse_request_error_str(e)
                if ret:

                    content = "<html><head><title>%s</title></head>" \
                              "<body>%s</body></html>" % (ret, url)

                    with codecs.open(fname, mode='wb') as fw:
                        fw.write(content)
                    ret = True
                    retry = 0
            else:

                logging.info("[REQUEST]: retry:%d %s %s" % (retry, url, e))

                retry = retry - 1

    return ret

def parse_request_error_str(st):
    """

    :param st:
    :return:
    """

    pattern = re.compile(
        r"HTTPS?ConnectionPool\(host='([^\x22]+)', port=(\d+)\): Max retries exceeded with url: (/\S*) \(")
    match = re.match(pattern, st)
    if match:
        host, port, url = match.groups()
        port = str(port)
        if port == 443:
            ret = "https://%s%s" % (host, url)
        else:
            ret = "http://%s%s" % (host, url)
        return ret