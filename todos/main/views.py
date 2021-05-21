from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Todo, Category

# Create your views here.
def homepage(request):
    todos = Todo.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/home.html', {'todos': todos, 'categories': categories})

@login_required
def user_detail(request):
    todos = Todo.objects.filter(user=request.user, done=False)
    return render(request, 'main/mytodos.html', {'todos': todos})

# TODO make a view that is called by new URL that lists user's Todos
def category_detail(request, pk):
    category = get_object_or_404(Category)
    return render(request, 'main/category_detail.html', {'category': category})
