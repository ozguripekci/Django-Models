from django.contrib import admin
from relations.models import Creator, Language, Frameworks, Developers

# Register your models here.

admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Frameworks)
admin.site.register(Developers)