from django.urls import path
from .views import ( StudentLogin,StudentRegister,StudentLogout )

urlpatterns = [
    path('login/',StudentLogin.as_view(),name='login'),
    path('signup/',StudentRegister.as_view(),name='signup'),
    path('logout/',StudentLogout.as_view(),name='logout')
]