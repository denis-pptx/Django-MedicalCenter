from django import template
from datetime import datetime, timezone

register = template.Library()


@register.simple_tag
def current_times():
    return {
        'local_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'utc_time':  datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        'time_zone': datetime.now().astimezone().tzinfo
    }

