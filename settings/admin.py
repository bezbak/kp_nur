from django.contrib import admin
from django.utils.html import format_html

from .models import (
    PricePage,
    HallsWeekMonthPrices,
    HallsSinglePrices,
    PlacementAndLedPrices,
    BannerAreaMonthlyPrices,
)


class HallsWeekMonthPricesInline(admin.StackedInline):
    model = HallsWeekMonthPrices
    extra = 0
    max_num = 1
    can_delete = False


class HallsSinglePricesInline(admin.StackedInline):
    model = HallsSinglePrices
    extra = 0
    max_num = 1
    can_delete = False


class PlacementAndLedPricesInline(admin.StackedInline):
    model = PlacementAndLedPrices
    extra = 0
    max_num = 1
    can_delete = False


class BannerAreaMonthlyPricesInline(admin.StackedInline):
    model = BannerAreaMonthlyPrices
    extra = 0
    max_num = 1
    can_delete = False


@admin.register(PricePage)
class PricePageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "public_link")
    readonly_fields = ("slug", "public_link")

    inlines = [
        HallsWeekMonthPricesInline,
        HallsSinglePricesInline,
        PlacementAndLedPricesInline,
        BannerAreaMonthlyPricesInline,
    ]

    def public_link(self, obj: PricePage):
        if not obj.pk:
            return "Сохраните страницу, чтобы появился URL"
        url = obj.get_absolute_url()
        return format_html(
            '<div style="display:flex;gap:10px;align-items:center;">'
            '<a href="{0}" target="_blank">{0}</a>'
            '<input type="text" value="{0}" style="width:360px;" readonly '
            'onclick="this.select();document.execCommand(\'copy\');" />'
            '<small>клик по полю = копировать</small>'
            "</div>",
            url
        )
    public_link.short_description = "Публичная ссылка"

    # ❌ НЕ создаём OneToOne в save_model — иначе inline потом создаст второй
    # def save_model(...): pass

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        obj = form.instance
        # ✅ Создаём после сохранения inline’ов — тогда дубля не будет
        HallsWeekMonthPrices.objects.get_or_create(page=obj)
        HallsSinglePrices.objects.get_or_create(page=obj)
        PlacementAndLedPrices.objects.get_or_create(page=obj)
        BannerAreaMonthlyPrices.objects.get_or_create(page=obj)
