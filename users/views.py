from django.shortcuts import redirect, render

from users.forms import UserSignUpForm
from django.views import View


class UserSignUpView(View):
    def get(self, request, *args, **kwargs):
        form = UserSignUpForm()
        return render(request, "registration/sign-up.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()

            return redirect("/auth/login")
        else:
            return render(request, "registration/sign-up.html", {"form": form})
