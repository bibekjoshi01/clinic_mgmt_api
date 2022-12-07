from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

User = get_user_model()

class Blog(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    content = FroalaField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:100]
    
    class Meta:
        ordering = ['-created_at', '-updated_at']
    
    def get_api_url(self):
        try: 
            return reverse("blogs_api:blog_detail", kwargs={"slug":self.slug})
        except: 
            None
    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter(parent=instance)
        return qs


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Blog)

class Comment(models.Model):
    parent = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-created_at', '-updated_at']