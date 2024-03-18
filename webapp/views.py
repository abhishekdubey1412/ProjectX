from webapp.models import Records
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login_user')

    context = {'form': form}
    return render(request, 'register.html', context=context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'user_login.html', context=context)

def logout_user(request):
    logout(request)
    messages.success(request, "Successful Signout.")
    return redirect('login_user')

@login_required(login_url='login_user/')
def dashboard(request):
    user_records = Records.objects.all()
    context = {'records': user_records}
    return render(request, 'dashboard.html', context=context)

@login_required(login_url='login_user/')
def create_record(request):
    form = AddRecordForm()

    if request.method == 'POST':
        form = AddRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'create_record.html', context=context)

@login_required(login_url='login_user/')
def update_record(request, pk):
    record = Records.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, "Successful Record Updated.")
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'update_record.html', context=context)

@login_required(login_url='login_user/')
def delete_record(request, pk):
    delete_record = Records.objects.get(id=pk)
    delete_record.delete()
    return redirect('dashboard')

@login_required(login_url='login_user/')
def singular_record(request, pk):
    single_record = Records.objects.get(id=pk)
    context = {'record': single_record}
    return render(request, 'view-record.html', context=context)