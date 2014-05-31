from arkansassymphony.staff_board.models import Administrator
from django.contrib import admin

class AdministratorAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basic info',	{'fields': ['name', 'title']}),
		('Order',	{'fields': ['order']}),
		('Staff, board, or advisor?',	{'fields': ['board_or_staff']}),
		('For board members only',	{'fields': ['board_type']}),
		('Staff only',	{'fields': ['email', 'phone', 'department']}),
	]
	
	list_display = ('name', 'board_or_staff', 'board_type', 'department', 'title', 'order')
admin.site.register(Administrator, AdministratorAdmin)
