from django.contrib import admin
from .models import Place, FeedBack


admin.site.register(Place)

class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'text', 'user', 'checked'] # отображение на экране
    list_editable = ['checked'] # галочка проверен
    list_filter = ['checked'] # фильтр
    search_fields = ['text', 'place__name', 'place__location', 'place__description']  # поисковик по строкам

    fields = ['user', 'place', 'text'] # поля на карточке
    readonly_fields = ['place', 'text'] # разрешено только читать


admin.site.register(FeedBack, FeedBackAdmin)
