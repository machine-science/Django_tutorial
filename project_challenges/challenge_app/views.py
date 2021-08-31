from django.http import response
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "january challenge",
    "february": "february challenge",
    "march": "march challenge",
    "april": "april challenge",
    "may": "may challenge",
    "june": "june challenge",
    "july": "july challenge",
    "august": "august challenge",
    "september": "september challenge",
    "october": "october challenge",
    "november": "november challenge",
    "december": "december challenge",

}


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capital_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href = \"{month_path}\">{capital_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month-1]
    # We use reverse to make use of path name to make urls more dynamic
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    # with use of reverse, we don't need to change '/challenges/' in path
    # It will be taken care of automatically by reverse.
    # return HttpResponseRedirect("/challenges/"+redirect_month)

    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenge_app\challenge_app.html")
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1> This month is not supported!! </h1>")
