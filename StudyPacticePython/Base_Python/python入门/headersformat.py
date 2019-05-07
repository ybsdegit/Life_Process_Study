headers = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=F5D7772D2678EA7C3D7993CB14091E2B; _CSRFCOOKIE=52F7D4CBEAF12DEE47E8AEE18029565A6FBA9855; EPTOKEN=52F7D4CBEAF12DEE47E8AEE18029565A6FBA9855
Host: ggzyjy.jiangxi.gov.cn
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
"""
hs = headers.split('\n')
b = [k for k in hs if len(k)]
e = b
f = {(i.split(":")[0], i.split(":", 1)[1].strip()) for i in e}
g = sorted(f)
index = 0
print("{")
for k, v in g:
    print(repr(k).replace('\'', '"'), repr(v).replace('\'', '"'), sep=':', end=",\n")
print("}")

