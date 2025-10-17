from django.contrib import admin
from .models import Statement,Contact

class StatementAdmin(admin.ModelAdmin):
    list_display = ( 'last_name', 'id_number', 'incident_type', 'incident_location','incident_date')
    search_fields = ( 'last_name', 'id_number','incident_location')
    list_filter = ('recorded_at',)

admin.site.register(Statement, StatementAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'contact_name', 'contact_email', 'contact_message')
    search_fields = ( 'contact_name', 'contact_email', 'contact_message')
    list_filter = ('contact_name', 'contact_email', 'contact_message')

admin.site.register(Contact, ContactAdmin)





# Register your models here.
