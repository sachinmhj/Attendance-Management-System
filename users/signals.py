from django.db.models.signals import post_migrate
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import CustomUser

@receiver(post_migrate)
def generate_slugs_for_existing_users(sender, **kwargs):
    if sender.name == 'users':
        # print(True)
        allusersqueryset = CustomUser.objects.all()
        alluserslist = [x for x in allusersqueryset]
        # print(alluserslist)
        for single_user in alluserslist:
            if single_user.user_slug == '':
                single_user.user_slug = slugify(f'{single_user.username} {single_user.pk}')
                single_user.save()

@receiver(post_save, sender=CustomUser)
def send_blog_post_notification(sender, instance, created, **kwargs):
    if created:
        instance.user_slug = slugify(f'{instance.username} {instance.pk}')
        instance.save()