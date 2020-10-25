from PIL import Image
from django.db import models


class Leader(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    img = models.ImageField(upload_to='static/leaders')
    audience = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            img = Image.open(self.img.path)

            width, height = img.size
            ratio = round(height / width)
            newheight = ratio * 300

            img = img.resize((500, 500), Image.ANTIALIAS)
            img.save(self.img.path)

    class Meta:
        ordering = ['name']