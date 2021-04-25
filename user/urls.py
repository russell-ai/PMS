from django.urls import path
from . import views
from .views import MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('change-password/', MyPasswordChangeView.as_view(), name='password-change'),
    path('change-password/done', MyPasswordResetDoneView.as_view(), name='password-change-done'),

]
