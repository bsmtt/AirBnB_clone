#!/usr/bin/python3
from models.user import User

my_model = User()
my_model.name = "My_First_Model" 
my_model.first_name = "999"
print(my_model.first_name) 
print("--")
my_model_json = my_model.to_dict() 
my_model.save()
print("--")
my_new_model = User(**my_model_json)
print(my_new_model.first_name) 
 
my_new_model.save()