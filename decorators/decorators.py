from django.http import HttpResponse


def administrator_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role != "Administrator":
            return HttpResponse("You are not authorized to see this page")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
