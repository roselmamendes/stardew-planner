from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:fazenda_id>/", views.get_fazenda, name="get_fazenda"),
    path("<int:fazenda_id>/materiais/", views.get_materiais, name="get_materiais")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)