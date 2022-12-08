from django.db import models

# Create your models here.
class Misc(models.Model):
    question = models.TextField(null=False,)
    op1 = models.TextField(null=False,)
    op2 = models.TextField(null=False,)
    op3 = models.TextField(null=False,)
    op4 = models.TextField(null=False,)