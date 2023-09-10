from django import template
from doctors.models import DoctorProfile, Category

register = template.Library()


@register.inclusion_tag('doctors/doctors_tag.html')
def get_doctors(service_category_slug=None):
    if service_category_slug:
        profiles = DoctorProfile.objects.filter(specializations__service_category__slug=service_category_slug).distinct()
    else:
        profiles = DoctorProfile.objects.all()

    return {'profiles': profiles}
