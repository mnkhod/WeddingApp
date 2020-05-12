from django.contrib import admin
from .models import Hurimiin_Yslol_Uilchilgee
from .models import Tureesiin_Uilchilgee
from .models import Neriin_Buteegdehuun
from .models import Surgalt
from .models import Hamtragch_Baiguulgiin_Zuuchlah_Uilchilgee



@admin.register(Hamtragch_Baiguulgiin_Zuuchlah_Uilchilgee)
class Hamtragch_Baiguulgiin_Zuuchlah_UilchilgeeAdmin(admin.ModelAdmin):
    # Display on Object List Page
    list_display = ('name','price','picture')
    # list page now include right side bar with filters
    list_filter = ('price',)
    # Search Bar
    search_fields = ('name','price')

@admin.register(Surgalt)
class SurgaltAdmin(admin.ModelAdmin):
    # Display on Object List Page
    list_display = ('name','price','picture')
    # list page now include right side bar with filters
    list_filter = ('price',)
    # Search Bar
    search_fields = ('name','price')

@admin.register(Neriin_Buteegdehuun)
class Neriin_ButeegdehuunAdmin(admin.ModelAdmin):
    # Display on Object List Page
    list_display = ('name','price','picture')
    # list page now include right side bar with filters
    list_filter = ('price',)
    # Search Bar
    search_fields = ('name','price')




@admin.register(Tureesiin_Uilchilgee)
class Tureesiin_UilchilgeeAdmin(admin.ModelAdmin):
    # Display on Object List Page
    list_display = ('name','price','picture')
    # list page now include right side bar with filters
    list_filter = ('price',)
    # Search Bar
    search_fields = ('name','price')

@admin.register(Hurimiin_Yslol_Uilchilgee)
class Hurimiin_Yslol_UilchilgeeAdmin(admin.ModelAdmin):
    # Display on Object List Page
    list_display = ('name','price','picture')
    # list page now include right side bar with filters
    list_filter = ('price',)
    # Search Bar
    search_fields = ('name','price')

