from django.shortcuts import render, redirect
from loginpage.models import Note
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def accounts(request):
	return render(request, "accounts.html", {})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home/")
    return redirect('/accounts?error=True')
	
	# render(request, 'accounts.html', {})

def logout_view(request):
    logout(request)
    return redirect("/login/")



def signup_view(request):
	print(request.POST['username'], request.POST['password'], request.POST['email'])
	user = User.objects.create_user(
		username=request.POST['username'], 
		password=request.POST['password'],
		email = request.POST['email'])
	login(request, user)
	return redirect('/home/')


