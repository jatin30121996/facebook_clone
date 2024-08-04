from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.login, name="login"),
    path("about/", views.createAccount, name="createAccount"),
    path("abouts/<str:phone>", views.abouts, name="abouts"),
    path("home/<str:phone>", views.home, name="home"),
    path("contact/<str:phone>", views.contact, name="contact"),
    path("find/<str:phone>", views.find, name="find"),
    path("findus/<str:phone>/<str:phons>", views.findus, name="findus"),
    path("cancel/<str:phone>/<str:phons>", views.cancel, name="cancel"),
    path("cancels/<str:phone>/<str:phons>", views.cancels, name="cancels"),
    path("accept/<str:phone>/<str:phons>", views.accept, name="accept"),
    path("remove_friend/<str:phone>/<str:phons>", views.remove_friend, name="remove_friend"),
    path("request/<str:phone>", views.request, name="request"),
    path("friends/<str:phone>", views.friends, name="friends"),
    path("profile/<str:phone>", views.profile, name="profile"),
    path("upload/<str:phone>", views.upload, name="upload"),
    path("log_in/", views.log_in, name="log_in"),
    path("lig/", views.lig, name="lig"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)