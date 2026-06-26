# -*- coding: utf-8 -*-
# dcrm/website/admin.py

from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import Record

# Register your models here.
admin.site.register(Record)
