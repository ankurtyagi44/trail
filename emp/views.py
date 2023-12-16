from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import EMP


# Create your views here.
def ask (request):
    emps=EMP.objects.all()


    return render(request,"emp/home.html",{'emps':emps})
def emp_add (request):
    if request.method=="POST":
       print("data is coming")
       e_name=request.POST.get('emp_name')
       e_id=request.POST.get('emp_id')
       e_phone=request.POST.get('emp_phone')
       e_address=request.POST.get('emp_address')
       e_dept=request.POST.get('emp_dept')
       e_status=request.POST.get('emp_status')

       e=EMP()
       e.name=e_name
       e.emp_id=e_id
       e.phone_no=e_phone
       e.address=e_address
       e.dept=e_dept
       if e_status is None:
           e.working=False
       else:
           e.working=True

       e.save()
       

       return redirect("/emp/home/")
     
       
    return render(request ,"emp/add.html",{})

def emp_del(request, emp_id):
    m=EMP.objects.get(pk=emp_id)
    m.delete()
   
    return redirect("/emp/home")
def emp_upd(request, emp_id):
    emp=EMP.objects.get(pk=emp_id)
    return render(request,"emp/update.html",{'emp':emp})
   
def emp_do_update(request, emp_id):
    if request.method == 'POST':
        e_name = request.POST.get('emp_name')
        e_id = request.POST.get('emp_id')
        e_phone = request.POST.get('emp_phone')
        e_address = request.POST.get('emp_address')
        e_dept = request.POST.get('emp_dept')
        e_status = request.POST.get('emp_status')

        print(f"Name: {e_name}, ID: {e_id}, Phone: {e_phone}, Address: {e_address}, Dept: {e_dept}, Status: {e_status}")

        m = EMP.objects.get(pk=emp_id)
        m.name = e_name
        m.emp_id = e_id
        m.phone_no = e_phone
        m.address = e_address
        m.dept = e_dept
        if e_status is None:
            m.working = False
        else:
            m.working = True

        m.save()
        print("Employee Updated Successfully")

        return redirect("/emp/home/")
    else:
        print("No POST Data Received")
        return redirect("/emp/home/")

