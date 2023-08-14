from django.urls import path
from .views import ClassView,StudentRegistration,StudentLogin,StudentProfileUpdate

urlpatterns = [
    path("add/",ClassView.as_view(),name="add_class"),
    path("register/",StudentRegistration.as_view(),name="registration"),
    path("login/",StudentLogin.as_view(),name="loginn"),
    path("profile/",StudentProfileUpdate.as_view(),name="profilee"),
]