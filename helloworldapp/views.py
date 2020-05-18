from django.shortcuts import render

# Create your views here.
# 追加


def helloworldfunction(request):
    return render(request, 'index.html')
