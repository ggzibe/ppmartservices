from django.conf.urls import url
from product_app.views import ProductListView, ProductDetailView

urlpatterns = [
    url(r'^list', ProductListView.as_view()),
    url(r'^detail/(?P<pk>[A-Za-z0-9]*)$', ProductDetailView.as_view()),
]
