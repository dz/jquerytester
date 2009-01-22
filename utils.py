from django.template import defaultfilters
from django.views.generic.simple import direct_to_template

def render(request, template, extra_context=None):
    return direct_to_template(request, template=template, extra_context=extra_context)
    
    
def slugify(target):
    return defaultfilters.slugify(target)