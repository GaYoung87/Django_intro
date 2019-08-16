# ages / view
from django.shortcuts import render
from datetime import datetime
import random


# Create your views here. ###엄청중요!!!!
# 작업을하는 것은 함수로 작성이 될 것이고, 그것들을 views에 저장(작성)

def index(request):    # 첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보(페이지를 사용자에게 보여준다.)
# 요청이 들어오면 'index.html'을 보여줌.
    return render(request, 'index.html')   # render의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'introduce.html')


# Templated Variable Example
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'name': name,
        'pick': pick,
    }

    # Django template로 context 전달
    return render(request, 'dinner.html', context)
    
    import random


def image(request):
    image_url = 'https://picsum.photos/500'
    context = {
        'image_url': image_url,
    }

    return render(request, 'image.html', context)


def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 * num2
    }
    return render(request, 'times.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    datetimenow = datetime.now()
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)


def isitbirthday(request):
    return render(request, 'isitbirthday.html')


def lotto(request):
    real_lottos = [21, 25, 30, 32, 40, 42]
    lottos = sorted(list(random.sample(range(1, 46), 6)))

    context = {
        'real_lottos': real_lottos,
        'lottos': lottos,
    }
    return render(request, 'lotto.html', context)