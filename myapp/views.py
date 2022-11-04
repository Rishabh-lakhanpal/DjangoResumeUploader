from django.shortcuts import render, HttpResponseRedirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.

class HomeViews(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'candidates':'candidates', 'form':form})
    
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('myapp/home.html')
            # return render(request, 'myapp/home.html', {'form':'form'})

