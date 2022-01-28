from django.contrib import admin
from .models import Post, Category,Venue, MyClubUser, Event
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)
