from django.contrib import admin
from crowd_funding.models import *
admin.site.register(CustomUser)
admin.site.register(Contribution)
admin.site.register(Project)


