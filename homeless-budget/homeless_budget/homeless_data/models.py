from django.db import models

class DataSource(models.Model):
   description = models.CharField(max_length=40, blank=True, default='')
   class Meta:
       ordering = ('description',)

   def __str__(self):
       return self.description

class PopType(models.Model):
   description = models.CharField(max_length=40, blank=True, default='')
   class Meta:
       ordering = ('description',)

   def __str__(self):
       return self.description


class SubType(models.Model):
   description = models.CharField(max_length=40, blank=True, default='')
   class Meta:
       ordering = ('description',)

   def __str__(self):
       return self.description


class HomelessStat(models.Model):
   source = models.ForeignKey(DataSource, )
   population = models.ForeignKey(PopType, )
   subpopulation = models.ForeignKey(SubType, )
   record_dt = models.DateField()
   record_value = models.IntegerField(blank=True,)
