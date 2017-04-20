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
    description = models.TextField(blank=False, null=False)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class SummaryParagraph(models.Model):
    description = models.TextField(blank=False, null=False)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
