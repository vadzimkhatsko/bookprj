from django.shortcuts import render, HttpResponse
from ajaxapp.models import Video


def hello(request):
    responce = {'video': Video.objects.all()}
    return render(request, "index.html", responce)


def adding_like(request):
    print(request.GET)
    video = Video.objects.get(id=request.GET["id"])
    video.likes += 1
    video.save()
    return HttpResponse(video.likes)

