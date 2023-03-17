
from django.contrib import admin

from .models import Autor, Livro, Categoria, Editora

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
