from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from users.models import User
from firstapp.models import ProfileTask


# Create your views here.


def login(request):
    """Логин"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    """Регистрация"""
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы зарегестрированы!")
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile(request):
    """Редактирование имени пользователя"""
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    context = {'title': 'Профиль',
               'form': form,
               'task': ProfileTask.objects.filter(user=request.user),
               }

    return render(request, 'users/profile.html', context)


def logout(request):
    """Выход из системы"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {'user': user}
    return render(request, 'users/user.html', context)


"""
   Написать авто тестирование задания 
   Отображение exp в профиле
"""
