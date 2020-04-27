from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=100)
    composer = models.CharField(max_length=100)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitprice = models.DecimalField(decimal_places=2,max_digits=10)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
