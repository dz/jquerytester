import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils import slugify

class Case(models.Model):
    title = models.CharField(max_length=1024)
    slug = models.CharField(max_length=1024)

    source = models.TextField()

    script = models.ForeignKey('Script', blank=True, null=True, related_name="cases")

    has_custom = models.BooleanField(default=False)
    custom = models.TextField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def save(self):
        self.slug = slugify(self.title)
        super(Case, self).save()
    
    def __unicode__(self):
        return self.title
    
class Script(models.Model):
    title = models.CharField(max_length=1024)
    
    source = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)