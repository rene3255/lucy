from django.shortcuts import render


# Create your views here.
def chat(request):
    return render(request, "lucyschat/chat.html")
