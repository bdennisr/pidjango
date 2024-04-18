from django.urls import path

from . import views

urlpatterns = [
    path('', views.GraphListView.as_view(), name='index'),
    path('<int:pk>', views.GraphDetailView.as_view(), name='graph_detail'),
]