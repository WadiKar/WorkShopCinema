"""moviebase URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from showtimes.views import CinemaView, CinemaListView, ScreeningListView, ScreeningView
from movielist.views import MovieListView, MovieView, PersonListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', MovieListView.as_view()),
    path('movies/<int:pk>/', MovieView.as_view(), name='movies-detail'),
    path('cinema/<int:pk>/', CinemaView.as_view()),
    path('cinemas/', CinemaListView.as_view(), name='cinema-list'),
    path('screening/', ScreeningListView.as_view()),
    path('screening/<int:pk>/', ScreeningView.as_view(), name='screening-detail'),
    path('person/', PersonListView.as_view())

]
