from core.models import Restaurent, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models import Count, F, Value


def run():
    pass
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
    
    # restaurent = Restaurent.objects.first()
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
    # print(restaurent.sales.all())
    
    ################################################################
    ########### Getting or Creating/ Updating data with Model ######
    
    # restaurent = Restaurent.objects.first()
    # user = User.objects.first()
    
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
    ########### Updating Queries ##########################
    
    # restaurent = Restaurent.objects.first()
    # print(restaurent.name)
    
    # restaurent.name = "The Italian Pizza Shop"
    # restaurent.save()
    
    # Restaurent.objects.create(
    #     name="The Maharaja Cafe",
    #     date_opened=timezone.now(),
    #     latitute =50.2,
    #     longitute=30.3
    # )


    # restaurent.name = "The Irani Chai Shop"
    # restaurent.save(update_fields=['name'])
    
    #######################################################
    ############### Validators Examples ###################
    
    # user = User.objects.get(id=3)
    # restaurent = Restaurent.objects.get(id=3)
    
    # # Rating.objects.create(user=user,restaurent=restaurent,rating=9)
    # user = User.objects.get( id = 2 )
    # restaurent = Restaurent.objects.get(id=7)      
    
    
    # Rating.objects.create(user=user,restaurent=restaurent,rating=9)
    # rating = Rating.objects.create(user=user,restaurent=restaurent,rating=9)
    # rating.full_clean()
    # rating.save()
    
    ###############################################################
    ########## Updating Queryset of records #######################
    
    # restaurents = Restaurent.objects.all()
    # restaurents.update(
    #     date_opened=timezone.now()
    # )
    
    ###############################################################
    ########## Field Lookups ######################################
    # exact
    # iexact
    # contains
    # icontains
    # startswith
    
    # restaurents = Restaurent.objects.filter(name__startswith='T')
    # print(restaurents)
    
    # restaurents.update(
    #     date_opened=timezone.now() - timezone.timedelta(days=365)
    # )
    
    # restaurent = Restaurent.objects.get(id=5)
    # print(restaurent.pk)
    
    # # print(restaurent.ratings.all())
    # restaurent.delete()
    
    # Restaurent.objects.all().delete()
    ################# OPTIONS ON DELETION ###########################
    
    ## CASCADE
    ## PROTECT
    ## RESTRICT
    ## SET_NULL
    ## SET_DEFAULT
    
    #################################################################
    ############### Queryset Filtering and lookups/Ordering##########
    
    # print(Restaurent.objects.count())
    
    # print(Rating.objects.count())
    
    # print(Sale.objects.count())
    
    
    # restaurents = Restaurent.objects.filter(restaurent_type=Restaurent.TypeChoices.ITALIAN)
    # print(restaurents)
    
    # print(Restaurent.objects.filter(name="Dragon Wok"))
    
    # restaurent = Restaurent.objects.filter(name="Dragon Wok")
    # print(restaurent.count())
    
    ## Converting Queryset to single objects with get()
    ## get only return single instance of a queryset of object
    # print(restaurent.get())


    ### Failuer of filtering multiple objects with get
    
    # restaurent = Restaurent.objects.get(restaurent_type=Restaurent.TypeChoices.ITALIAN)
    # print(restaurent)
    
    ## get as it dont return multiple objects of a queryset it give error of MultipleObjectReturned Error
    
    # restaurent = Restaurent.objects.filter(restaurent_type=Restaurent.TypeChoices.ITALIAN)
    # print(restaurent.exists())
    
    # restaurent = Restaurent.objects.filter(name="jahsgasjdh")
    # print(restaurent.exists())
    
    ##################################################################
    ############Multiple Filters######################################
    
    
    # italian = Restaurent.TypeChoices.ITALIAN
    # restaurent = Restaurent.objects.filter(restaurent_type=italian)
    # print(restaurent)
    
    
    # italian = Restaurent.TypeChoices.ITALIAN
    # restaurent = Restaurent.objects.filter(restaurent_type=italian,name__startswith='T')
    # print(restaurent)
    
    
    
    ############# IN (in) lookup in Filter ##############
    
    # chinese = Restaurent.TypeChoices.CHINESE
    # indian = Restaurent.TypeChoices.INDIAN
    # italian = Restaurent.TypeChoices.ITALIAN
    
    # filter_types = [chinese,italian]
    
    # restaurents = Restaurent.objects.filter(restaurent_type__in=filter_types)
    # print(restaurents)
    
    ################## exclude mehtod ###################
    ## In refrence to SQL it puts an NOT operator in front of your where clause
    
    # chinese = Restaurent.TypeChoices.CHINESE
    # indian = Restaurent.TypeChoices.INDIAN
    # # restaurents = Restaurent.objects.exclude(restaurent_type=chinese)
    # # print(restaurents)
    
    # filter_types = [chinese,indian]
    
    # restaurents = Restaurent.objects.exclude(restaurent_type__in=filter_types)
    # print(restaurents)
    
    ################# Additional lookups ###############
    # restaurents = Restaurent.objects.filter(name__lt='E')
    # print(restaurents)    
    
    # restaurents = Restaurent.objects.filter(longitute__gt=0)
    # print(restaurents)  
    
    # restaurents = Restaurent.objects.exclude(longitute__gt=0)
    # print(restaurents)  
    
    # sale = Sale.objects.filter(income__gt=1000)
    # print(sale)
    # for sa in sale:
    #     print(sa.restaurent.name)
        
    # sale = Sale.objects.filter(income__gt=1000).select_related('restaurent')
    # for sa in sale:
    #     print(sa.restaurent.name) 
        
        
    #     SELECT 
    #     sale.id,
    #     sale.income,
    #     sale.datetime,
    #     sale.restaurent_id,
    #     restaurent.id,
    #     restaurent.name,
    #     restaurent.website,
    #     restaurent.date_opened,
    #     restaurent.latitute,
    #     restaurent.longitute,
    #     restaurent.restaurent_type
    # FROM app_sale AS sale
    # INNER JOIN app_restaurent AS restaurent
    # ON sale.restaurent_id = restaurent.id
    # WHERE sale.income > 1000;

    # sales_all = Sale.objects.filter(income__range=(1000,2000))

    
    # sales_all = Sale.objects.filter(income__range=(1000, 2000)).select_related('restaurent')
    # print(sales_all)
    # for sale in sales_all:
    #     print(sale.restaurent)
    
    ############## ORDER BY 
    
    # restaurents = Restaurent.objects.order_by('-name')  # order Alphabetically
    # print(restaurents)
    
   
    # sales = Sale.objects.all().order_by('income').select_related('restaurent') # Ascending Order
    # sales = Sale.objects.all().order_by('-income').select_related('restaurent') # Descending Order
    
    # for data in sales:
    #     print(data.restaurent)
    
    #############################################################################
    ################### prefetch_related ########################################
    
    # restaurent = Restaurent.objects.first()
    # print(restaurent.rating_set.all())
    
    # print(restaurent.ratings.all())  
    
    #restaurents = Restaurent.objects.prefetch_related('ratings')
    #print(restaurents)
    
    #############################################################################
    ###################### Limiting #############################################
    
    
    # restaurent = Restaurent.objects.order_by('date_opened')[:2]
    # print(restaurent)
    
    ###### Default way of ordering can be done in modes.py file Model class by adding below code
    
    # class Meta:
    #     ordering = [Lower('name')]
    
    # restaurents = Restaurent.objects.all()
    # print(restaurents)
    
    ################################################################################
    ##################### Earliest and Latest ######################################
    
    # restaurent = Restaurent.objects.earliest('date_opened')
    # print(restaurent.date_opened)
    
    # restaurent = Restaurent.objects.latest('date_opened')
    # print(restaurent.date_opened)
    
    ################################################################################
    ###################### F() Expressions #########################################
    
    ## USE CASE 1: Update a Field Based on Its Current Value
    ##
    
    # for r in Restaurent.objects.all():
    #     print(r.name, [rating.rating for rating in r.ratings.all()])
    
    
    # restaurents = Restaurent.objects.prefetch_related('ratings')
    
    # # print(restaurents[0].ratings.all())
    
    # for r in restaurents:
    #     print(r.name, [rating.rating for rating in r.ratings.all()])
    # sale = Sale.objects.filter(id=1).update(income=F('income') * 1.10)
    
    #################################################################################
    
    ######## Updating sale price on DB level only
    # Sale.objects.filter(id=sale.id).update(income=F('income') * 1.10)
    # updated_sale = Sale.objects.get(id=1)
    # print(updated_sale.income)
    
    
    ######### Updating sale price on python side not DB
    # sale = Sale.objects.get(id=1)
    # sale.income *= 1.10
    # sale.save()
    
    #########################################################################################
    # 🆚 .update() vs .save() Summary                                                      # 
    #                                                                                       #
    # Method	 Applies to	        Calls save() logic?	    Validations?	  Efficient?    #
    #                                                                                       #
    # update()	 QuerySet only	    ❌ No	                  ❌ No	          ✅ Yes     #
    # save()	 Single instance	✅ Yes	                  ✅ Yes	          ❌ No      #
    #                                                                                       #
    #########################################################################################
    
    '''
        .update() works only with filter() because it's designed for 
         direct SQL-level updates on querysets — not for individual objects.
    '''
    #########################################################################################
    ## USE CASE 2: Filter Where One Field Is Greater Than Another
    ##
     
    # restaurents = Restaurent.objects.filter(latitute__gt=F('longitute'))
    
    ## Without F()
    # restaurents = Restaurent.objects.all()
    # filtered = [r for r in restaurents if r.latitute > r.longitute]
    # print(filtered)
    
    # restaurents = list(Restaurent.objects.all())  # Make sure values are loaded
    # for r in restaurents:
    #     print(r.name, r.latitute, r.longitute)
    # filtered = [r for r in restaurents if r.latitute > r.longitute]
    
    
    # print(restaurents)
    ## USE CASE 3: Bulk Update
    # Sale.objects.update(income=F('income') * 1.1)
    # # Without F() expression
    # for sale in Sale.objects.all():
    #     sale.income *= 1.1
    #     sale.save()
    ###################################################################################
    ############### N + 1 problem and solutions #######################################
    
    pprint(connection.queries)