from django.urls import path,include
from .views import orm_test
urlpatterns = [
    path("", orm_test,name="check"),
]