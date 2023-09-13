from datetime import datetime, timezone, timedelta
from django import template
register = template.Library()


@register.simple_tag
def current_times():
    return {
        'local_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'utc_time':  datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        'time_zone': datetime.now().astimezone().tzinfo
    }


@register.simple_tag
def date_range(num):
    today = datetime.now()
    date_list = [today + timedelta(days=i) for i in range(num)]
    return date_list
