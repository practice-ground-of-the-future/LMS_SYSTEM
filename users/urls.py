from django.urls import path
from users.views import login, register, profile, logout, view_profile

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('<int:user_id>/', view_profile, name='user'),
]