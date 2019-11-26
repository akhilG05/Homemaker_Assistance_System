from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from django.template import Template, Context, loader
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
import json
from newsapi.newsapi_client import NewsApiClient
  
@login_required
def index(request): 
      
    newsapi = NewsApiClient(api_key ='60b42cb82ffe4033a251dddb29af48f1') 
    
    india = newsapi.get_top_headlines(country='in') 
    world = newsapi.get_top_headlines(language='en') 
    # business = newsapi.get_top_headlines(category='business')
    entertainment = newsapi.get_top_headlines(country='in', category='entertainment', language='en')
    health = newsapi.get_top_headlines(country='in', category='health', language='en')
    # science = newsapi.get_top_headlines(category='science')
    technology = newsapi.get_top_headlines(country='in', category='technology', language='en')
    sports = newsapi.get_top_headlines(country='in', category='sports', language='en')
    # general = newsapi.get_top_headlines(category='general')


    l1 = india['articles']
    l2 = world['articles']
    # l3 = business['articles']
    l4 = entertainment['articles']
    l5 = health['articles']
    # l6 = science['articles']
    l7 = technology['articles']
    l8 = sports['articles']
    # l9 = general['articles']
    
    desc1 = [] 
    news1 = [] 
    img1 = [] 
  
    for i in range(len(l1)): 
        f = l1[i] 
        news1.append(f['title']) 
        desc1.append(f['description']) 
        img1.append(f['urlToImage']) 

    desc2 = [] 
    news2 = [] 
    img2 = [] 
  
    for i in range(len(l2)): 
        f = l2[i] 
        news2.append(f['title']) 
        desc2.append(f['description']) 
        img2.append(f['urlToImage']) 
    
    # desc3 = [] 
    # news3 = [] 
    # img3 = [] 
  
    # for i in range(len(l3)): 
    #     f = l3[i] 
    #     news3.append(f['title']) 
    #     desc3.append(f['description']) 
    #     img3.append(f['urlToImage']) 
            
    desc4 = [] 
    news4 = [] 
    img4 = [] 
  
    for i in range(len(l4)): 
        f = l4[i] 
        news4.append(f['title']) 
        desc4.append(f['description']) 
        img4.append(f['urlToImage']) 
            
    desc5 = [] 
    news5 = [] 
    img5 = [] 
  
    for i in range(len(l5)): 
        f = l5[i] 
        news5.append(f['title']) 
        desc5.append(f['description']) 
        img5.append(f['urlToImage']) 
            
    # desc6 = [] 
    # news6 = [] 
    # img6 = [] 
  
    # for i in range(len(l6)): 
    #     f = l6[i] 
    #     news6.append(f['title']) 
    #     desc6.append(f['description']) 
    #     img6.append(f['urlToImage']) 

    desc7 = [] 
    news7 = [] 
    img7 = [] 
  
    for i in range(len(l7)): 
        f = l7[i] 
        news7.append(f['title']) 
        desc7.append(f['description']) 
        img7.append(f['urlToImage']) 
    
    desc8 = [] 
    news8 = [] 
    img8 = [] 
  
    for i in range(len(l8)): 
        f = l8[i] 
        news8.append(f['title']) 
        desc8.append(f['description']) 
        img8.append(f['urlToImage']) 
            
    # desc9 = [] 
    # news9 = [] 
    # img9 = [] 
  
    # for i in range(len(l9)): 
    #     f = l9[i] 
    #     news9.append(f['title']) 
    #     desc9.append(f['description']) 
    #     img9.append(f['urlToImage']) 


    mylist1 = zip(news1, desc1, img1)
    mylist2 = zip(news2, desc2, img2)
    # mylist3 = zip(news3, desc3, img3)
    mylist4 = zip(news4, desc4, img4)
    mylist5 = zip(news5, desc5, img5)
    # mylist6 = zip(news6, desc6, img6)
    mylist7 = zip(news7, desc7, img7)
    mylist8 = zip(news8, desc8, img8)
    # mylist9 = zip(news9, desc9, img9)
     
    # return render(request, 'newsapp/index.html', context ={"mylist":mylist1, "mylist2":mylist2}) 
    
    # mylist = zip(news1, desc1, img1)
  
    return render(request, 'newsapp/index.html', context ={"mylist1":mylist1, "mylist2":mylist2, "mylist4":mylist4, "mylist5":mylist5, "mylist7":mylist7, "mylist8":mylist8})