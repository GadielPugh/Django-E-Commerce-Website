from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'laptop', 'date_of_purchase', 'is_paid')
    list_filter = ('is_paid',)
    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        queryset.update(is_paid=True)
    mark_as_paid.short_description = "Mark selected transactions as paid"

admin.site.register(Transaction, TransactionAdmin)
