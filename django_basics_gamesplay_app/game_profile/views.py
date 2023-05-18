from django.shortcuts import render

# Create your views here.

def create_profile(request):
    context = {}
    return render(request=request, template_name='create-profile.html', context=context)