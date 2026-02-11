from .models import Advertisement
from django.utils import timezone


def ads_processor(request):
    """Context processor to add active advertisements to all templates"""
    active_ads = Advertisement.objects.filter(
        is_active=True,
        start_date__lte=timezone.now(),
        end_date__gte=timezone.now()
    )
    return {'active_ads': active_ads}