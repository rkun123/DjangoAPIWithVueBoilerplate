import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import *

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class ListTodos(TemplateView):
    # GET
    def get(self, req):
        # List todos
        rawTodos = Todo.objects.values()
        todos = []
        for t in rawTodos:
            todos.append(t)
        todos.append

        data = {
            'payload': todos
        }
        return JsonResponse(data=data)

    # POST
    def post(self, req):
        # Make todo
        rawTodo = json.loads(req.body)
        print(rawTodo)
        todo = Todo(name=rawTodo["name"], description=rawTodo["description"])

        todo.save()
        return JsonResponse(data={'id': todo.pk})

