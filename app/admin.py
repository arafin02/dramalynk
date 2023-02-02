from django.contrib import admin
from .models import Drama, Episode, Genre, Origin

# Register your models here.


class DramaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class EpisodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"ep_slug": ('drama', 'ep_no')}


admin.site.register(Drama, DramaAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Genre)
admin.site.register(Origin)
