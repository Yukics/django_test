from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author) Esta comentado para definir con una clase el comportamiento del formulario de esta tabla
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)

class BookInline(admin.TabularInline):
    model = Book
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

'''
@admin.register(Book)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
#Con el inlines de arriba y la clase de abajo insertamos el formulario dentro de otro formulario
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]'''


#admin.site.register(Book, BookAdmin)
# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status','due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
