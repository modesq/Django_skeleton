from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Character


class CharacterListView(ListView):
    template_name = "characters/characters-list.html"
    model = Character


class CharacterDetailView(DetailView):
    template_name = "characters/characters-detail.html"
    model = Character


class CharacterCreateView(CreateView):
    template_name = "characters/characters-create.html"
    model = Character
    fields = ['name', 'description']


class CharacterUpdateView(UpdateView):
    template_name = "characters/characters-update.html"
    model = Character
    fields = ['name', 'description']


class CharacterDeleteView(DeleteView):
    template_name = "characters/characters-delete.html"
    model = Character
    success_url = reverse_lazy("characters-list")