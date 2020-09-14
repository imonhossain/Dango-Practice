from django.contrib import admin
from django.utils.safestring import mark_safe
# from .models import School, Subject, ClassInfo, Department, AcademicYear
from .models import Actor, ActorInfo, Address, Category, CategoryActorCount, City, Country, Customer, CustomerList, Film, FilmActor, FilmCategory, FilmList, FilmText, Inventory, Language, NicerButSlowerFilmList, Payment, Rental, SalesByFilmCategory, SalesByStore, Staff, StaffList, Store

from django.urls import reverse
from django.utils.http import urlencode
class CityModel(admin.ModelAdmin):
    list_display = ('city', 'country')
    list_filter=[('country', admin.RelatedOnlyFieldListFilter)]
    search_fields = ('city', )
    list_per_page = 3

class CountryModel(admin.ModelAdmin):
    list_display = ["country","link_to_city"]
    def link_to_city(self, obj):
        url = (
            reverse("admin:polls_city_changelist")
            + "?"
            + urlencode({"country_id": f"{obj.country_id}"})
        )
        count = obj.city_set.count()
        return mark_safe('<a href="%s">City (%s)</a>' % (url,count))



admin.site.register(Actor)
admin.site.register(ActorInfo)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(CategoryActorCount)
admin.site.register(City, CityModel)
admin.site.register(Country, CountryModel)
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
