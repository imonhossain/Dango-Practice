from django.db import models

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=200)
  establish_year = models.IntegerField(default=0)
  def __str__(self):
        return '{}'.format(self.name)

class AcademicYear(models.Model):
  year = models.IntegerField(default=0)
  def __str__(self):
        return '{}'.format(self.year)

class ClassInfo(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
        return '{}'.format(self.name)

class Subject(models.Model):
  year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  code = models.CharField(max_length=10)
  credit = models.IntegerField(default=0)
  marks = models.IntegerField(default=0)

class Department(models.Model):
  year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  code = models.CharField(max_length=10)
  def __str__(self):
        return '{}'.format(self.name)
