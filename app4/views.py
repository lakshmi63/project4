from django.shortcuts import render

# Create your views here.
def maccha(request):
    return render(request,'maccha.html')