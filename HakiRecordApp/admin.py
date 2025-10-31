from django.contrib import admin
from .models import Statement,Contact

class StatementAdmin(admin.ModelAdmin):
    list_display = ( 'last_name', 'id_number', 'incident_type', 'incident_location','incident_date')
    search_fields = ( 'last_name', 'id_number','incident_location')
    list_filter = ('recorded_at',)
    readonly_fields = [f.name for f in Statement._meta.fields]

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Statement, StatementAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'contact_name', 'contact_email', 'contact_message')
    search_fields = ( 'contact_name', 'contact_email', 'contact_message')
    list_filter = ('contact_name', 'contact_email', 'contact_message')

admin.site.register(Contact, ContactAdmin)





# Register your models here.
