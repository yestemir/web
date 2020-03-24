from django.urls import path
from api.views import product_list, getproduct, category_list, getcategory, getproductsbycategory

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', getproduct),
    path('categories/', category_list),
    path('categories/<int:category_id>', getcategory),
    path('categories/<int:category_id>/products', getproductsbycategory),

]