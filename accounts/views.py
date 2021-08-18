from django.shortcuts import redirect, render
from .models import Post
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        post = Post()
        post.email = request.POST.get('email')
        post.password = request.POST.get('psw')

        if Post.objects.filter(email=post.email).exists() and Post.objects.filter(password=post.password).exists():
            return render(request,"Hello.html")
            
        else:
            messages.info(request,"Invalid credentials, Please sign up and then login")
            return redirect('login')

    else:    
        return render(request,"login.html")
        print("Matched")

def index(request):
    if request.method == 'POST':
        post = Post()
        post.username = request.POST.get('username')
        post.email = request.POST.get('email')
        post.password = request.POST.get('psw')
        password1 = request.POST.get("psw-repeat")
        post.address = request.POST.get('address')

        if password1 == post.password:
            if Post.objects.filter(email=post.email).exists():
                messages.info(request,'User already has account')
                return redirect('index')
                
            if Post.objects.filter(password=post.password).exists():
                messages.info(request,'User already has account')
                return redirect('index')
            else:
                post.save()
                messages.info(request,'User account created')
                return redirect('index')
        else:
             messages.info(request,'Password does not match with confirm password, please type correctly')
             return redirect('index') 
             
        return redirect('/')

    else:
        return render(request,"index.html")


def retrieve_data(request):
    event_list = Post.objects.all()
    return render(request, 'database_data.html',{'event_list':event_list})    

def delete(request,id):
    event_list = Post.objects.get(id=id)
    event_list.delete()
    return redirect("/event")
