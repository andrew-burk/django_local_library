from django.contrib import admin

# Register your models here.


from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

# Define the admin class

class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
# Register the admin class with the associated model
    inlines = [BooksInline]


''' list_filter = ('title', 'summary', 'isbn', 'genre', 'language')
fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
        }),
        ('Availability', {
            'fields': ('title', 'summary', 'isbn', 'display_genre', 'language')
        }),
    )  '''

 


 
# Register the Admin classes for Book using the decorator


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
# Register the Admin classes for BookInstance using the decorator
admin.site.register(Book, BookAdmin)


@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_date', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    ) 
    list_display = ('book', 'status', 'due_back', 'id')
