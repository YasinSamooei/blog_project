from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Comment,Blog,Notification
from accounts.models import User

@receiver(post_save, sender=Comment)
def create_reply_notification_signal(sender, instance, created, *args, **kwargs):
    """
    craete notification when user reply comment 
    """
    if created :
        if instance.parent_id:
            if instance.parent.user != instance.user:
                message = f'A user replied to your message in the article {instance.blog.title}.'
                blog=instance.blog
                Notification.objects.create(user=instance.parent.user, message=message,blog=blog)
        elif instance.user != instance.blog.author:
            message = f'A user left a message under your article: {instance.blog.title}'
            blog=instance.blog
            Notification.objects.create(user=instance.blog.author, message=message,blog=blog)


@receiver(post_save, sender=Blog)
def create_blog_notification_signal(sender, instance, created, *args, **kwargs):
    """
    craete notification when add new article
    """
    if created:
        message = f'The article {instance.title} was published.'
        blog=instance
        user=User.objects.all()
        public=Notification.objects.create(message=message,blog=blog)
        public.all_user.set(user)
