from django.contrib import admin
from .models import Person, Loginto, Suggestion, FriendRequest, Friends, Profile

# Register your models here.
admin.site.register(Person)
admin.site.register(Loginto)
admin.site.register(Suggestion)
admin.site.register(FriendRequest)
admin.site.register(Friends)
admin.site.register(Profile)