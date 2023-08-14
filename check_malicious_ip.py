import requests

# 设置默认的apikey（注意：仅供示例使用，实际应该填入你的实际apikey）
DEFAULT_API_KEY = "example"


def check_malicious_ip(formatted_ips, apikey=DEFAULT_API_KEY):

    url = "https://api.threatbook.cn/v3/scene/ip_reputation"

    query = {
        "apikey": apikey,
        "resource": formatted_ips,
        "lang": "zh"
    }

    response = requests.get(url, params=query)

    return response.json()
