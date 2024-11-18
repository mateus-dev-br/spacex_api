from django.shortcuts import render
from .services import fetch_spacex_launches
from django.http import JsonResponse

# Create your views here.

def home(request):
    data = fetch_spacex_launches()

    if "error" in data:
        return render(request, "home.html", {"error": data["error"]})
    
    success_launches = list(filter(lambda x: x["success"] and not x["upcoming"], data))
    failed_launches = list(filter(lambda x: not x["success"] and not x["upcoming"], data)) 
    upcoming_launches = list(filter(lambda x: x["upcoming"], data))

    return render(request, "home.html", {
    "success_launches": success_launches,
    "failed_launches": failed_launches,
    "upcoming_launches": upcoming_launches
})