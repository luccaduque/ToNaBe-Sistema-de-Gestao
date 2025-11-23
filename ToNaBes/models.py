from django.db import models

class Produto(models.Model):
    """Produtos Cadastrados"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text
    
class Entry(models.Model):
    """Algo específico sobre algum produto."""
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text[:50] + '...'