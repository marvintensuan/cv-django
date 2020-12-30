from django.contrib import admin

# Register your models here.
from .models import CPD, SDL_OnlineCourse, SDL_Webinars

@admin.register(CPD)
class CPDAdmin(admin.ModelAdmin):
  pass

class SDL_OnlineCourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(SDL_OnlineCourse, SDL_OnlineCourseAdmin)

@admin.register(SDL_Webinars)
class SDL_WebinarsAdmin(admin.ModelAdmin):
    return {}