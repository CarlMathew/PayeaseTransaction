from django.urls import path
from . import views


urlpatterns = [
    path("register", view=views.registration),
    path('regis', view=views.register),
    path('reload', view=views.reload),
    path("reload_amount", view=views.reload_card)
]
