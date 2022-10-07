import json
from datetime import date
import requests
import os


WEBHOOK = os.environ.get('WECHATWORK_WEBHOOK')

def get_today():
    today = date.today()
    d = int(today.strftime("%d")) % 10
    return d


def get_menu():
    menu = (
        '咸菜蒸肉饼、尖椒炒秘制头皮、手撕包菜、青菜',
        '皖鱼焖萝卜、酸菜煲五花肉、手撕包菜、青菜',
        '白切鸡、海鲜豆腐、干锅散花菜、青菜',
        '花生焖猪脚、麻婆豆腐、苦瓜吊菜焖豆角、青菜',
        '蒸鱼块，五花肉炒豆腐干、炒洋葱、青菜',
        '秘制头皮炒摘菜、山城毛血旺、手撕包菜、青菜',
        '酸甜香酥肉、猪肠猪红煲、焖南瓜、青菜',
        '炒五花肉，焖笋干、青瓜、青菜',
        '香菇蒸鸡、回锅肉、焖冬瓜、青菜',
        '红焖肉、西红柿焖蛋、粉丝蒸娃娃菜、青菜',
    )
    today = get_today()
    tomorrow = (get_today() + 1) % 10
    menu = {'today': menu[today], 'tomorrow': menu[tomorrow]}

    return menu


def get_message():
    menu = get_menu()
    today_menu = menu['today']
    tomorrow_menu = menu['tomorrow']
    message = {
        "msgtype": "news",
        "news": {
            "articles": [{
                "title":
                "上言加餐食，下言长相忆",
                "description":"\n" + "🐟 " + today_menu + "\n\n" + "🐟 " + tomorrow_menu,
                "url":
                "https://www.baidu.com/s?wd=" + today_menu,
                "picurl":
                "https://i.loli.net/2020/11/18/3zogEraBFtOm5nI.jpg"
            }]
        }
    }
    return message


def send_message():
    headers = {"Content-Type": "text/plain"}
    send_url = WEBHOOK
    send_data = get_message()
    res = requests.post(url=send_url, headers=headers, json=send_data)
    print(res.text)


def main_handler():
    send_message()
    return ("执行完成")

main_handler()
