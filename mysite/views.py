from django.shortcuts import HttpResponse
from django.shortcuts import render

val = ""
x = {}
i = 0
dict = {'name1': "Business", 'name2': "Entertainment", 'name3': "Health", 'name4': "Science", 'name5': "Sports",
        'name6': "Technology"}


def Akhbaar(request):
    global i
    i = 0
    return render(request, 'template3.html', dict)


def funcy(request):
    import requests
    import json
    global x
    global i
    if request.POST.get('move') == 'move':
        i = i + 1
        return render(request, 'template2.html', x[i])
    if i == 0:
        apikey = request.POST.get('inputPassword', False)
        for key, value in dict.items():
            if (request.POST.get('categories', 'off')) == key:
                global val
                val = value
        url = f"http://newsapi.org/v2/top-headlines?country=in&category={val}&apiKey={apikey}"
        data = requests.get(url=url).text
        news = json.loads(data)
        x = news['articles']
        return render(request, 'template2.html', x[i])


def funcy2(request):
    def speaky(str):
        from win32com.client import Dispatch
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(str)

    speaky("The News for Today is")

    speaky(x[i]['title'])
    speaky(x[i]['description'])
    speaky(f"For details visit the website")
    speaky("Thanks for Listening")
    return render(request, 'template2.html', x[i])


def aboutus(request):
    return render(request, 'template4.html')
