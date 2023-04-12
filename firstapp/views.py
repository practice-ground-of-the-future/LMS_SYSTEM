from django.shortcuts import render, HttpResponseRedirect
from firstapp.models import Task, TaskCategory, ProfileTask, FileModel
from .forms import UploadFileForm
from django.utils import timezone


# Create your views here.

# Вывод главной страницы
def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'firstapp/index.html', context)


# Вывод странички с заданиями
def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Task.objects.all(),
        'categorys': TaskCategory.objects.all(),
    }
    return render(request, 'firstapp/products.html', context)


# Добавление задания в to-do таблицу
def basket_add(request, product_id):
    product = Task.objects.get(id=product_id)
    product.take = True
    basket = ProfileTask.objects.filter(user=request.user, task=product)

    if not basket.exists():
        ProfileTask.objects.create(user=request.user, task=product)
    else:
        basket = basket.first()
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# Загрузка файлов в таблицу проверки
def upload_file(request, task_id):
    task = ProfileTask.objects.get(id=task_id)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            FileModel.objects.create(profile_task=task, file=request.FILES['file'])
            return render(request, 'firstapp/upload_file.html',
                          {'form': form, 'uploaded_file': uploaded_file, 'task': task})
    else:
        form = UploadFileForm()
    return render(request, 'firstapp/upload_file.html', {'form': form, 'task': task})


# Вывод таблицы проверки
def views_file(request):
    context = {'file': FileModel.objects.all()}
    return render(request, 'firstapp/table.html', context)


# Вывод to-do таблицы
def todo_table(request):
    context = {
        'tasks': ProfileTask.objects.filter(user=request.user),
        'now_time': timezone.now()
    }

    return render(request, 'firstapp/tasktable.html', context)


# Отметка о выполнении задания
def success(request, id_task):
    current_task = FileModel.objects.get(id=id_task).profile_task
    current_task.success = True
    current_user = current_task.user
    current_user.exp += current_task.task.exp
    current_task.save()
    current_user.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
