from django.contrib import admin
from v0.models import (
    Log, 
    Person, 
    Offer, OfferTag, OfferComment
)

# Register your models here.

admin.site.register(Log)
admin.site.register(Person)
admin.site.register(Offer)
admin.site.register(OfferTag)
admin.site.register(OfferComment)

