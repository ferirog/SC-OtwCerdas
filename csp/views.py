from django.shortcuts import render

# Create your views here.
def csp(request):
    return render(request, 'tescsp.html')