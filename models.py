import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils import slugify

class Case(models.Model):
    script = models.ForeignKey('Script', blank=True, null=True, related_name="cases")
    source = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    use_qunit = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return "/cases/%s" % self.id

    def get_run_url(self):
        return "%s/run" % self.get_absolute_url()
    
    def __unicode__(self):
        return "%s" % self.id
    
class Script(models.Model):
    title = models.CharField(max_length=1024)
    source = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title