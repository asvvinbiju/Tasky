from django.urls import path
from .views import *

urlpatterns = [
    path("", task),
    path("addtask", add_task),
    path("deletetask/<int:id>", deletetask),
    path("completetask/<int:id>", completetask),
]