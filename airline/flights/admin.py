from django.contrib import admin

from .models import Flights,airport,passenger

# Register your models here.
class FlightsAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")
class passengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
admin.site.register(airport)
admin.site.register(Flights , FlightsAdmin)
admin.site.register(passenger, passengerAdmin)