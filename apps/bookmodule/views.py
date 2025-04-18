from django.shortcuts import render  # Add this import
from django.http import HttpResponse
# from .models import Book
from .models import Student
from django.db.models import Q
from django.db.models import Count

def task7(request):
    city_counts = Student.objects.values('address__city').annotate(num_students=Count('id'))
    return render(request, 'bookmodule/task7.html', {'city_counts': city_counts})

from django.db.models import Count
from django.shortcuts import render
from .models import Student, Course, Department

def task1(request):
    departments = Department.objects.annotate(num_students=Count('student'))
    return render(request, 'bookmodule/task1.html', {'departments': departments})

def task2(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task2.html', {'courses': courses})


def task3(request):
    departments = Department.objects.all()
    data = []
    for dept in departments:
        oldest_student = dept.student_set.order_by('id').first()
        if oldest_student:
            data.append({'department': dept.name, 'student': oldest_student.name})
    return render(request, 'bookmodule/task3.html', {'data': data})

def task4(request):
    departments = Department.objects.annotate(student_count=Count('student')) \
                                    .filter(student_count__gt=2) \
                                    .order_by('-student_count')
    return render(request, 'bookmodule/task4.html', {'departments': departments})


from django.db.models import Count, Sum, Avg, Max, Min

def task5(request):
    aggregation = Book.objects.aggregate(
        num_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'aggregation': aggregation})


def simple_query(request):

    books = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': books})


def complex_query(request):
    
    expensive_books = Book.objects.filter(price__gt=20.0)
    return render(request, 'bookmodule/bookList2.html', {'books': expensive_books})

def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False) \
                          .filter(title__icontains='The') \
                          .filter(edition__gte=2) \
                          .exclude(price__lte=20)[:10]

    if len(mybooks) > 1:
        return render(request, 'bookmodule/lookup.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def index2(request, val1=0):
    return HttpResponse(f"value1 = {val1}")


def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def links(request):
    return render(request, "bookmodule/links.html")

def formatting(request):
    return render(request, "bookmodule/formatting.html")

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, "bookmodule/tables.html")


def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def search_books(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        search_in_title = request.POST.get('option1')
        search_in_author = request.POST.get('option2')
        books = []

        for book in __getBooksList():
            match = False
            if search_in_title and keyword in book['title'].lower():
                match = True
            if search_in_author and keyword in book['author'].lower():
                match = True
            if match:
                books.append(book)

        return render(request, "bookmodule/bookList.html", {'books': books})

    return render(request, "bookmodule/search.html")