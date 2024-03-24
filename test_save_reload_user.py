#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

 
new = BaseModel()
temp = {}
temp.update(storage.all())
print(temp[new.to_dict()['__class__'] +
                        '.' + new.id])
print(temp)
new.save()
 