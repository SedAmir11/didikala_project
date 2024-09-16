from django.contrib import admin
from app_social.models import point, is_Useful, comment, image



@admin.register(point)
class pointAdmin(admin.ModelAdmin):
    pass

@admin.register(is_Useful)
class is_Usefuln(admin.ModelAdmin):
    pass

@admin.register(comment)
class commentmin(admin.ModelAdmin):
    pass

@admin.register(image)
class imageAdmin(admin.ModelAdmin):
    pass



