from django.db import models


class Parts(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=260)
    image = models.ImageField(upload_to='parts/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
