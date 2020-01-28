


# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.views.generic import View


class DeepThoughtView(View):

    def get(self, request):
        return HttpResponse(42)
