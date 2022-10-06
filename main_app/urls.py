from django.urls import path
from . import views


urlpatterns =[
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('sodas/', views.SodaList.as_view(), name='soda_list'),
    path('sodas/new/', views.SodaCreate.as_view(), name='sodas_create'),
    path('sodas/<int:pk>/update',views.SodaUpdate.as_view(), name="sodas_update"),
    path('sodas/<int:pk>/delete', views.SodaDelete.as_view(), name=
    'soda_delete')


]