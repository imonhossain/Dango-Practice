# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

class ActorInfo(models.Model):
    actor_id = models.IntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    film_info = models.TextField(blank=True)
    def __str__(self):
        return '{}'.format(self.first_name)

class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.address)

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.name)

class CategoryActorCount(models.Model):
    name = models.CharField(max_length=25)
    actorname = models.CharField(db_column='ActorName', max_length=91) # Field name made lowercase.
    count_fa_actor_id_field = models.BigIntegerField(db_column='COUNT(FA.actor_id)') # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    def __str__(self):
        return '{}'.format(self.name)
class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.city)

class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.country)

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    active = models.IntegerField()
    create_date = models.DateTimeField()
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.first_name)

class CustomerList(models.Model):
    customer_list_id = models.IntegerField() # Field name made lowercase.
    name = models.CharField(max_length=91)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(db_column='zip code', max_length=10, blank=True) # Field renamed to remove unsuitable characters.
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    notes = models.CharField(max_length=6)
    sid = models.IntegerField(db_column='SID') # Field name made lowercase.
    def __str__(self):
        return '{}'.format(self.name)

class Film(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_year = models.TextField(blank=True) # This field type is a guess.
    language = models.ForeignKey('Language', related_name='filmslanguage', on_delete=models.CASCADE)
    original_language = models.ForeignKey('Language', blank=True, null=True, on_delete=models.CASCADE)
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.IntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=5, blank=True)
    special_features = models.CharField(max_length=54, blank=True)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.title)

class FilmActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.film)

class FilmCategory(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.film)

class FilmList(models.Model):
    fid = models.IntegerField(db_column='FID', blank=True, null=True) # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=5, blank=True)
    actors = models.TextField(blank=True)
    def __str__(self):
        return '{}'.format(self.title)

class FilmText(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    def __str__(self):
        return '{}'.format(self.title)

class Inventory(models.Model):
    inventory_id = models.IntegerField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.film)

class Language(models.Model):
    language_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.name)

class NicerButSlowerFilmList(models.Model):
    fid = models.IntegerField(db_column='FID', blank=True, null=True) # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=5, blank=True)
    actors = models.TextField(blank=True)
    def __str__(self):
        return '{}'.format(self.title)

class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    rental = models.ForeignKey('Rental', blank=True, null=True, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.amount)

class Rental(models.Model):
    rental_id = models.IntegerField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.rental_date)

class SalesByFilmCategory(models.Model):
    category = models.CharField(max_length=25)
    total_sales = models.DecimalField(max_digits=27, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return '{}'.format(self.category)

class SalesByStore(models.Model):
    store = models.CharField(max_length=101)
    manager = models.CharField(max_length=91)
    total_sales = models.DecimalField(max_digits=27, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return '{}'.format(self.store)

class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    picture = models.TextField(blank=True)
    email = models.CharField(max_length=50, blank=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    active = models.IntegerField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.first_name)

class StaffList(models.Model):
    staff_list_id = models.IntegerField() # Field name made lowercase.
    name = models.CharField(max_length=91)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(db_column='zip code', max_length=10, blank=True) # Field renamed to remove unsuitable characters.
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    sid = models.IntegerField(db_column='SID') # Field name made lowercase.
    def __str__(self):
        return '{}'.format(self.name)

class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    manager_staff = models.ForeignKey(Staff,related_name='storesmanagerstaff', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    def __str__(self):
        return '{}'.format(self.manager_staff)

