from django.urls import path
from .views import (
    EvenementListView,
    EvenementDetailView,
    EvenementCreateView,
    EvenementUpdateView,
    EvenementDeleteView,
)

urlpatterns = [
    path('', EvenementListView.as_view(), name='evenement_list'),
    path('<int:pk>/', EvenementDetailView.as_view(), name='evenement_detail'),
    path('ajouter/', EvenementCreateView.as_view(), name='evenement_create'),
    path('<int:pk>/modifier/', EvenementUpdateView.as_view(), name='evenement_update'),
    path('<int:pk>/supprimer/', EvenementDeleteView.as_view(), name='evenement_delete'),
]
