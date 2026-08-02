from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..services.dashboard import get_dashboard_data


@login_required
def dashboard_view(request):

    context = get_dashboard_data(request.user)

    return render(
        request,
        "expenses/dashboard/dashboard.html",
        context,
    )