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
    title = models.CharField('عنوان', max_length=30)
    slug = models.SlugField('اسلاگ', allow_unicode=True, blank=True, null=True, unique=True)
    created_at = models.DateTimeField('تاریخ آپلود دسته بندی', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('تاریخ به روز رسانی دسته بندی', auto_now=True, null=True)

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'
        ordering = ['-updated_at']

    def __str__(self):
        return self.title


class Blog(models.Model):

    title = models.CharField('عنوان', max_length=50)
    tag = models.ManyToManyField(Tag, related_name='blogs', verbose_name='برچسب ها')
    description = models.TextField('توضیحات')
    meta_description = models.CharField('متادیسکریپشن', max_length=3000)
    image = models.ImageField('تصویر مقاله', upload_to='images/blog', null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')
    created_at = models.DateTimeField('تاریخ آپلود مقاله', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ به روز رسانی مقاله', auto_now=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='blogs',
                                verbose_name='نویسنده مقاله')
    slug = models.SlugField('اسلاگ', unique=True, null=True, blank=True, allow_unicode=True)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ["-created_at"]

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        else:
            return format_html('<h3 style="color: red">بدون تصویر</h3>')

    def __str__(self):
        return self.title

    show_image.short_description = 'تصویر'

    def get_absolute_url(self):
        return reverse('blog:blog-detail', kwargs={'slug': self.slug})



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله مربوطه')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True,
                               verbose_name='کامنت پدر')
    body = models.TextField('متن کامنت')
    created_at = models.DateTimeField('تاریخ و زمان', auto_now_add=True)

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت‌ها'
        ordering = ["-blog__id", "parent__id"]

    def show_body(self):
        return self.body[:25]


class Notification(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='notifs',verbose_name="کاربر")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد")
    message = models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE, null=True, blank=True, related_name='notifs',verbose_name="مقاله")

    class Meta:
        verbose_name="خبر"
        verbose_name_plural="اخبار"
        ordering = ('-created_at',)

    def get_jalali_date(self):
        return JalaliDate(self.created_at, locale=('fa')).strftime("%c")

    def __str__(self):
        return f"{self.user} , {self.message[:10]}"

