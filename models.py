from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=4, decimal_places=2)
  availability = models.BooleanField(null=True)


class Client(models.Model):
  last_name = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  e_mail = models.EmailField(max_length=50)
  phone_number =models.IntegerField()
  
class credits_par_client(models.Model):
  fullname_client=models.CharField(max_length=50)
  email_client=models.EmailField(max_length=50)
  phonenumber_client=models.IntegerField()
  montant_total_credit =models.FloatField()
  montant_paye =models.FloatField()
  montant_restant =models.FloatField()
  # if montant_total_credit>montant_paye:
  #     montant_restant=montant_total_credit - montant_paye
  # else:
  #     montant_restant==0
    
  
  