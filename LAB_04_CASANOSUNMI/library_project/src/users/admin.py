from django.contrib import admin
from .models import LibraryUser, ReadingList, BookReview

@admin.register(LibraryUser)
class LibraryUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'bio')
    search_fields = ('username', 'email')

@admin.register(ReadingList)
class ReadingListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_public', 'created_at')
    search_fields = ('name', 'user__username')
    list_filter = ('is_public',)

@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    search_fields = ('book__title', 'user__username')
    list_filter = ('rating',)
