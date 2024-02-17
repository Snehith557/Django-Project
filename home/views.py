# from django.shortcuts import render
# from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required

from feedback.models import feedBacks
# from django.shortcuts import render

# Create your views here.



def leetcode_profile(request):
    response = requests.get('https://leetcode.com/Snehith1312')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    solved_problems = soup.find_all('span', class_='mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1')
    
    values = dict()
    types = ["Easy","Medium","Hard"]

    iter = 0
    for span in solved_problems:
        # values.append(span.text)
        values[types[iter]] = span.text
        iter+=1
    # print(values)
        
    return values
    # return {'solved_problems': values}


# leetcode_profile('')

# <div class="whitespace-nowrap text-xs text-label-3 dark:text-dark-label-3 

def homePage(request):
    # context = leetcode_profile('')
    context = dict()
    # print(values)

    return render(request,'homepage.html',context)




@login_required
def get_feed_backs(request):
    print("INSIDE FEEDBACKS")

    if request.method == 'GET' and request.user.is_authenticated :


        data = feedBacks.objects.all() 
        dataList = dict()
        # keys = "1"
        iter = 0
        print("-----------------------------------------")
        for item in data:
            
            print(f"Field1: {item.name}, Field2: {item.email},Field3: {item.description}")
            temp = {}
            temp["name"]= item.name
            temp["email"]= item.email
            temp["description"]= item.description
            # temp.append(item.email)
            # temp.append(item.description)
            dataList["key"+str(iter)] = temp
            iter+=1
        print("-----------------------------------------")

    # conte xt = {'form':data}
    # context =
        print("dataList in view:", dataList)

        # open the admin page 
    # return render(request,'admin_login')
        return render(request, 'feedBack_details.html', {'dataList': dataList})
    
    return redirect('/')
