from django.views import generic
from .models import Graph
from django.contrib.auth.mixins import LoginRequiredMixin


class GraphListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Graph
    context_object_name = 'graph_list'   # your own name for the list as a template variable
    template_name = 'graphs/index.html'  # Specify your own template name/location


class GraphDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Graph
    context_object_name = 'graph'   # your own name for the list as a template variable
    template_name = 'graphs/graph.html'  # Specify your own template name/location
