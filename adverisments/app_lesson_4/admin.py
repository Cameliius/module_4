from django.contrib import admin
from .models import Adverisments


# Register your models here.

class AdverismentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'auction', 'created_date', 'update_date', 'user', 'photo']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'user', 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)


admin.site.register(Adverisments, AdverismentsAdmin)
