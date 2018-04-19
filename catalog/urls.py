from django.urls import path, re_path
from . import views


app_name = 'catalog'
urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'borrowed/', views.AllBorrowedBooksListView.as_view(), name='all-borrowed'), #Added for challenge
]
