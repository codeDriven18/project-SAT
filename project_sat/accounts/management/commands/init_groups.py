from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import Task   # replace with your model

class Command(BaseCommand):
    help = "Initialize default groups and permissions"

    def handle(self, *args, **options):
        # Define groups
        groups_permissions = {
            "Editors": ["view_task", "change_task"],
            "Managers": ["view_task", "change_task", "delete_task", "can_approve_task"],
        }

        for group_name, perms in groups_permissions.items():
            group, _ = Group.objects.get_or_create(name=group_name)

            for codename in perms:
                try:
                    if codename == "can_approve_task":
                        perm = Permission.objects.get(codename=codename)
                    else:
                        content_type = ContentType.objects.get_for_model(Task)
                        perm = Permission.objects.get(codename=codename, content_type=content_type)
                    group.permissions.add(perm)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Permission {codename} not found"))

            self.stdout.write(self.style.SUCCESS(f"Group {group_name} updated"))
