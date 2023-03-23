from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class BaseModel(models.Model):
#     created_at= models.DateTimeField(auto_now_add=True)
#     updated_at= models.DateTimeField(auto_now=True)
#     created_by= models.ForeignKey(
#         User, 
#         related_name="%(class)s_createdby", 
#         on_delete=models.CASCADE, 
#         null=True 
#     )
#     updated_by= models.ForeignKey(
#         User, 
#         related_name="%(class)s_updatedby", 
#         on_delete=models.CASCADE, 
#         null=True, 
#     )

#     class Meta: 
        # abstract=True 

class Emp(models.Model):
    emp_id= models.IntegerField( primary_key=True)
    emp_name= models.CharField(max_length=100, null=False)
    salary= models.IntegerField(null=False)
    dep_id= models.IntegerField(default=True, null=False)
    

    def __str__(self) -> str:
        return self.emp_name