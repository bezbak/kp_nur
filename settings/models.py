# app/models.py
import uuid
from django.db import models
from django.urls import reverse


class PricePage(models.Model):
    title = models.CharField("Название страницы", max_length=200, default="Прайс")
    slug = models.SlugField("Уникальный URL", unique=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Страница цен"
        verbose_name_plural = "Страницы цен"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4().hex  # уникальный url
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("price_page_public", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.title} ({self.slug})"


# 1) Фото 1: 7 залов x (неделя/месяц) = 14 полей
class HallsWeekMonthPrices(models.Model):
    page = models.OneToOneField(PricePage, on_delete=models.CASCADE, related_name="halls_week_month")

    # Зал 1 (Mega)
    hall1_week = models.PositiveIntegerField("Зал 1 — неделя", default=0, help_text="Зал 1 (Mega): стоимость за НЕДЕЛЮ, сом")
    hall1_month = models.PositiveIntegerField("Зал 1 — месяц", default=0, help_text="Зал 1 (Mega): стоимость за МЕСЯЦ, сом")

    # Let’s Go
    hall2_week = models.PositiveIntegerField("Зал 2 — неделя", default=0, help_text="Let's Go: стоимость за НЕДЕЛЮ, сом")
    hall2_month = models.PositiveIntegerField("Зал 2 — месяц", default=0, help_text="Let's Go: стоимость за МЕСЯЦ, сом")

    # Малый зал 3
    hall3_week = models.PositiveIntegerField("Зал 3 — неделя", default=0, help_text="Малый зал (№3): стоимость за НЕДЕЛЮ, сом")
    hall3_month = models.PositiveIntegerField("Зал 3 — месяц", default=0, help_text="Малый зал (№3): стоимость за МЕСЯЦ, сом")

    # Малый зал 4
    hall4_week = models.PositiveIntegerField("Зал 4 — неделя", default=0, help_text="Малый зал (№4): стоимость за НЕДЕЛЮ, сом")
    hall4_month = models.PositiveIntegerField("Зал 4 — месяц", default=0, help_text="Малый зал (№4): стоимость за МЕСЯЦ, сом")

    # Малый зал 5
    hall5_week = models.PositiveIntegerField("Зал 5 — неделя", default=0, help_text="Малый зал (№5): стоимость за НЕДЕЛЮ, сом")
    hall5_month = models.PositiveIntegerField("Зал 5 — месяц", default=0, help_text="Малый зал (№5): стоимость за МЕСЯЦ, сом")

    # Малый зал 6
    hall6_week = models.PositiveIntegerField("Зал 6 — неделя", default=0, help_text="Малый зал (№6): стоимость за НЕДЕЛЮ, сом")
    hall6_month = models.PositiveIntegerField("Зал 6 — месяц", default=0, help_text="Малый зал (№6): стоимость за МЕСЯЦ, сом")

    # VIP зал 7
    hall7_week = models.PositiveIntegerField("Зал 7 — неделя", default=0, help_text="VIP зал: стоимость за НЕДЕЛЮ, сом")
    hall7_month = models.PositiveIntegerField("Зал 7 — месяц", default=0, help_text="VIP зал: стоимость за МЕСЯЦ, сом")

    class Meta:
        verbose_name = "Цены по залам (неделя/месяц)"
        verbose_name_plural = "Цены по залам (неделя/месяц)"

    def __str__(self):
        return "Залы: неделя/месяц"


# 2) Фото 2: 7 залов x (разовая стоимость) = 7 полей
class HallsSinglePrices(models.Model):
    page = models.OneToOneField(PricePage, on_delete=models.CASCADE, related_name="halls_single")

    hall1 = models.PositiveIntegerField("Зал 1", default=0, help_text="Зал 1 (Mega): разовая стоимость (сом)")
    hall2 = models.PositiveIntegerField("Зал 2", default=0, help_text="Let's Go: разовая стоимость (сом)")
    hall3 = models.PositiveIntegerField("Зал 3", default=0, help_text="Малый зал (№3): разовая стоимость (сом)")
    hall4 = models.PositiveIntegerField("Зал 4", default=0, help_text="Малый зал (№4): разовая стоимость (сом)")
    hall5 = models.PositiveIntegerField("Зал 5", default=0, help_text="Малый зал (№5): разовая стоимость (сом)")
    hall6 = models.PositiveIntegerField("Зал 6", default=0, help_text="Малый зал (№6): разовая стоимость (сом)")
    hall7 = models.PositiveIntegerField("Зал 7", default=0, help_text="VIP зал: разовая стоимость (сом)")

    class Meta:
        verbose_name = "Цены по залам (разовая)"
        verbose_name_plural = "Цены по залам (разовая)"

    def __str__(self):
        return "Залы: разовая стоимость"


# 3) Фото 3: билеты (2), дисконт (1), LED (3 строки x неделя/месяц = 6) => всего 9 полей
class PlacementAndLedPrices(models.Model):
    page = models.OneToOneField(PricePage, on_delete=models.CASCADE, related_name="placement_led")

    # Размещение на обратной стороне билета
    ticket_100k = models.PositiveIntegerField("Билеты 100 000", default=0, help_text="Размещение на обратной стороне билета: тираж 100 000 (сом)")
    ticket_500k = models.PositiveIntegerField("Билеты 500 000", default=0, help_text="Размещение на обратной стороне билета: тираж 500 000 (сом)")

    # Размещение на дисконтных картах
    discount_cards_5000 = models.PositiveIntegerField("Дисконтные карты 5 000", default=0, help_text="Размещение на дисконтных картах: 5 000 карт (сом)")

    # Реклама в фойе и на LED экранах
    led_cash_week = models.PositiveIntegerField("Касса (2 LED) — неделя", default=0, help_text="LED экраны: Касса — 2 LED экрана, цена за НЕДЕЛЮ (сом)")
    led_cash_month = models.PositiveIntegerField("Касса (2 LED) — месяц", default=0, help_text="LED экраны: Касса — 2 LED экрана, цена за МЕСЯЦ (сом)")

    led_bar_week = models.PositiveIntegerField("Кино Бар (2 LED) — неделя", default=0, help_text="LED экраны: Кино Бар — 2 LED экрана, цена за НЕДЕЛЮ (сом)")
    led_bar_month = models.PositiveIntegerField("Кино Бар (2 LED) — месяц", default=0, help_text="LED экраны: Кино Бар — 2 LED экрана, цена за МЕСЯЦ (сом)")

    led_inside_week = models.PositiveIntegerField("Внутри (5 LED) — неделя", default=0, help_text="LED экраны: Внутри кинотеатра — 5 LED экранов, цена за НЕДЕЛЮ (сом)")
    led_inside_month = models.PositiveIntegerField("Внутри (5 LED) — месяц", default=0, help_text="LED экраны: Внутри кинотеатра — 5 LED экранов, цена за МЕСЯЦ (сом)")

    class Meta:
        verbose_name = "Билеты/карты/LED цены"
        verbose_name_plural = "Билеты/карты/LED цены"

    def __str__(self):
        return "Билеты/карты/LED"


# 4) Фото 4: 3 прямоугольника (цена / месяц) = 3 поля
class BannerAreaMonthlyPrices(models.Model):
    page = models.OneToOneField(PricePage, on_delete=models.CASCADE, related_name="banner_areas")

    area_left_month = models.PositiveIntegerField("Левый баннер — месяц", default=0, help_text="Площадь 6м x 6.7м: стоимость за МЕСЯЦ (сом)")
    area_top_month = models.PositiveIntegerField("Верхний баннер — месяц", default=0, help_text="Площадь 5.5м x 4.3м: стоимость за МЕСЯЦ (сом)")
    area_bottom_month = models.PositiveIntegerField("Нижний баннер — месяц", default=0, help_text="Площадь 18м x 5.2м: стоимость за МЕСЯЦ (сом)")

    class Meta:
        verbose_name = "Цены по площади (месяц)"
        verbose_name_plural = "Цены по площади (месяц)"

    def __str__(self):
        return "Площади: месяц"
