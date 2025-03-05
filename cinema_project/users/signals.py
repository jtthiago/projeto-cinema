from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, *args, **kwargs):
    if created:
        if instance.is_staff:
            staff_group, _ = Group.objects.get_or_create(name="staff")
            instance.groups.add(staff_group)
        else:
            client_group, _ = Group.objects.get_or_create(name="client")
            instance.groups.add(client_group)