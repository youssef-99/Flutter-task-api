from django.urls import path

from product.views import *

app_name = 'product'

urlpatterns = [
    path('form-data/', APIFormDataView.as_view(), name='form-data'),
    path('', APIProductListView.as_view(), name='listing'),
    path('add-product/', APIProductView.as_view(), name='add'),
]
