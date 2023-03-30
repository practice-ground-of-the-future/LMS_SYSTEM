from django.urls import path
from firstapp.views import products, basket_add, upload_file, views_file, todo_table, success

app_name = 'firstapp'

urlpatterns = [
    path('test/', products, name='index'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('upload/<int:task_id>', upload_file, name='upload_file'),
    path('table/', views_file, name='views_file'),
    path('task/', todo_table, name='todo_table'),
    path('table/<int:id_task>', success, name='success')
]
