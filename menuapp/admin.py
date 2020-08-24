from django.contrib import admin

from menuapp.models import VegIndian,NonvegIndian,VegChinese,NonvegChinese

admin.site.register(VegIndian)
admin.site.register(NonvegIndian)
admin.site.register(VegChinese)
admin.site.register(NonvegChinese)

# Register your models here.
