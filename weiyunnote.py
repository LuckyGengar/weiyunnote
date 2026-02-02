from bs4 import BeautifulSoup
import requests
import time
import random
import json


def strip_html_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n", strip=True)

def get_weiyun_note(url, password="", only_title=False):
    """
    获取微云笔记内容

    参数:
        url (str): 微云分享链接
        password (str): 微云分享密码（无密码则留空，默认""）
        only_title (bool): 是否只返回笔记标题，默认False（返回完整内容）

    返回:
        str: 笔记标题或去HTML后的完整内容；若出错，返回错误信息
    """
    try:
        share_code = url.rstrip("/").split("/")[-1]

        session = requests.Session()
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
        }
        session.get(url, headers=headers1)

        token = session.cookies.get("wyctoken", "")

        timestamp = str(int(time.time() * 1000))
        api_url = f"https://share.weiyun.com/webapp/json/weiyunShareNoLogin/WeiyunShareView?refer=chrome_windows&g_tk={token}&r={timestamp}"

        seq_number = int(str(int(time.time())) + str(random.randint(1000, 9999)))

        req_header = {
            "seq": seq_number,
            "type": 1,
            "cmd": 12002,
            "appid": 30113,
            "version": 3,
            "major_version": 3,
            "minor_version": 3,
            "fix_version": 3,
            "wx_openid": "",
            "user_flag": 0
        }

        req_body = {
            "ReqMsg_body": {
                "ext_req_head": {
                    "token_info": {
                        "token_type": 0,
                        "login_key_type": 1,
                        "login_key_value": ""
                    },
                    "language_info": {
                        "language_type": 2052
                    }
                },
                ".weiyun.WeiyunShareViewMsgReq_body": {
                    "share_pwd": password,
                    "share_key": share_code
                }
            }
        }

        post_data = {
            "req_header": json.dumps(req_header),
            "req_body": json.dumps(req_body)
        }

        headers2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8"
        }

        response = session.post(api_url, json=post_data, headers=headers2)
        result = response.json()

        if only_title:
            return result["data"]["rsp_body"]["RspMsg_body"]["share_name"]
        else:
            html_content = result["data"]["rsp_body"]["RspMsg_body"]["note_list"][0]["html_content"]
            return strip_html_tags(html_content)

    except Exception as e:
        return f"错误: {str(e)}"
