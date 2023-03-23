import json
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . models import Todo
from django.db.models import Q
from django.contrib import messages

# List of Todos
# todos = [
#     {"id": 1, "name":"Morning Prayers"},
#     {"id": 2, "name":"Breakfast"},
#     {"id": 3, "name":"Gym Workout"},
#     {"id": 5, "name":"Start writing Code"},
#     {"id": 6, "name":"Start writing Programming"},
#     {"id": 7, "name":"Start Eating lauch"},
#     {"id": 8, "name":"Start Driving Manual Car Lessons"},
#     {"id": 9, "name":"Heading for Football exercises on the field"},
#     {"id": 10, "name":"Play some playstation video games"},
#     {"id": 11, "name":"Time to sleep"},
# ]

# Create your views here.
def homePage(request):
    # filter through the todos....
    query = request.GET.get("search") if request.GET.get("search") != None else ""
    todos = Todo.objects.filter(Q(item__icontains = query))
    # get all the todo items from the Database;
    # todos = Todo.objects.all()
    # get the form
    form = UserCreationForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username).lower()
        except:
            messages.error(request, 'User Doesnot Exist....')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.warning(request, 'Username or Password Doesnot Exist..')
        
        form = UserCreationForm(request.POST)
        # users = UserDetail()
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("index")
        
        if "name" in request.POST and request.user:
            item = request.POST.get('name')
            if not item == "":
                msg = "success" 
                json.dumps(msg)
                # user_details = UserDetail.objects.get()
                if request.user.is_authenticated:
                    user_id = request.user
                    print(user_id)
                    todo = Todo.objects.create(
                        host = user_id,
                        item = item,
                    )
                    todo.save()
                    return JsonResponse(msg, safe=False)
            else:
                msg = "No todo item entered"
                return JsonResponse(msg, safe=False)
    if request.method == "GET":
        deleted = request.GET.get("delete")
        if deleted:
            todo_item = Todo.objects.filter(id = deleted)
            # print(todo_item.delete())
            for item in todo_item:
                print(item)
                item.delete()
                return JsonResponse(json.dumps({"msg": "deleted..."}), safe=False)
    context = {"names": todos, "form": form}
    return render(request, 'base/index.html', context)

def logoutUser(request):
    logout(request)
    return redirect("index")

