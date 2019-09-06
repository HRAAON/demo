import requests
from pprint import pprint
url = "http://pifu.dd373.com/api/NoticeAdmin/addnotice"

#请求体中的参数
data = {
  "Title": "绍斐test",
  "OrderNumber": 4,
  "Color": "#f2ad79",
  "Overview": "青可权风容器较电别市",
  "IsUsable": 0,
  "IsPupUp": 1,
  "IsScrolling": 1,
  "Content": "车明看话里起记收至团于织八党养委其"
}

headers = {

    'cookie':'manage_session=YDy249gBcbIWpLhbGRquuz8Z605WrrW5sh3bFt5YKVDL1cjWIN4jQsBUl%2b%2f1AZJeenWSx41bT6jpFbv8DgCEdF2EFgQxVp0xQRXCaIvPGfuWVLMDYVNlyeQD6kkD%2fgcl5BOwS%2bIVdJKm9joZlWBqW74ZpPZ2XK8UYlgyAg6NZy8vDOtVxwpd8wscorgcEH1767zhw60VkfYFWdogPlwX1VUYjUudlILBoe8HUf4wTL9gU%2fK5AwezJRlz3hwESAoNs2%2bPDw11IgaV3gU%2fDkx%2bmA8RHtnx306XPg6e3RtRzWYnvt9hq4AV3d%2bFZCHSfbc%2fcYz2W86gL81l2XMJC27OVA%3d%3d; path=/; domain=.dd373.com; Expires=Tue, 19 Jan 2038 03:14:07 GMT;'
    }

response = requests.request("POST", url, headers=headers, data=data)
ret = response.json()
pprint(ret, indent=5)

# 对返回值进行断言
SD = ret['StatusData']
assert ret["StatusCode"]=="0"
assert ret["StatusMsg"]=="请求成功"
assert ret["StatusData"]!=True
assert SD['ResultCode']=="0"
assert SD["ResultMsg"]=="操作成功"

print('\n========= 添加公告：test case pass =============')


