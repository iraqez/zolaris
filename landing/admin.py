from django.contrib import admin

from landing.models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ["name", ]
    search_fields = ["email", ]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
