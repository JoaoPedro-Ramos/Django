from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    # título
    title = models.CharField(max_length=500, blank=False, null=False) # não pode ser em branco ou nulo
    # conteúdo
    content = RichTextField()
    # data de publicação
    publication_date = models.DateTimeField(auto_now_add=True) # auto_now == toda vez que o objeto for salvo ele vai pegar a data atual. // auto_now_add == a data que fica é a que o objeto foi salvo.
    # slug " https://blablabla/(slug).com "
    slug = models.SlugField(editable=False)
    # resumo 
    description = models.TextField(default='')

    def __str__(self):
        return self.title

    
