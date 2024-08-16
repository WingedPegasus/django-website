from django.contrib import admin
from .models import Member,BlogModel
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date","phone")
admin.site.register(Member)

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
   pass

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)

