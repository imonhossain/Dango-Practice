from django.contrib import admin
# from .models import School, Subject, ClassInfo, Department, AcademicYear
from .models import Actor, ActorInfo, Address, Category, CategoryActorCount, City, Country, Customer, CustomerList, Film, FilmActor, FilmCategory, FilmList, FilmText, Inventory, Language, NicerButSlowerFilmList, Payment, Rental, SalesByFilmCategory, SalesByStore, Staff, StaffList, Store

from django.urls import reverse
from django.utils.http import urlencode
class CityModel(admin.ModelAdmin):
    list_display = ('city', 'country')
    list_filter=[('country', admin.RelatedOnlyFieldListFilter)]
    search_fields = ('city', )



admin.site.register(Actor)
admin.site.register(ActorInfo)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(CategoryActorCount)
admin.site.register(City, CityModel)
admin.site.register(Country)
admin.site.register(Customer)
admin.site.register(CustomerList)
admin.site.register(Film)
admin.site.register(FilmActor)
admin.site.register(FilmCategory)
admin.site.register(FilmList)
admin.site.register(FilmText)
admin.site.register(Inventory)
admin.site.register(Language)
admin.site.register(NicerButSlowerFilmList)
admin.site.register(Payment)
admin.site.register(Rental)
admin.site.register(SalesByFilmCategory)
admin.site.register(SalesByStore)
admin.site.register(Staff)
admin.site.register(StaffList)
admin.site.register(Store)
# Register your models here.

# class SubjectModel(admin.ModelAdmin):
#     list_display = ('name', 'year', 'code', 'credit', 'marks')

# admin.site.register(Subject, SubjectModel)
# admin.site.register(ClassInfo)
# admin.site.register(Department, DepartmentModel)
# admin.site.register(AcademicYear)