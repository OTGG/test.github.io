# -*- coding: utf-8 -*-
# version: 1.00

import sys,socket

url = "www.baidu.com"
result = []
ret = socket.getaddrinfo(url,None)
for i in ret:
    result.append(i[4][0])

result = list(set(result))
print result

url_ping = 'http://ping.chinaz.com/' + url

# import dns.resolver

# result = dns.resolver.query('baidu.com', 'A')
# for ipval in result:
#     print('IP', ipval.to_text())

