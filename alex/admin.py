from django.contrib import admin

from alex.models import *

admin.site.register(SiteUser)
admin.site.register(Contact)
admin.site.register(Article)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Rev)

