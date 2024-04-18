from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {
        'sidebar' : {
            'graphs': {
                'title': 'Graphs',
                'link': 'graphs'
            },
            'recipes': {
                'title': 'recipes',
                'link': 'recipes'
            }
        }
    }
    return render(request, 'main/index.html', context)
