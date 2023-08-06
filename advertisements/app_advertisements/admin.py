from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date',  'auction', 'image']

    list_filter = ['auction', 'created_at']

    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        (
            'Общее', {
                'fields': ('title', 'description', 'image')
            }
        ),
        (
            'Финансы', {
                'fields': ('price', 'auction'),
                'classes': ['collapse']
            }
        ),
    )

    @admin.action(description="Убрать возможнсть торга")
    def make_auction_as_false(self, request,  queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможнсть торга")
    def make_auction_as_true(self, request,  queryset):
        queryset.update(auction=True)
admin.site.register(Advertisement, AdvertisementAdmin)