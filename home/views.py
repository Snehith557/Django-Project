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
    solved_types = soup.find_all('span', class_='text-xs font-medium text-label-4 dark:text-dark-label-4')
    
    values = {}
    problemType = ['easy_solved','medium_solved','hard_solved','easy_problm','medium_problm','hard_problm']
    # totalProblems = []

    index = 0
    for span in solved_problems:
        values[problemType[index]]=span.text
        index+=1
    
    # index = 0
    for span in solved_types:
        values[problemType[index]] = span.text
        index+=1
    
    print(values)

    
    return values


# leetcode_profile('')

# <div class="whitespace-nowrap text-xs text-label-3 dark:text-dark-label-3 

def homePage(request):
    data = leetcode_profile('')
    # print(data)


    return render(request,'homepage.html',context=data)

