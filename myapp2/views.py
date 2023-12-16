from django.shortcuts import render
from django.http import HttpResponse

student_data={'student_name': "ANKUR",
              'student_college': "XYZ",
              'student_city':"Ghaziabad"}
IsActive=True
Channel="Codewith_Durgesh"
data={'student': student_data,
      'ch':Channel,
      'IsActive': IsActive
      }

def test(request):
    if (request.method=='POST'):
        check = request.POST.get('check', '')
        print(check)

    print("this is the test function of the views class")
    return render(request,"about.html",data)
def s(request):
    print("this is the test function of the views class")
    return render(request, "service.html",{})
def c(request):
    print("this is the test function of the views class")
    return render(request,"contact.html",{})