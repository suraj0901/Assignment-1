from django.http import HttpResponse


def homepage(request):
    print("homepage")
    return HttpResponse("this is home page")
