"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# import apps.bookmodule.views  # Import the view from your bookmodule app
# import apps.usermodule.views  

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', apps.bookmodule.views.index),  # Map the root URL to your index view
#     path('hello/', apps.bookmodule.views.index),  # Keep this if you want /hello to work
# ]
# from django.contrib import admin
# from django.urls import path
# import apps.bookmodule.views  # Import your index view
# from django.http import HttpResponse

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', apps.bookmodule.views.index),  # Use the index view for the root URL
#     path('index2/<int:val1>/', apps.bookmodule.views.index2),  # add this line
#     # path('hello/', apps.bookmodule.views.index),  # Keep this for /hello if needed
    

# ]

import apps.bookmodule.views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),
    path('', apps.bookmodule.views.index),
    path('index2/<int:val1>/', apps.bookmodule.views.index2),
    path('users/', include("apps.usermodule.urls")),
] 