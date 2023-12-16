from django.urls import path
from .views import * 

urlpatterns = [
    path("home/",ask),
    path("emp_add/",emp_add),
    path("emp-delete/<int:emp_id>",emp_del),
    path("emp-update/<int:emp_id>",emp_upd),
    path("do-update/<int:emp_id>",emp_do_update),
]