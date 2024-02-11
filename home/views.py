from django.shortcuts import render
# from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
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
    context = leetcode_profile('')
    # print(values)

    return render(request,'homepage.html',context)

