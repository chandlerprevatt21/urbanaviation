from django.shortcuts import render

def home(request):
    context = {
        'title': 'Urban Aviation Group',
    }
    return render(request, 'home.html', context)
