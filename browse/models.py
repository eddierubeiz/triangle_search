from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class TriangleIssue(models.Model):
    pub_date = models.DateTimeField('date published')
    volume = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    issue_url = models.TextField()
    ocr_text= models.TextField()
    notes_2= models.TextField()
    notes_3= models.TextField()

    def __str__(self):
        return "Drexel Triangle, v. %d, n. %d, published  %s " % (self.volume, self.number, self.pub_date.strftime("%b. %d,  %Y"))
        
            
    def dir(self):
        return dir(self)
    
    def get_absolute_url(self):
        return reverse('issue', args=[self.id])

    dir = property(dir)


@python_2_unicode_compatible  # only if you need to support Python 2
class TriangleArticle(models.Model):
    title = models.TextField()
    description = models.TextField()
    keywords = models.TextField()
    page = models.IntegerField(default=0)
    issue = models.ForeignKey(TriangleIssue, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)
    notes_1= models.TextField()
    notes_2= models.TextField()
    notes_3= models.TextField()

    def __str__(self):
        return "Triangle article: %s " % self.title

    def get_absolute_url(self):
        return reverse('article', args=[self.id])

    def dir(self):
        return dir(self)

    dir = property(dir)
