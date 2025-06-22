from django.contrib import admin
from applications.reference_data.models.country import Country
from applications.reference_data.models.metals_type import MetalType
from applications.reference_data.models.transaction_type import TransactionType

# Register your models here.

admin.site.register(Country)
admin.site.register(MetalType)
admin.site.register(TransactionType)
