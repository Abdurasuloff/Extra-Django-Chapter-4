from django.urls import path
from .views import index, signup, test_send


urlpatterns = [
    path('', index, name="index"),
    path("signup/", signup, name="signup"),
    path("test/", test_send, name="test_send"),
]
