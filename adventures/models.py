# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Adventure(models.Model):
    name = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SummarySentence(models.Model):
    text = models.TextField(blank=False, null=False)
    adventure = models.OneToOneField(Adventure, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class SummaryParagraph(models.Model):
    text = models.TextField(blank=False, null=False)
    adventure = models.OneToOneField(Adventure, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class CharacterOutline(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=False, null=False)
    background = models.TextField(blank=False, null=False)
    personality = models.TextField(blank=False, null=False)
    motive = models.TextField(blank=False, null=False)
    conflict = models.TextField(blank=False, null=False)
    image_url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
