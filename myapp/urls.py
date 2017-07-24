from django.conf.urls import include, url
from myapp.views import Main

urlpatterns = [
    url(r'^$', Main.as_view()),
    url(r'^auth/', include('auth_app.urls')),
    url(r'^users/',include('user_app.urls')),
    url(r'^employees/',include('employee_app.urls')),
    url(r'^product/types/',include('product_type_app.urls')),
    url(r'^product/groups/',include('product_group_app.urls')),
]
