from django.shortcuts import render

# Create your views here.


def method(request):
    return render(request, 'product/index.html')
