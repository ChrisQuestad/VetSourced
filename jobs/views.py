from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.detail import DetailView
from .models import Job
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from .forms import CreateJobForm
from django.utils import timezone
from accounts.permissions import employer_login_required



class HomeView(View):
    template_name = 'jobs/home.html'
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()

        return render(request, self.template_name, {'jobs': jobs})




class BrowseView(View):
    template_name = 'jobs/browse.html'
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()

        return render(request, self.template_name, {'jobs': jobs})




class BrowseDetailView(DetailView):
    template_name = 'jobs/detail.html'
    def get(self, request, *args, **kwargs):
        job = get_object_or_404(Job, pk=self.kwargs['pk'])

        return render(request, self.template_name, {'job': job, 'now': timezone.now()})



class JobSearchView(DetailView):
    template_name = 'jobs/search.html'
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        jobs = Job.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(company__icontains=query) |
            Q(location__icontains=query) |
            Q(experience_required__icontains=query)
        )
        return render(request, self.template_name, {'query': query, 'jobs': jobs})

@method_decorator(employer_login_required, name='dispatch')
class CreateJobView(View):
    template_name = 'jobs/create-job.html'
    form_class = CreateJobForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.employer = request.user
            model.save()
            return redirect('jobs:browse')

        else:
            return render(request, self.template_name, {'form': form})


@method_decorator(employer_login_required, name='dispatch')
class DeleteJobView(View):
    def get(self, request, *args, **kwargs):
        model = Job.objects.get(pk=self.kwargs['pk'])
        if model.employer == request.user:
            model.delete()
            return redirect('accounts:employer-jobs')
        else:
            return HttpResponse(status=402)
