from django.db import models

# Create your models here.
# Creating Company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT', 'IT'),
                                                  ('Non IT', 'Non IT'),
                                                  ('Mobile Phones', 'Mobile Phones')
                                                  ))
    added_date = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

#Employee Model
class Employee(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    about=models.TextField()
    Position=models.CharField(max_length=50, choices=(
        ('Manager', 'manager'),
        ('Software Developer', 'Sd'),
        ('Project Manager', 'pm')
    ))

    company=models.ForeignKey(Company, on_delete=models.CASCADE)