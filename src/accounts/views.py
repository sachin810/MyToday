from django.shortcuts import render,redirect,reverse,HttpResponseRedirect,get_object_or_404
from .forms import RegistrationForm,LoginForm,UpdateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from diary.models import Diary
from django.core.paginator import Paginator

User = get_user_model()



def RegisterView(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('diary:index')
    else:
        return render(request, 'home.html',{'form':form})

    return render(request, 'home.html',{'form':form})


def LogoutView(request):
    logout(request)
    return redirect('accounts:index')


def LoginView(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password = password)
        login(request,user)
        return redirect('diary:index')
    else:
        return render(request,'login.html',{'form':form})

    return render(request,'login.html',{'form':form})


def AccountUpdateView(request):
    queryset = Diary.objects.filter(user=request.user)
    profile = get_object_or_404(User, pk=request.user.pk)
    form = UpdateForm(request.POST or None,instance=request.user)
    #sidebar list view
    queryset = Diary.objects.filter(user=request.user)
    #pagination
    paginator = Paginator(queryset, 8)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    #end pagination
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        new_password = form.cleaned_data.get('new_password')
        user.set_password(new_password)
        user.save()
        user = authenticate(username=username, new_password=new_password)
        login(request,user)
        return redirect('accounts:profile')
    return render(request,'profile.html',{"contacts":contacts,'form':form, 'profile':profile})
