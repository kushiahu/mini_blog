from django.urls import path

from posts import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.AddPostView.as_view(), name='create'),
    path('editar/<int:id>/', views.UpdatePostView.as_view(), name='update'),
    path('eliminar/<int:id>/', views.DeletePostView.as_view(), name='delete'),
    path('detalle/<int:id>/', views.DetailPostView.as_view(), name='detail'),
    path('search/', views.SearhView.as_view(), name='search'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]