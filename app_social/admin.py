from django.contrib import admin
from app_social.models import Comment , Advantage , Disadvantage , image



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    pass

@admin.register(Disadvantage)
class DisadvantageAdmin(admin.ModelAdmin):
    pass

@admin.register(image)
class imageAdmin(admin.ModelAdmin):
    pass



