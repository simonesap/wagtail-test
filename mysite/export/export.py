from blog.models import *

obj = Author.objects.all() 
print(obj)

# for o in obj:
#     name = p[0]
#     surname = p[1]
#     date_of_birthday = p[2]
#     return

# print(name)
    

name = Author.objects.all()[0].name




