from django.shortcuts import render, redirect

# Create your views here.
def get_home(request):
    return render(request, 'home/home.html')

def loginPage(request)
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else: messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'home/login.html', context)