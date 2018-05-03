from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,reverse,redirect
from .models import Diary
from .forms import DiaryCreateForm
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from  django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


User = get_user_model()


@login_required
def DiaryListView(request):
    if request.user.is_authenticated:
        queryset = Diary.objects.filter(user=request.user)
        paginator = Paginator(queryset, 8)#shows 10 item per page
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        form = DiaryCreateForm(request.POST or None)
        query = request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
            ).distinct()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'successfully created the Diary')
            return HttpResponseRedirect(instance.get_absolute_url())

        return render(request,'list.html', {"form":form,'contacts': contacts})

@login_required
def DiaryDetailView(request,slug):
    instance = get_object_or_404(Diary, slug=slug, user=request.user)
    #for sidebar listview
    queryset = Diary.objects.filter(user=request.user)
    #pagination
    paginator = Paginator(queryset, 8)#shows 10 item per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'detail.html',{"contacts":contacts ,"instance":instance})


@login_required
def DiaryDeleteView(request,pk):
    instance = Diary.objects.filter(pk=pk)
    instance.delete()
    messages.success(request, 'successfully Deleted the Diary')
    return redirect('diary:index')

@login_required
def DiaryUpdateView(request,pk):
    instance = get_object_or_404(Diary, pk=pk, user=request.user)
    #for sidebar listview
    queryset = Diary.objects.filter(user=request.user)
    #pagination
    paginator = Paginator(queryset, 8)#shows 10 item per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    #end
    form = DiaryCreateForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'successfully updated the Diary')
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, 'edit.html',{"contacts":contacts,"instance":instance,"form":form})

