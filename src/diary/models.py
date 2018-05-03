from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save





class Diary(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('diary:detail', kwargs = {'slug':self.slug})


from .utils import unique_slug_generator

def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(pre_save_post_receiver,sender = Diary)