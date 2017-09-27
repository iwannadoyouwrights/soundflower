from django.contrib import admin
from .models import *


class InlineMusician(admin.TabularInline):
    model = Musician


class InlineNews(admin.TabularInline):
    model = News


@admin.register(MusicianProject)
class MusicianProjectAdmin(admin.ModelAdmin):
    inlines = [InlineMusician, InlineNews]


@admin.register(Petal)
class PetalAdmin(admin.ModelAdmin):
    inlines = [InlineMusician]


admin.site.register(Role)
admin.site.register(Musician)
admin.site.register(News)
admin.site.register(MusicAlbum)
admin.site.register(Song)
