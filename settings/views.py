from django.shortcuts import get_object_or_404, render
from .models import PricePage

# Create your views here.


def index(request):
    return render(request, 'index.html')


def price_page_public(request, slug):
    page = get_object_or_404(PricePage, slug=slug)
    ctx = {
        "page": page,
        "hwm": page.halls_week_month,
        "hs": page.halls_single,
        "pl": page.placement_led,
        "ba": page.banner_areas,
    }
    print(ctx)
    return render(request, "index.html", context=ctx)
