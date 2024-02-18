
from django.urls import path
from .import views
app_name='med'
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/',views.detail,name='detail'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('login/',views.login,name='login'),
]