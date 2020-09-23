import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import Todo

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

@method_decorator(csrf_exempt, name='dispatch')
class Todos(TemplateView):
    def get(self, req, todo_id):
        todo = Todo.objects.filter(pk=todo_id).values()
        print(json.dumps(todo[0]))
        return JsonResponse(todo[0])

    def delete(self, req, todo_id):
        todo = Todo.objects.filter(pk=todo_id)
        todo.delete()
        return HttpResponse(200)