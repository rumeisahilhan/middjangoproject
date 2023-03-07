from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def project(request):
    return render(request,'project.html')
def staff(request):
    return render(request,'staff.html')
