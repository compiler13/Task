# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (Language, Application, Website,
                     Product, Contact, Profession
                     )

# Register your models here.

admin.site.register(Language, Application, Website,
                    Product, Contact, Profession
                    )
