from core.models import Restaurent, Rating, Sale
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
    
    #########################################################
    ############### Quering reverse relations in Django #####
    
    
    #restaurent = Restaurent.objects.first()
    # print(restaurent.rating_set.all())
    
    #print(restaurent.ratings.all())  # using related_name as the reverse manager
    
    #########################################################
    ######## Reverse relation on sales ######################
    # restaurent = Restaurent.objects.get(id=3)
    # Sale.objects.create(
    #     restaurent=restaurent,
    #     income=2.33,
    #     datetime=timezone.now()
    # )
    
    # Sale.objects.create(
    #     restaurent=restaurent,
    #     income=2.53,
    #     datetime=timezone.now()
    # )
    
    # Sale.objects.create(
    #     restaurent=restaurent,
    #     income=3.33,
    #     datetime=timezone.now()
    # )
    
    
    # restaurent = Restaurent.objects.get(id=3)
    # print(restaurent.sale_set.all())
    
    ################################################################
    ########### Getting or Creating/ Updating data with Model ######
    
    restaurent = Restaurent.objects.first()
    user = User.objects.first()
    
    # print(Rating.objects.get_or_create(
    #     restaurent=restaurent,
    #     user=user,
    #     rating=3
    # ))
    
    # rating, created = Rating.objects.update_or_create(
    #     restaurent=restaurent,
    #     user=user,
    #     defaults={'rating': 3}
    # )
    
    # print(rating,created)
    
    # if created :
    #     # send email
    
    ########################################################
    ######### Deleting an object ###########################
    
    # restaurent = Restaurent.objects.get(id=1)
    # restaurent.delete()
    
    ########################################################
    
    
    pprint(connection.queries)