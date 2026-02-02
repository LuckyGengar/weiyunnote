from weiyunnote import get_weiyun_note

if __name__ == "__main__":
    url = "https://share.weiyun.com/FsonvDt7"
    content = get_weiyun_note(url)
    print(content)