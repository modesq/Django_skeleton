from django.urls import path
from .views import CharacterListView, CharacterDetailView, CharacterCreateView, CharacterUpdateView, CharacterDeleteView

urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='characters-list'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='characters-detail'),
    path('characters/create/',CharacterCreateView.as_view(), name='characters-create'),
    path('characters/<int:pk>/update/', CharacterUpdateView.as_view(), name='characters-update'),
    path('characters/<int:pk>/delete/', CharacterDeleteView.as_view(), name='characters-delete'),
]