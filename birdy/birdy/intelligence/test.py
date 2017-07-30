import wikipedia
from birdy.models import Bird

a = Bird.objects.all()

for i in a:
    b = wikipedia.page(i.name)
    i.url = b.url
