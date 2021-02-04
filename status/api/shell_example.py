

from django.utils.six import BytesIO

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from status.api.serializers import StatusSerializer
from status.models import Status


'''
Serialize a  obj
'''
obj = Status.objects.first()

serializer = StatusSerializer(obj)

serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)


'''
Serialize a  queryset
'''

qs = Status.objects.all()

serializer2 = StatusSerializer(obj,many = True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)



stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)

print(data2)





"""
 create dat
"""
data = {'user':1}

serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save()

# if serializer.is_valid():
#     serializer.save()



"""
 update data
 """
obj = Status.objects.first()
data = {'content': 'some new content ', 'user':1}
update_serializer = StatusSerializer(data=data)
update_serializer.is_valid()
update_serializer.save()

"""
 delete  data
 """

obj = Status.objects.first()
data = {'content': 'PLEASE delete me ', 'user':1}
create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
create_obj =create_obj_serializer.save()

print(create_obj)

data = {'id':9}
update_serializer = StatusSerializer(data=data)
update_serializer.is_valid()
update_serializer.save()

obj = Status.objects.last()
get_data_sarializer = StatusSerializer(obj)

print(get_data_sarializer.data)




data = {'user':1,'content': 'PLEASE delete me '}
update_serializer = StatusSerializer(data=data)
update_serializer.is_valid()
update_serializer.save()
