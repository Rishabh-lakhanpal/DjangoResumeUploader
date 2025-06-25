from django.shortcuts import render, HttpResponseRedirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.urls import reverse  # ✅ needed for redirect

class HomeViews(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})  # ✅ FIXED

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))  # ✅ FIXED redirect to home
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})  # return form with errors
