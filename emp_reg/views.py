from django.shortcuts import render
from emp_reg.models import Employee


from datetime import datetime


# Create your views here.

def welcome_page(request):
    return render(request, template_name="employee.html")


def save_update_employee(request):
    error_message = ''
    success_message = ''
    if request.method == 'POST':
        formdata = request.POST
        print('FORMDATA :', formdata)
        eid = formdata.get('eid')
        enm = formdata.get('enm')
        if not enm:
            error_message = "Employee Name Cannot be Empty..!"
        else:
            eage = formdata.get('eage')
            erole = formdata.get('role')
            email = formdata.get('eemail')
            edj = formdata.get('edate')
            edr = formdata.get('address')
            ephone = formdata.get('ephone')
            currentDate = datetime.now()
            parts = edj.split("/")  # 6/01/2023
            # currentDate.day = parts[0]#01
            # currentDate.month = parts[1]#12
            # currentDate.year = parts[2]#2023
            edj = datetime(int(parts[2]), int(parts[1]), int(parts[0]))
            emp = Employee(name=enm, age=eage, email=email, role=erole, phone_num=ephone,
                           joiningDate = edj, address=edr)
            emp.save()
            success_message = "Employee Record Saved..!"
        return render(request, "employee.html", {"success_message": success_message, "error_message": error_message})


def edit_employee(request):
    pass


def delete_employee(request):
    pass
