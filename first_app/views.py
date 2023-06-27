from django.shortcuts import render
import random
import requests
from faker import Faker

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
        'pick_num' : pick_num,
        'lotto_number': lotto_number,
        'num' : num,
    }

    return render(request, 'lotto.html', result)


def hello(request,name):
    result = {
        'name': name,
    }
    return render(request, 'hello.html', result)


def cube(request, num):
    result ={
        'num' : num,
        'cube' : num ** 3,
    }
    return render(request, 'cube.html', result)

def posts(request):
    fake = Faker()

    post_dict = {}
    for i in range(20):
        post_dict[fake.text(max_nb_chars=10)] = fake.text()
    result = {
        'post_dict' : post_dict
    }
    return render(request, 'posts.html', result)