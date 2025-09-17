from django.contrib import admin
from .models import BookView, CategoryAnalytics, AuthorAnalytics, RecommendationLog

@admin.register(BookView)
class BookViewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'timestamp')
    search_fields = ('book__title', 'user__username')

@admin.register(CategoryAnalytics)
class CategoryAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('category', 'total_views', 'total_books', 'popularity_score', 'last_updated')

@admin.register(AuthorAnalytics)
class AuthorAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('author', 'total_views', 'avg_rating', 'total_reviews', 'last_updated')

@admin.register(RecommendationLog)
class RecommendationLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'reason', 'timestamp', 'clicked')
    list_filter = ('clicked',)
