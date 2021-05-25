from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Todo, Category

# Create your views here.
def homepage(request):
    todos = Todo.objects.all()
    categories = Category.objects.all()
    return render(request, 'main/home.html', {'todos': todos, 'categories': categories})

# same purpose as homepage, but for consumption by other apps/computers
def list_todos_json(request):
    todos = Todo.objects.all()
    todos_json = serialize("json", todos, fields=('text', 'user'))
    return HttpResponse(todos_json, content_type="application/json")

@login_required
def user_detail(request):
    todos = Todo.objects.filter(user=request.user, done=False)
    return render(request, 'main/mytodos.html', {'todos': todos})

def todos_by_user_json(request):
    todos = Todo.objects.filter(user=request.user, done=False)
    todos_json = serialize("json", todos, fields=('text', 'done'))
    return HttpResponse(todos_json, content_type="application/json")


# TODO make a view that is called by new URL that lists user's Todos
def category_detail(request, pk):
    category = get_object_or_404(Category)
    return render(request, 'main/category_detail.html', {'category': category})


