from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day.",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day.",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day.",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monnth_handler_by_number(request, month):
    
    months = list(monthly_challenges.keys())

    if month < 1 or month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def month_handler(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html", {
            "month": month,
            "challenge": challenge_text
        })
    except KeyError:
        raise Http404()