from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'weight', 'is_approved', 'created_at')
    list_filter = ('category', 'is_approved')
    search_fields = ('user__username', 'category')
    actions = ['approve_records']

    def approve_records(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Выбранные записи были одобрены.")
    approve_records.short_description = "Одобрить выбранные записи"