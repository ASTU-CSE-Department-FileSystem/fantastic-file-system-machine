from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()

@receiver(pre_save, sender=User)
def max_number_of_users_type(sender, instance, **kwargs):
    # if User.objects.filter(id=instance.id).exists():
    #     print("User already exists")    
    if instance.type == User.Types.DEPARTMENT_HEAD:
        print("Department head")   
        if User.objects.filter(department__department=instance.department).filter(type=User.Types.DEPARTMENT_HEAD).count() > 1: 
            instance.delete()
            raise ValidationError(_('Only one Department Head is Allowed.'), code='department')
    else:
        if User.objects.filter(department__department=instance.department).filter(type=User.Types.SECRETARY).count() > 2:
            instance.delete()
            raise ValidationError(_('Max of two Secretaries are Allowed in one Department.'), code='department')

