from django.http import response
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
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
    "december": None,

}


def index(request):

    months = list(monthly_challenges.keys())

    return render(request, "challenge_app\index.html", context={"months": months})


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

    # return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        # Render always use to render success response
        return render(request, "challenge_app\challenge.html",
                      context={"text": challenge_text,
                               "month": month})

    # response_data = render_to_string("challenge_app\challenge.html")
    # response_data = f'<h1>{challenge_text}</h1>'
    # return HttpResponse(response_data)
    except:
        # not_found_page = render_to_string("404.html")
        # return HttpResponseNotFound(not_found_page)
        # Instead of above approach Django provides us
        # inbuilt functionality to raise 404 error
        raise Http404
