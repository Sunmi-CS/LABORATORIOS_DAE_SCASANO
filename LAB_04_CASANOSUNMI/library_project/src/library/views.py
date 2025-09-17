from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Author, Book, Category, Publisher






# Añade estas importaciones al principio del archivo si no están:
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json





def home(request):
    """View for home page with library statistics"""
    context = {
        'total_books': Book.objects.count(),
        'total_authors': Author.objects.count(),
        'total_categories': Category.objects.count(),
        'total_publishers': Publisher.objects.count(),
        # Get categories with book counts 📊
        'categories': Category.objects.annotate(
            book_count=Count('books')
        ).order_by('-book_count')[:5],
        # Get recent books 📚
        'recent_books': Book.objects.select_related('author').order_by('-publication_date')[:5],
    }
    return render(request, 'library/home.html', context)

def author_list(request):
    """View for listing all authors"""
    authors = Author.objects.all().order_by('name')
    return render(request, 'library/author_list.html', {'authors': authors})

def author_detail(request, pk):
    """View for author details with books"""
    author = get_object_or_404(Author, pk=pk)
    # Get all books by this author 📚
    books = author.books.all()
    return render(request, 'library/author_detail.html', {'author': author, 'books': books})

def book_list(request):
    """View for listing all books"""
    books = Book.objects.all().select_related('author').order_by('title')
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, pk):
    """View for book details"""
    book = get_object_or_404(Book, pk=pk)
    # Get all categories for this book 🏷️
    categories = book.categories.all()
    # Get all publishers for this book with publication details 🏢
    publications = book.publication_set.select_related('publisher').all()
    
    context = {
        'book': book, 
        'categories': categories,
        'publications': publications
    }
    return render(request, 'library/book_detail.html', context)

def category_list(request):
    """View for listing all categories"""
    categories = Category.objects.annotate(book_count=Count('books')).order_by('name')
    return render(request, 'library/category_list.html', {'categories': categories})

def category_detail(request, slug):
    """View for category details with books"""
    category = get_object_or_404(Category, slug=slug)
    # Get all books in this category 📚
    books = category.books.all().select_related('author')
    return render(request, 'library/category_detail.html', {'category': category, 'books': books})

























# --- Endpoints JSON ---

def api_books(request):
    """GET: lista de libros (id, title, author, isbn, publication_date)"""
    if request.method != 'GET':
        return HttpResponseBadRequest('Sólo GET permitido')
    books = list(
        Book.objects.select_related('author').values(
            'id','title','isbn','publication_date','summary','author__id','author__name'
        )
    )
    # Normalizar author
    for b in books:
        b['author'] = {'id': b.pop('author__id'), 'name': b.pop('author__name')}
    return JsonResponse(books, safe=False)


def api_book_detail(request, pk):
    """GET: detalle de libro con categorías y publicaciones"""
    if request.method != 'GET':
        return HttpResponseBadRequest('Sólo GET permitido')
    try:
        book = Book.objects.select_related('author').get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({'error':'Not found'}, status=404)
    data = {
        'id': book.id,
        'title': book.title,
        'isbn': book.isbn,
        'publication_date': book.publication_date.isoformat() if book.publication_date else None,
        'summary': book.summary,
        'author': {'id': book.author.id, 'name': book.author.name},
        'categories': list(book.categories.values('id','name','slug')),
        'publications': list(book.publication_set.select_related('publisher').values(
            'id','date_published','country','publisher__id','publisher__name'
        ))
    }
    # nidificar publisher info
    for p in data['publications']:
        p['publisher'] = {'id': p.pop('publisher__id'), 'name': p.pop('publisher__name')}
    return JsonResponse(data)


@csrf_exempt
def api_post_review(request, book_id):
    """
    POST para agregar review:
    body JSON: { "user_id": 1, "rating": 5, "comment": "Me gustó" }
    """
    if request.method != 'POST':
        return HttpResponseBadRequest('Sólo POST permitido')
    try:
        payload = json.loads(request.body.decode('utf-8'))
    except Exception:
        return HttpResponseBadRequest('JSON inválido')

    rating = payload.get('rating')
    comment = payload.get('comment','').strip()
    user_id = payload.get('user_id')

    if not (user_id and rating):
        return HttpResponseBadRequest('user_id y rating son requeridos')

    # Importar modelos localmente para evitar circular imports
    from users.models import LibraryUser
    try:
        user = LibraryUser.objects.get(pk=user_id)
    except LibraryUser.DoesNotExist:
        return JsonResponse({'error':'user not found'}, status=404)

    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return JsonResponse({'error':'book not found'}, status=404)

    # Crear review
    review = BookReview.objects.create(user=user, book=book, rating=int(rating), comment=comment)
    return JsonResponse({'id': review.id, 'book_id': book.id, 'user_id': user.id, 'rating': review.rating}, status=201)





