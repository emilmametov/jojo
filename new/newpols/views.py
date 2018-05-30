from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from urllib.request import urlopen
from bs4 import BeautifulSoup
from .models import News

# def index(request):
# 	return render(request, 'newpols/home.html')
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


def save_value(collection, obj, value_type):
    value = None
    try:
        if value_type == 'link':
            value = obj[0]['href']
        if value_type == 'title':
            value = obj[0].contents[1].contents[0].string
        if value_type == 'image':
            value = obj[0].contents[0].contents[0].contents[0]['src']            
    except:
        pass

    if value:
        collection.append(value)

   

def requst(request):
    html = urlopen('https://ria.ru/world/').read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    div = soup.find('div', attrs={'class':'b-list'})
    f = []
    href = []
    title = []
    image = []
    for row in div.find_all('div'):
        cols = row.find_all('a')
        f.append(cols)
    for i in range(len(f)):
        save_value(href, f[i], 'link')
        save_value(title, f[i], 'title')
        save_value(image, f[i], 'image')
    return render(request, 'newpols/pars.html', {'cols':f, 'href':href, 'title':title, 'image':image})

def main_page_view(request):
    news = News.objects.all()
    return render(request, 'newpols/home.html', {'news': news})



def sport(request):
    return render(request, 'sports/sport.html')    
