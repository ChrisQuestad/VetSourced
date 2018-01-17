from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import logout
from .forms import EmployerForm, UpdateProfileForm
from .models import User, EmployerProfile
from jobs.models import Job
from .permissions import employer_login_required


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'industry', 'current_job', 'bio', 'desired_industry', 'desired_job')

class EmployerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class LogoutView(View):
    template_name = 'layout.html'
    def logout_view(request):
        logout(request)

        return redirect('jobs:browse')




class UserRegisterView(View):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            model = form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('jobs:browse')
        else:
            return render(request, self.template_name, {'form':form})

class EmployerRegisterView(View):
    template_name = 'registration/employer-register.html'
    form_class = EmployerForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {
            'form':form,
            'form2': EmployerCreationForm()
        })

    def post(self, request, *args, **kwargs):
        user_creation_form = EmployerCreationForm(request.POST)
        employer_profile_form = self.form_class(request.POST)
        if user_creation_form.is_valid() and employer_profile_form.is_valid():
            _user = user_creation_form.save(commit=False)
            employer_profile = employer_profile_form.save()
            _user.employer = employer_profile
            _user.is_employer = True
            _user.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'],
                                password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('jobs:browse')
        else:
            return render(request, self.template_name, {
                'form':employer_profile_form,
                'form2':user_creation_form
                })


class ProfileView(View):
    template_name = 'registration/profile.html'
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        return render(request, self.template_name, {'user': user})


class UpdateProfileView(View):
    template_name = 'registration/update.html'
    form_class = UpdateProfileForm

    def get(self, request, *args, **kwargs):
        user_creation_form = UpdateProfileForm(instance=request.user)
        return render(request, self.template_name, { 'user_form':user_creation_form })

    def post(self, request, *args, **kwargs):
        user_creation_form = UpdateProfileForm(request.POST, instance=request.user)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('accounts:profile', username=request.user.username)
        else:
            return render(request, self.template_name, { 'user_form':user_creation_form })


class UpdateEmployerView(View):
    template_name = 'registration/employer-update.html'
    form_class = EmployerForm

    def get(self, request, *args, **kwargs):
        employer_profile_form = self.form_class(instance=request.user.employer)
        return render(request, self.template_name, { 'employer_form': employer_profile_form })

    def post(self, request, *args, **kwargs):
        employer_profile_form = self.form_class(request.POST, instance=request.user.employer)
        if request.user.is_employer and employer_profile_form.is_valid():
            employer_profile_form.save()
            return redirect('accounts:profile', username=request.user.username)
        else:
            return render(request, self.template_name, { 'employer_form': employer_profile_form })


class EmployerJobsView(View):
    template_name = 'registration/employer-jobs.html'

    def get(self, request, *args, **kwargs):
        jobs = request.user.jobs.all()
        return render(request, self.template_name, {'jobs': jobs})
