from django.db import models
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from persiantools.jdatetime import JalaliDate
from django.utils.html import format_html
from django.urls import reverse
from django.utils.timezone import utc
import datetime
# local
from accounts.models import User

class Tag(models.Model):
    title = models.CharField( max_length=30)
    slug = models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Blog(models.Model):

    title = models.CharField(max_length=50)
    tag = models.ManyToManyField(Tag, related_name='blogs')
    description = models.TextField()
    meta_description = models.CharField(max_length=3000)
    image = models.ImageField(upload_to='images/blog', null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blogs',)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)

    class Meta:
        ordering = ["-created_at"]

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        else:
            return format_html('<h3 style="color: red">no image</h3>')

    def __str__(self):
        return self.title

    show_image.short_description = 'image'

    def get_absolute_url(self):
        return reverse('blog:blog-detail', kwargs={'slug': self.slug})



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True,)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-blog__id", "parent__id"]

    def show_body(self):
        return self.body[:25]


class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='notifs')
    created_at=models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE, null=True, blank=True, related_name='notifs')

    class Meta:
        ordering = ('-created_at',)

    def get_jalali_date(self):
        return JalaliDate(self.created_at, locale=('fa')).strftime("%c")

    def __str__(self):
        return f"{self.user} , {self.message[:10]}"

