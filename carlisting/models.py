from django.db import models
from django.urls import reverse
import uuid
#the first model is the car type

class CarType(models.Model):
    #heredocument
    """Model that represents the car type"""
    car_type = models.CharField(max_length = 200, help_text ='Please enter car type (e.g SUV, Saloon..)')

    def __str__(self):
        return self.car_type

#second model
class CarMake(models.Model):
    """Model that represent a car make"""
    #'Make' is a verbose name
    car_make = models.CharField('Make', max_length = 200, help_text ='Please enter car make (e.g Toyota, Nissan..)') 

    def __str__(self):
        return self.car_make
        
#third model
class CarModel(models.Model):
    """Model that represents car model"""

    car_model = models.CharField('Model', max_length = 200, help_text ='Please enter car model (e.g Corolla, Sunny..)') 
    image_one = models.ImageField(upload_to='images/', null = True)
    

    def __str__(self):
        return  self.car_model      

#fourth model
class Car(models.Model):
    """Model that represents a car"""
    registration = models.CharField('Reg No.',max_length = 7, unique = True)
    car_type = models.ForeignKey(CarType, on_delete = models.RESTRICT)
    car_make = models.ForeignKey(CarMake, on_delete = models.RESTRICT)
    car_model = models.ForeignKey(CarModel, on_delete = models.RESTRICT)
    description = models.TextField(max_length = 1000, help_text = "Some additonal info about the car")
    image_one = models.ImageField('Car Picture', upload_to='images/', null = True)

    def __str__(self):
        return f'{self.car_make} {self.car_model} {self.registration}'
    
    #reverse the object to generate a URL to the string output
    def get_absolute_url(self):
        #return a url to generate a detailed car record
        return reverse('car-detail', args=[str(self.id)])  

class CarOwner(models.Model):
    first_name = models.CharField('Firstame', max_length = 200, null=True, help_text ='Please enter your Firstname') 
    last_name = models.CharField('Lastame', max_length = 200, null=True, help_text ='Please enter your Lastname')
    email = models.EmailField( max_length = 30, null=True)
    car = models.ForeignKey(Car, on_delete = models.RESTRICT, null = True)
    information = models.TextField(max_length = 1000, help_text = "Some additonal information about you", null=True)
    image_one = models.ImageField('Car Picture', upload_to='images/', null = True)



    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.car}'
    
class carInstance(models.Model):
    """Model to represent a car instance"""

    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    car = models.ForeignKey('Car', on_delete = models.RESTRICT)
    imprint = models.CharField(max_length = 500)
    due_back = models.DateField(null = True, blank = True)

    hire_status = (
        ('a', 'Available'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
        ('m','Maintenance')
    )

    status = models.CharField(
        max_length =1,
        choices = hire_status,
        blank = True,
        default= 'a',
        help_text='Car Availability'
    )

    class Meta:
        ordering=['due_back']

    def __str__(self):
        return f'{self.id} {self.car}'  


         