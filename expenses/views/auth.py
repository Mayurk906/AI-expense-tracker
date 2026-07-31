from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from ..forms.auth import LoginForm, RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Account created successfully. Please login."
            )

            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "expenses/auth/register.html",
        {"form": form},
    )


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())

            messages.success(
                request,
                f"Welcome {request.user.username}!"
            )

            return redirect("dashboard")

    else:
        form = LoginForm()

    return render(
        request,
        "expenses/auth/login.html",
        {"form": form},
    )


def logout_view(request):
    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect("login")