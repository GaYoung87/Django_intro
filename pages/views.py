# ages / view
from django.shortcuts import render
import random


# Create your views here. ###엄청중요!!!!
# 작업을하는 것은 함수로 작성이 될 것이고, 그것들을 views에 저장(작성)

def index(request):    # 첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보(페이지를 사용자에게 보여준다.)
# 요청이 들어오면 'index.html'을 보여줌.
    return render(request, 'index.html')   # render의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'introduce.html')


# Templated Variable Example
def dinner(request):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
    }

    # Django template로 context 전달
    return render(request, 'dinner.html', context)
    