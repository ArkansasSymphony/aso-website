from arkansassymphony.galleries.models import Gallery, Photo, Audio
from django.contrib import admin
	
class PhotosAdmin(admin.ModelAdmin):
	fieldsets = [
		('Select Gallery', {'fields': ['gallery']}),
		('Upload photo', {'fields': ['photo']}),
		('Photo info', {'fields': ['photo_id', 'short_desc']}),
	]
	
	list_display = ('photo_id', 'short_desc', 'gallery')

class GallerysAdmin(admin.ModelAdmin):
	prepopulated_fields = {"url_name": ("name",)}

admin.site.register(Audio)
admin.site.register(Gallery, GallerysAdmin)
admin.site.register(Photo, PhotosAdmin)
