from django.urls import path
from . import views

urlpatterns = [
    # pages
    path('', views.cust_home, name = "cust_home"),
    path('cust_products/', views.cust_products, name = "cust_products"),
    path('loginForm/', views.loginForm, name = "loginForm"),
    path('registrationForm/', views.registrationForm, name = "registrationForm"),
    path('logout_user/', views.logout_user, name = "logout_user"),

    # user page
    path('userpage/', views.userpage, name = "userpage"),


    # dynamic urls
    path('order_product/<str:id>', views.order_product, name = "order_product"),
    path('customer/<str:id>', views.customer, name = "customer"),
    path('update_data/<str:id>', views.updateOrder, name = "updateOrder"),
    path('deteleOrder/<str:id>', views.deteleOrder, name = "deteleOrder"),
    # path('profile/<str:id>', views.profile, name = "profile"),

    # db table
    path('dbcustomer/', views.dbcustomer, name = "dbcustomer"),
    path('dborder/', views.dborder, name = "dborder"),
    path('dbproduct/', views.dbproduct, name = "dbproduct"),
]