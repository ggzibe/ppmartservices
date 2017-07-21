from django.conf.urls import url
from product_group_app.views import ProductGroupListView, ProductGroupDetailView

urlpatterns = [
    url(r'^list', ProductGroupListView.as_view()),
    url(r'^detail/(?P<pk>[A-Za-z0-9]*)$', ProductGroupDetailView.as_view())
]
