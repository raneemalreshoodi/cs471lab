from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name="books.index"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.formatting, name="books.formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>/', views.viewbook),
    path('search', views.search_books, name="books.search"),
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query/', views.complex_query, name='complex_query'),
    path('lookup/query/', views.lookup_query, name='lookup_query'),
    path('lab9/task1', views.task1, name='task1'),
    path('lab9/task2', views.task2, name='task2'),
    path('lab9/task3', views.task3, name='task3'),
    path('lab9/task4', views.task4, name='task4'),
    path('lab8/task5/', views.task5, name='task5'),
    path('lab8/task7/', views.task7, name='task7'),

]