from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Brend, Car

admin.site.register(Brend)

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_photo', 'created', 'motorhp', 'motorl', 'views', 'price','brend')
    list_display_links = ('id', 'name')
    list_editable = ('brend',)
    list_filter = ('brend',)
    search_fields = ('name',)
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = False
    save_on_top = False
    readonly_fields = ('views',)

    def get_photo(self, car):
        if car.photo:
            return mark_safe(f'<img src="{car.photo.url}" width="150px">')
        return "-"

    get_photo.short_description = 'Rasm'

admin.site.register(Car, CarAdmin)