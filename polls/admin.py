from django.contrib import admin
from .models import School, Subject, ClassInfo, Department, AcademicYear
# Register your models here.
class DepartmentModel(admin.ModelAdmin):
    list_display = ('name', 'year', 'code')

class SubjectModel(admin.ModelAdmin):
    list_display = ('name', 'year', 'code', 'credit', 'marks')

admin.site.register(School)
admin.site.register(Subject, SubjectModel)
admin.site.register(ClassInfo)
admin.site.register(Department, DepartmentModel)
admin.site.register(AcademicYear)