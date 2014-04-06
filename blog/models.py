from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu)
    title = models.CharField(max_length=100)
    url = models.URLField()
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('order',)