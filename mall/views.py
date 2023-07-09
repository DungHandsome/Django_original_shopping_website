from django.shortcuts import render

# Create your views here.
def mall(request):
    return render(request, 'mall/mall.html')