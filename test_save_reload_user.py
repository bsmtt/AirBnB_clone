#!/usr/bin/python3
from models import storage
from models.city import City

 
my_model = City()
my_model.state_id = "state_id"
my_model.name = "name"

print("2=====")
city2 = City(**my_model.to_dict())
my_model.save()
 