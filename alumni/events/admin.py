from django.contrib import admin
from .models import Events

class EventsAdmin(admin.ModelAdmin):
    model = Events
    filter_horizontal = ('tags',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "tags":
            kwargs["queryset"] = db_field.related_model.objects.order_by('name')
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Events, EventsAdmin)
