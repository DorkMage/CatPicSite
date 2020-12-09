from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils.safestring import mark_safe
from .models import Pic
from .models import Filter
from random import randint
import json


class Clowder:
    whitelist = []
    blacklist = []

    def neutralize(self, cat):
        for i in self.blacklist:
            if i == cat:
                self.blacklist.remove(i)
        for i in self.whitelist:
            if i == cat:
                self.whitelist.remove(i)

    def add_to_whitelist(self, cat):
        self.neutralize(cat)
        self.whitelist.append(cat)

    def add_to_blacklist(self, cat):
        self.neutralize(cat)
        self.blacklist.append(cat)


def index(request):
    clowder = dict()
    catpics = Pic.objects.all()
    for i, pic in enumerate(catpics):
        url = pic.pic_url.url
        cats = pic.pic_cats
        clowder[i] = ([url, [cats]])
    filters = Filter.objects.all()
    template = loader.get_template('catpic/index.html')
    try:
        catpic = catpics[randint(0, len(catpics) - 1)]
    except:
        catpic = None
    #catpic = None
    context = {
        'filters': filters,
        'catpic': catpic,
        'clowder': mark_safe(json.dumps(clowder))
    }
    return HttpResponse(template.render(context, request))
