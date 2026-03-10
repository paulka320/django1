from django.db import models

# Create your models here.
class Teachers(models.Model):
    FirstName = models.CharField(max_length = 100)
    SecondName = models.CharField(max_length =100)
    Subject = models.CharField(max_length =100)
    email = models.EmailField()
    
    def __str__(self):
        print(f"FirstName":{self.FirstName})
        print(f"SecondName":{self.SecondName})
        print(f"Subject":{self.Subject})
        print(f"Email":{self.email})
    
    
class Students(models.Model):
    FirstName =models.CharField(max_length=100)
    SecondName = models.CharField(max_length=100)
    StudyYear = models.IntegerField()
    
    def __str__(self):
        print(f"FirstName":{self.FirstName})
        print(f"SecondName":{self.SecondName})
        print(f"Year of Study":{self.StudyYear})