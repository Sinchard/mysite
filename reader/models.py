from django.db import models
from django.urls import reverse


# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=200, null=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Fiction(BaseModel):
    fiction_id = models.PositiveIntegerField(null=False, db_index=True)
    save = models.BooleanField(default=True)

    def __str__(self):
        return "fiction name:{0},fiction url:{1}".format(self.name, self.url)

    def get_absolute_url(self):
        return '/reader/{0}/'.format(self.fiction_id)



class Chapter(BaseModel):
    fiction_id = models.PositiveIntegerField(null=False, db_index=True)
    chapter_id = models.DecimalField(max_digits=20, decimal_places=2, null=False, db_index=True)

    def __str__(self):
        return "chapter name:{0},fiction url:{1}".format(self.name, self.url)

    def get_absolute_url(self):
        cid=0
        if self.chapter_id==int(self.chapter_id):
            cid=int(self.chapter_id)
        else:
            cid=str(self.chapter_id).replace('.','_')
        return '/reader/{0}/{1}/'.format(self.fiction_id, cid)


class Content(models.Model):
    fiction_id = models.PositiveIntegerField(null=False, db_index=True)
    chapter_id = models.DecimalField(max_digits=20, decimal_places=2, null=False, db_index=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Content:{0}".format(self.content)

    def get_absolute_url(self):
        return '/reader/{0}/{1}/'.format(self.fiction_id, "{.2f%}".format(self.chapter_id))
