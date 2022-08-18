from django.db import models

# Create your models here.
 
class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Language(models.Model):
    name = models.CharField(max_length=50)
    creator= models.OneToOneField(Creator, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Frameworks(models.Model):
    name = models.CharField(max_length=50)
    creator= models.ForeignKey(Language, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class Developers(models.Model):
    name = models.CharField(max_length=50)
    creator= models.CharField(max_length=50)
    framework = models.ManyToManyField(Frameworks)
    
    def __str__(self):
        return self.name