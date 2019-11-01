from django.contrib import admin
from .models import Product
from .models import Cart
from .models import Person
from .models import Post
from .models import Profile
from .models import Hotel

admin.site.register(Product)

admin.site.register(Cart)

admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Hotel)

