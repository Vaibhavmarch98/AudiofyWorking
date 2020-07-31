from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
#when a user is saved then it sends 
#post_save signal, this signal is recieved by the creat_profile
# reciever and it takes all the arguents that are passed by post_save signal, 
#and one is the user instance, and one is created which triggers the reciever,
#kwargs just accepts any extra keyword args.
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)





@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):
	if created:
		instance.profile.save()