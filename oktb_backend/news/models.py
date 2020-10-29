from PIL import Image
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='static/news/')
    text = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            img = Image.open(self.img.path)

            width, height = img.size
            ratio = round(height / width)
            newheight = ratio * 300

            img = img.resize((500, 500), Image.ANTIALIAS)
            img.save(self.img.path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'