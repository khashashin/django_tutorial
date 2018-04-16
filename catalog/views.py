from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre


# def index(request):
#     """
#     View function for home page of site.
#     """
#     # Generate counts of some of the main objects
#     num_books=Book.objects.all().count()
#     num_instances=BookInstance.objects.all().count()
#     # Available books (status = 'a')
#     num_instances_available=BookInstance.objects.filter(status__exact='a').count()
#     num_authors=Author.objects.count()  # The 'all()' is implied by default.
#
#     # Render the HTML template index.html with the data in the context variable
#     return render(
#         request,
#         'catalog/index.html',
#         context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
#     )


class BookListView(generic.ListView):
    model = Book
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # context_object_name = 'book_list'   # your own name for the list as a template variable
    template_name = 'catalog/index.html'  # Specify your own template name/location
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        display_books = Book.objects.filter(title__icontains='war')[:5]
        # Generate counts of some of the main objects
        num_books=Book.objects.all().count()
        num_instances=BookInstance.objects.all().count()
        # Available books (status = 'a')
        num_instances_available=BookInstance.objects.filter(status__exact='a').count()
        num_authors=Author.objects.count()  # The 'all()' is implied by default.
        # Create any data and add it to the context
        context = {'display_books':display_books,'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors}
        return context


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request,pk):
        try:
            book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

        #book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/book_detail.html',
            context={'book':book_id,}
        )


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/authors.html'
    #context_object_name = 'author_list'
    paginate_by = 10
    #queryset = Author.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        authors = Author.objects.all()
        # Create any data and add it to the context
        context = {
            'authors': authors,
        }
        return context


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request,pk):
        try:
            author_id=Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404("Author does not exist")

        #book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/author_detail.html',
            context={'author':author_id,}
        )
