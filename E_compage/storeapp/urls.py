from django.urls import path
from storeapp.views import home,Product_list,webpage,ProductUpdateDelete,login_user,logout_user,product,text_generation_view,register_user
from cart.views import cart_add
urlpatterns = [
   path('home/',home,name='home'),
   path('',login_user,name='login_user'),
   
   path('product_serializer/',Product_list.as_view(),name='serial_view'),
   path('product_serializer/<int:pk>/',ProductUpdateDelete.as_view()),
   path('login/',login_user,name='login_user'),
   path('logout/',logout_user,name='logout_user'),
   path('register/',register_user,name='register'),
   path('product/<int:pk>',product,name='product'),
    path('generate_text/',text_generation_view, name='generate_text'),
]