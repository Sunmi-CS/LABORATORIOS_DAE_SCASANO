from django.contrib import admin
from .models import LibraryBranch, BookCopy, BookLoan, Reservation

@admin.register(LibraryBranch)
class LibraryBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')

@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'branch', 'condition', 'is_available', 'inventory_number')
    search_fields = ('book__title', 'inventory_number')
    list_filter = ('condition', 'is_available')

@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ('copy', 'borrower', 'checkout_date', 'due_date', 'return_date', 'status')
    list_filter = ('status',)
    search_fields = ('borrower__username', 'copy__book__title')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'branch', 'request_date', 'status')
    list_filter = ('status',)
    search_fields = ('book__title', 'user__username')
