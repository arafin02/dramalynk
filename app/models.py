from django.db import models
from django.template.defaultfilters import slugify  # new
from django.urls import reverse

# Create your models here.
from django.db import models

# Create your models here.

status = (('Ongoing', 'Ongoing'), ('Ended', 'Ended'))
type = (('Movie', 'Movie'), ('Drama', 'Drama'))


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Origin(models.Model):
    country = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.country


class Drama(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    genre = models.ForeignKey(
        "app.Genre", on_delete=models.CASCADE, to_field='name')
    origin = models.ForeignKey(
        "app.Origin", on_delete=models.CASCADE, to_field='country')
    pub_date = models.DateField()
    epi_num = models.IntegerField()
    season = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=30, choices=type)
    trailer = models.CharField(max_length=300)
    ver_poster = models.CharField(max_length=300)
    hor_poster = models.CharField(max_length=300)
    keywords = models.CharField(max_length=500)
    status = models.CharField(
        max_length=20,
        choices=status
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("details", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Episode(models.Model):
    ep_no = models.CharField(max_length=5)
    dlink = models.CharField(max_length=350, blank=True)
    sublink = models.CharField(max_length=350)
    watch_online = models.CharField(max_length=350, blank=True)
    drama = models.ForeignKey(
        "app.Drama", on_delete=models.CASCADE, to_field='title', db_constraint=False)
    ep_slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'{self.ep_no} - {self.drama.title}'
