from django.conf.urls import url
from product_type_app.views import ProductTypeListView, ProductTypeDetailView

urlpatterns = [
    url(r'^list', ProductTypeListView.as_view()),
    url(r'^detail/(?P<pk>[A-Za-z0-9]*)$', ProductTypeDetailView.as_view()),
]
