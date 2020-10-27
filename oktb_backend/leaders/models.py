from PIL import Image
from django.db import models


class LeaderCategory(models.Model):
    title = models.CharField(max_length=100)
    label = models.CharField(max_length=150)
    active = models.BooleanField()

    def save(self):
        if not LeaderCategory.objects.all():
            self.active = True
        else:
            self.active = False
        super(LeaderCategory, self).save()

    def __str__(self):
        return self.title


class Leader(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(LeaderCategory, on_delete=models.CASCADE)
    link = models.URLField()
    img = models.ImageField(upload_to='static/leaders')
    audience = models.PositiveIntegerField()
    job = models.CharField(max_length=200)
    phone = models.TextField(max_length=30)
    mail = models.EmailField()
    top = models.BooleanField()

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

        leaders = Leader.objects.filter(category__id=Leader.objects.get(id=self.id).category.id)
        self.top = True

        if len(leaders) > 4:
            not_top = Leader.objects.filter(id=self.id - 4)
            not_top.update(top=False)

        super(Leader, self).save()

    class Meta:
        ordering = ['name']