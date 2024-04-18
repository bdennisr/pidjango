from .models import Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



class RecipeListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Recipe
    context_object_name = 'recipe_list'
    template_name = 'recipes/index.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/recipe.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'].content = context['recipe'].content.split('\n')
        return context


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
  model = Recipe
  success_url = reverse_lazy('recipes-home')

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author


class RecipeCreateView(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['name', 'description', 'content']
  success_url = reverse_lazy('recipes-home')

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = ['name', 'description', 'content']

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    form.instance.author = str(self.request.user)
    return super().form_valid(form)
