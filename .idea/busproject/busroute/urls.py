
from django.urls import path,include
from .import views
urlpatterns = [

    path('', views.home,name="home"),
    path('home1/', views.home,name="home"),
    path('index/', views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('registersubmit/',views.registersubmit,name="registersubmit"),
    path('loginsubmit/',views.loginsubmit,name="loginsubmit"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogin2/', views.adminlogin2, name="adminlogin2"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('broute/',views.broute,name="broute"),
    path('show/',views.show,name="show"),
    path('show1/',views.show1,name="show1"),
    path('about/',views.about,name="about"),
    path('userlogin1/',views.userlogin1,name="userlogin1"),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>', views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('registeruser/',views.registeruser,name="registeruser"),
    path('contact/',views.contact,name="contact"),
   # path('loginsubmit/',views.loginsubmit,name="loginsubmit"),
]
