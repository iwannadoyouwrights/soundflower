# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Petal(AbstractUser):
    subscriptions = models.ManyToManyField('MusicianProject', related_name='subscriptions_petals', blank=True)
    avatar = models.ImageField(upload_to='petal_avatar/', null=True, blank=True)
    second_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    birth_country = models.CharField(max_length=255, null=True, blank=True)
    birth_city = models.CharField(max_length=255, null=True, blank=True)
    country_of_residence = models.CharField(max_length=255, null=True, blank=True)
    city_of_residence = models.CharField(max_length=255, null=True, blank=True)


class MusicianProject(models.Model):
    creator_project = models.ForeignKey(Petal, related_name='mu')
    avatar = models.ImageField(upload_to='musician_project_avatar/', null=True, blank=True)
    name = models.CharField(max_length=255)
    create_date = models.DateField(null=True, blank=True)
    city_from_created = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class News(models.Model):
    project = models.ForeignKey(MusicianProject, null=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    create_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "%s: %s" % (self.title, self.content)


class Role(models.Model):
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name


class Musician(models.Model):
    project = models.ForeignKey(MusicianProject)
    petal = models.ForeignKey(Petal, null=True, blank=True)
    avatar = models.ImageField(upload_to='musician_avatar/', null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.ForeignKey(Role)

    def __str__(self):
        return "%s %s-%s in %s" % (self.first_name, self.last_name, self.role, self.project)


class MusicAlbum(models.Model):
    image_dir = 'music_albums_images/'

    artist = models.ForeignKey(MusicianProject)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_dir, null=True, blank=True,
                              default=image_dir+'default.jpg')
    date = models.DateTimeField(auto_now_add=True)


class Song(models.Model):
    album = models.ForeignKey(MusicAlbum)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='songs/')


