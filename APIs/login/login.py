"""百里腾登录接口"""

API_NAME = 'login'

# 地址信息
uri_scheme = 'https'
endpoint = 'qa-gateway.fxqifu.net'
resource_path = '/pangu/fleshopy/merchant/site-user/site/login'
url = uri_scheme + u'://' + endpoint + resource_path


# 请求消息参数
req_param = {
    "credential": "e10adc3949ba59abbe56e057f20f883e",
    "identityType": [2],
    "identifier": "15512345678",
    "siteId": 100383
}

# 响应消息参数
res_param = {
    "success": True,
    "code": "2000",
    "message": None,
    "data": {
        "personalUserId": "975609114",
        "token": "958576f3009a4bb6ae569c0b6a818711-975609114-1-personal",
        "loginWayId": None
    }
}


def _separate_data(data, prefix='req.'):  # 去前缀
    pfx = prefix
    result = {}
    for key, value in data.items():  # 遍历字典
        if key.startswith(pfx):  # 键的前缀req.
            req_key = key[len(pfx):]
            result[req_key] = value
    return result
