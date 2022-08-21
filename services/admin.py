from django.contrib import admin

from services.models import Request, Service


class RequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'user', 'state', 'photo', 'extra_user_des', 'extra_staff_des')
    raw_id_fields = ('user', 'service',)
    list_per_page = 25


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Request, RequestAdmin)
admin.site.register(Service,ServiceAdmin)
