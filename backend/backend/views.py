from django.shortcuts import redirect

def redirect_view(request):
    response = redirect("http://localhost:8080/")
    return response
