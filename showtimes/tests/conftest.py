# import os
# import sys
# import pytest
# from rest_framework.test import APIClient
#
# from showtimes.models import Cinema, Screening, Movie
#
# from movielist.models import Person
# from .testy import faker, create_fake_cinema
#
# sys.path.append(os.path.dirname(__file__))
#
# @pytest.fixture # tu przygotowujemy materiały do testów
# def set_up_cinema():
#     lst = []
#     for n in range(10):
#         p = Cinema.objects.create(namec = n, city=n, movies=n)
#         lst.append(p)
#     for y in range(5):
#         create_fake_cinema
#     return lst, y
# #
# # @pytest.fixture
# # def client():
# #     client = APIClient()
# #     return client
# #
# #
# # @pytest.fixture
# # def set_up():
# #     for _ in range(5):
# #         Person.objects.create(name=faker.name())
# #     for _ in range(3):
# #         create_fake_movie()
#
#
# @pytest.fixture
# def client():
#     client = APIClient()
#     return client
#
#
# @pytest.fixture
# def set_up():
#     for _ in range(5):
#         Person.objects.create(name=faker.name())
#     for _ in range(10):
#         create_fake_movie()
#     for _ in range(3):
#         create_fake_cinema()
#
# @pytest.fixture  # tu przygotowujemy materiały do testów
# def cinemas():
#     lst = []
#     for n in range(10):
#         c = Cinema.objects.create(namec=n, city=n, movies = n)
#         lst.append(c)
#     return lst
#
# @pytest.fixture
# def movie(persons):
#     person = persons[0]  ##jak to było z ta listą?
#     return Movie.objects.create(title='Owoc który sie nie kula',
#                                 year=2022, director=person)
#
#
# @pytest.fixture
# def movies(persons):
#     lst = []
#     for person in persons:
#         m = Movie.objects.create(title="mis", year='1999', director=person)
#         lst.append(m)
#     return lst
#
#
# @pytest.fixture
# def user():
#     u = User.objects.create(username='tadeusz')
#     return u
#
#
# @pytest.fixture
# def user_with_permission():
#     u = User.objects.create(username='tadeusz')
#     permission = Permission.objects.get(codename='add_comment')
#     u.user_permissions.add(permission)
#     return u



import os
import sys

import pytest
from faker import Faker
from rest_framework.test import APIClient

from movielist.models import Person
from movielist.tests.utils import create_fake_movie
from showtimes.tests.utils import create_fake_cinema

sys.path.append(os.path.dirname(__file__))
faker = Faker("pl_PL")


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for _ in range(5):
        Person.objects.create(name=faker.name())
    for _ in range(10):
        create_fake_movie()
    for _ in range(3):
        create_fake_cinema()

