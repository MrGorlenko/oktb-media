from PIL import Image
from django.db import models
import re


class Video(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='static/videos')
    about = models.TextField()
    video = models.URLField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            img = Image.open(self.img.path)

            width, height = img.size
            ratio = round(height / width)
            newheight = ratio * 300

            img = img.resize((500, 500), Image.ANTIALIAS)
            img.save(self.img.path)

        self.video = self.video.replace("watch?v=", 'embed/')
        self.video = re.sub(r'&.+', '', self.video)

        super(Video, self).save()
