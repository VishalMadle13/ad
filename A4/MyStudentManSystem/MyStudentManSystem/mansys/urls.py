
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path("register/",views.registerfaculty,name="registerfaculty"),
    path("regstu/",views.registerstudent,name="registerstudent"),
    path("login/",views.login,name="login"),
    # path("course/",views.course,name="course"),
    # path("course1/",views.course1,name="course1")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)