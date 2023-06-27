from django.shortcuts import render
import random
import requests

# Create your views here.


def index(request):
    username = '홍길동'

    result = {
        'username': username,
    }

    return render(request, 'index.html', result)


def lunch(request):
    menus = ['라면', '김밥', '떡볶이']
    
    pick = random.choice(menus)
    result = {
        'pick': pick,
    }

    return render(request, 'lunch.html', result)

def lotto(request):
    list_num = list(range(1,46))
    pick_num = sorted(random.sample(list_num, 6))
    

    URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1073'

    res = requests.get(URL)

    data = res.json() # .text와는 다르게 json 형식으로 다듬어져 보임

    # print(data['drwtNo1'])

    drwtNo1 = data['drwtNo1']
    drwtNo2 = data['drwtNo2']
    drwtNo3 = data['drwtNo3']
    drwtNo4 = data['drwtNo4']
    drwtNo5 = data['drwtNo5']
    drwtNo6 = data['drwtNo6']

    lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6] # 현재 1등 당첨번호

    num = len(set(lotto_number) & set(pick_num))

    result = {
        'lotto_number': lotto_number,
        'pick_num' : pick_num,
        'num' : num,
    }

    return render(request, 'lotto.html', result)