import requests   #引入requests库
from pprint import pprint   #引入pprint pprint就是打印出你的响应内容

#这个是的测试接口
url = "http://pifu.dd373.com/api/notice/noticeviewlist"

#这个是你的请求参数：
querystring = {"pageIndex":"1","pageSize":"20"}

# 这个是你的请求头：
headers = {
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "2c355245-aa14-41ee-92d4-b1a20ab9f28b,855e6cc7-f7b1-4fd8-9867-c9500a856d23",
    'Host': "pifu.dd373.com",
    'cookie': "member_session=evTpkR3WHlaNQQDtFnRIqh3l4B2XwcXOGxBQ468bvKZVxUPQcB2xhwMoOXm%2bgNtovta4gI2awFZH10vVkJamGqaMLR2hOgmpbssG7zPH5HkUZB3PLBVvNLMRqQynCe5wMbSWJuWJCe48LPcC0E9zzSWFk64c%2fRjureW0Hqn5CoVbNqmioDoe7UhTSp0%2bOWz%2fudVosxumlflhsYrJgEY4MTad2xI9V3Vccn0U%2bPi8luGyOoCWkWvOgPt6VZ7mEbvFWc4a8YfB68%2b3FmBBetnV0YIbONqcB8qXOUyc50KvXadTEDg8NQwsgL1xAMtSP4zWiDW4152wJDZQlJSjZfKzPg%3d%3d; ASP.NET_SessionId=pjrynn3r3dzzafp2hz54hy1u; manage_session=a4mIxeIJRKBetYSLLrTvp8vzWzYXTVWpafQa84xEg9AMNcp8jCMAOrxnwmtnpEqtDtVYxQJcBxRQ78sPq6Wi0LBnstQsYxXG5Lm7HU%2bFDeSRYnEk27eyrv8XBYhRAvc15YxKTdg7qrYDvHFCtp5MdYmvakh4CGXmSUq0RBYlmbAZTELBAt41Q3FlngJAyAJ0xmfeLIn1%2b%2bc2upWD1TmMHRB4qRikgfpMU2LlSL1jlA1k3v%2bJvZtNONhE7rM77SXLqjm78JL9eiKozhBmrQ%2bkOOnALdISCPEKLIZ7esSOcg%2frNdCNMu1Zjk0OYZELj%2bqFS2VqViDXAjTQMmM4NokHxQ%3d%3d",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

# 发送这次请求
response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

bodyRet = response.json()  #转换成json格式的字符串
pprint(bodyRet)    #pprint 打印出的是按照响应内容的格式打印。
