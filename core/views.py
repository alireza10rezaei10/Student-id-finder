from django.http import HttpResponse
from .models import Student
from bs4 import BeautifulSoup
import json
import requests

# Create your views here.
URL = 'http://physics.sharif.edu/post/bs_email.php'

def update(request):
    if request.method == 'GET':
        page = requests.get(URL).text
        students = BeautifulSoup(page, 'html.parser').find('center').find_all('tr')
        
        for s in students:
            try:
                student_number = s.find('b').text
                name           = s.find('a')['href'].split('~')[1]
                student = Student.objects.get_or_create(student_number=student_number, name=name)
                print(student)
            except:
                pass
        return HttpResponse('done !\n')


def get(request, type, data):
    if type == 'name':
        students = Student.objects.filter(name__contains=data)
    else:
        students = Student.objects.filter(student_number__contains=data)
    
    found_data = {}
    for s in students:
        found_data[s.name] = s.student_number
    
    return HttpResponse(json.dumps(found_data))