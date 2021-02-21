from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import MemePost, HashTags

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(MemePost)
admin.site.register(HashTags)
admin.site.site_header = "Xmeme"
