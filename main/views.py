from django.shortcuts import render
from main import models
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/auth/login')
def index(request):
    colleges = models.College.objects.all()
    context = {
        "colleges":colleges
    }
    return render(request, 'index.html', context)


class Index(ListView):
    model = models.College
    template_name = 'index.html'
    context_object_name = 'colleges'

def collegeDetail(request, pk):
    colleges = models.College.objects.get(pk = pk)
    context = {
        "colleges":colleges
    }
    return render(request, 'collegeDetail.html', context)

class CollegeDetail(DetailView):
    model = models.College
    template_name = 'collegeDetail.html'
    context_object_name = 'colleges'

class CollegeCreate(CreateView):
    model = models.College
    template_name = 'createCollege.html'
    fields = '__all__'
    success_url = '/'

class CollegeUpdate(UpdateView):
    model = models.College
    template_name = 'createCollege.html'
    fields = '__all__'
    success_url = '/'

class CollegeDelete(DeleteView):
    model = models.College
    template_name = 'collge_delete.html'
    success_url = '/'