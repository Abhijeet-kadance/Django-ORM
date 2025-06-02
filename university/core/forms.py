from django import forms
from core.models import Rating,Restaurent
from django.core.validators import MinValueValidator, MaxValueValidator



class RestaurentForm(forms.ModelForm):
    class Meta:
        model=Restaurent
        fields=('name',)
        
# class RatingForm(forms.ModelForm):
#     class Meta:
#         model=Rating
#         fields=('restaurent','user','rating')

# class RatingForm(forms.Form):
#     rating = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

