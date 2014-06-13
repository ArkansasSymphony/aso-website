from arkansassymphony.concerts.models import Piece, Show, Concert, Subscription
from django.contrib import admin

class ShowAdmin(admin.ModelAdmin):
        prepopulated_fields = {"url_name": ("name",)}
	search_fields = ['name']
	list_filter = ['end_date']
	list_display = ('name', 'type', 'season')
class PieceAdmin(admin.ModelAdmin):
	search_fields = ['title', 'composer']
	list_display = ('title', 'composer')
class ConcertAdmin(admin.ModelAdmin):
	search_field = ['show']
        list_display = ('show', 'date', 'pe_id')

admin.site.register(Piece,PieceAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Subscription)


