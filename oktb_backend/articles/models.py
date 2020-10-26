from PIL import Image
from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    def save(self):
        if not Theme.objects.all():
            self.is_active = True
        else:
            self.is_active = False
        super(Theme, self).save()


class Article(models.Model):
    title = models.CharField(max_length=250, unique=True)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/articles/')
    is_active = models.BooleanField(default=True)
    hot = models.BooleanField()

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

        articles = Article.objects.filter(theme__id=Article.objects.get(id=self.id).theme.id)
        self.hot = True

        if len(articles) > 2:
            not_hot = Article.objects.filter(id=self.id-2)
            not_hot.update(hot=False)

        super(Article, self).save()




