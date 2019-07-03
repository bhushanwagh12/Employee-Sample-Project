from django.shortcuts import render
from django.http import HttpResponse
import datetime
def demo(request):
    return HttpResponse('<h1 align="center"> Hi am Django Application </h1>')
def date(request):
    date=datetime.datetime.now()
    s='<h1 align="center" The Current Date and Time is :>'+str(date)+'</h1>'
    return HttpResponse(s)
def good_morning(request):
    return HttpResponse('<h1 align="center"> Hello >>>> Good Morning ....!!!!!</h1> ')
def template(request):

    Name='Bhushan'
    Roll_no=101
    Marks=100
    my_dict={'Name':Name,'Roll_no':Roll_no,'Marks':Marks}
    return render(request, 'result.html', context=my_dict)

def reg(request):
    return render(request,'reg.html')
def disp(request):
    name = request.POST['t1']
    age = request.POST['t2']
    email = request.POST['t3']
    address = request.POST['t4']
    data = {'Name': name, 'Age': age, 'Email': email, 'Address': address}
    return render(request, 'disp.html', data)
