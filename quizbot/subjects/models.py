from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Misc(models.Model):
    question = models.TextField(null=False,)
    op1 = models.TextField(null=False,)
    slug	=	AutoSlugField(populate_from='question',max_length=750,unique=True,null=True,default=None) 
    op2 = models.TextField(null=False,)
    op3 = models.TextField(null=False,)
    op4 = models.TextField(null=False,)