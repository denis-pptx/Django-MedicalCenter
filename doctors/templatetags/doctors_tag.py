from django import template
from doctors.models import Profile, Category

register = template.Library()


@register.inclusion_tag('doctors/doctors_tag.html')
def get_doctors(service_category_slug=None):
    if service_category_slug:
        profiles = Profile.objects.filter(specializations__service_category__slug=service_category_slug).distinct()
    else:
        profiles = Profile.objects.all()

    return {'profiles': profiles}
