from django.conf.urls import url
from employee_app.views import EmployeeRoleListView, EmployeeRoleDetailView, EmployeeListView, EmployeeDetailView

urlpatterns = [
    url(r'^rolelist', EmployeeRoleListView.as_view()),
    url(r'^roledetail/(?P<pk>[A-Za-z0-9]*)$', EmployeeRoleDetailView.as_view()),
    url(r'^list', EmployeeListView.as_view()),
    url(r'^detail/(?P<pk>[A-Za-z0-9]*)$', EmployeeDetailView.as_view()),
]
