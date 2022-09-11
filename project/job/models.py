from django.db import models
from django.utils.text import slugify
# Create your models here.

JOB_TYPE = [
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
]

CAREER_LEVEL = [
    ("student","Student"),
    ("entry level","Entry Level"),
    ("junior","Junior"),
    ("senior","Senior"),
    ("manager","Manager"),
]

def image_upload(inestance,filename):
    image_name , extention = filename.split('.')
    
    return "jobs/%s.%s"%(inestance.id,extention)

class Job(models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=10,choices=JOB_TYPE,default='ft')
    job_description = models.TextField(max_length=1000)
    job_requirment = models.TextField(max_length=1000)
    vacancy = models.IntegerField(default=1)
    career_level = models.CharField(max_length=50, choices=CAREER_LEVEL)
    salary = models.IntegerField(default=0,help_text="Enter number with zeros like 12000 not 12k")
    published_at = models.DateTimeField(auto_now_add=True)
    experiance = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True,null=True)
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title + str(self.experiance) + str(self.salary))
        super(Job,self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model) :
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
