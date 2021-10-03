
from django.shortcuts import render


def administrator_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role != "Administrator":

            return render(request, "access-denied.html")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
