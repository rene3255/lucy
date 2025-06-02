from django.contrib import admin
from applications.reference_data.models.country import Country
from applications.reference_data.models.metals_type import MetalType

# Register your models here.

admin.site.register(Country)
admin.site.register(MetalType)
