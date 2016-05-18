
from django import template
from datetime import timedelta
from django.utils.timesince import timesince
from django.utils import timezone

register = template.Library()

@register.filter(name='timeago')
def timeago(value):
    now = timezone.now()
    try:
        difference = now - value
    except:
        return value

    if difference < timedelta(minutes=1):
        return 'less then minute ago'
    if timedelta(minutes=1) <= difference < timedelta(minutes=2):
        return 'about a minute ago'
    if timedelta(hours=1) <= difference < timedelta(hours=2):
        return 'about a hour ago'
    if timedelta(days=1) <= difference < timedelta(days=2):
        return 'about a day ago'
    if timedelta(weeks=1) <= difference < timedelta(weeks=2):
        return 'about a week ago'
    if timedelta(days=30) <= difference < timedelta(days=60):
        return 'about a month ago'
    if timedelta(days=365) <= difference < timedelta(days=730):
        return 'about a year ago'
    return '%(time)s ago' % {'time': timesince(value).split(', ')[0]}
