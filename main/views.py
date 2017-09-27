from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic.base import View
from .models import *
import json


def index(request):
    all_petals = Petal.objects.all()
    context = {'all_petals': all_petals}
    return render(request, 'main/index.html', context)


def petal(request, petal_id):
    petal = get_object_or_404(Petal, id=petal_id)
    news = News.objects.filter(
        project__subscriptions_petals__id=petal_id).order_by('-create_date')
    context = {'petal': petal,
               'news': news}
    return render(request, 'main/user_profile.html', context)


class MusicianProjectView(View):
    def get(self, request, project_id):
        project = MusicianProject.objects.get(id=project_id)
        if project.subscriptions_petals.filter(id=request.user.id).exists():
            subs = 'Unsubscribe'
        else:
            subs = 'Subscribe'
        context = {'Musician_project': project,
                   'subs': subs}
        return render(request, 'main/musician_profile.html', context)

    def post(self, request, project_id):
        project = MusicianProject.objects.get(id=project_id)
        if request.is_ajax():
            if project.subscriptions_petals.filter(id=request.user.id).exists():
                Petal.objects.get(
                    id=request.user.id).subscriptions.remove(project)
                sub_users = [
                    i.first_name for i in project.subscriptions_petals.all()]
                context_ajax = {'subs': 'Subscribe',
                                'sub_users': sub_users}
            else:
                Petal.objects.get(
                    id=request.user.id).subscriptions.add(project)
                sub_users = [
                    i.first_name for i in project.subscriptions_petals.all()]
                context_ajax = {'subs': 'Unsubscribe',
                                'sub_users': sub_users}
        return HttpResponse(json.dumps(context_ajax), content_type='application/json')


class Album(View):
    def get(self, request, project_id, album_id):
        album = MusicianProject.objects.get(
            id=project_id).musicalbum_set.get(id=album_id)
        context = {'album': album}
        return render(request, 'main/album.html', context)
