from core.models import Restaurent, Rating
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    
    ######## Creating Object ####################
    
    # restaurent = Restaurent()
    # restaurent.name = "My Italian Restaurent"
    # restaurent.latitute = 50.2
    # restaurent.longitute = 50.2
    # restaurent.date_opened = timezone.now()
    # restaurent.restaurent_type = Restaurent.TypeChoices.ITALIAN
    # restaurent.save()
    
    # Restaurent.objects.create(
    #     name="The Pizza Shop",
    #     date_opened=timezone.now(),
    #     restaurent_type=Restaurent.TypeChoices.ITALIAN,
    #     latitute=50.2,
    #     longitute=50.4
    # )
    
    #################################################
    
    ######## Fetching Objects ####################
    
    # restaurents = Restaurent.objects.all()
    # print(restaurents)
    
    
    # restaurent = Restaurent.objects.first()
    # print(restaurent)
    
    # restaurent = Restaurent.objects.last()
    # print(restaurent)
    
    # restaurent = Restaurent.objects.all()[0]
    # print(restaurent)
    
    #################################################
    
    ############### Randon function #################
    
    # count_rows = Restaurent.objects.count()
    # print(count_rows)
    
    #################################################
    
    ############### Foreign Key Objects #################
    
    # restaurent = Restaurent.objects.first()
    # user = User.objects.first()
    
    # Rating.objects.create(user=user,restaurent=restaurent,rating=3)
    
    # rating = Rating.objects.all()
    # print(rating)
    
    #########################################################
    ################ Filter #################################
    
    # rating = Rating.objects.filter(rating=3)
    
    # Filter Lookups 
    
    # rating_lookup = Rating.objects.filter(rating__gte=3)
    # rating_lookup = Rating.objects.filter(rating__lte=3)
    # rating_lookup = Rating.objects.filter(rating__gt=3)
    # rating_lookup = Rating.objects.filter(rating__lt=3)
    
    ########################################################
    ############# Exclude ##################################
    
    # rating = Rating.objects.exclude(rating=3)
    # rating_lookup = Rating.objects.exclude(rating__gte=3)
    
    
    # print(rating_lookup)
    
    ########################################################
    ############# Updating existing records ################
    
    # restaurent = Restaurent.objects.first()
    # print(restaurent.name)
    
    # restaurent.name = 'My Mexican Restaurent'
    # restaurent.save()    
    
    
    ########################################################
    ############# Quering related records ##################
    
    # rating = Rating.objects.first()
    # print(rating.restaurent.name)
    
    
    pprint(connection.queries)