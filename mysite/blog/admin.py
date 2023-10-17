from django.contrib import admin
from .models import Post
# Register your models here.
# Customizing models are displayed in admin site interface
# admin.site.register(Post)
# Here the decorator  
# We are telling the Django Administration site the the model is regitered in the site
# using a custom class that inherits from ModelAdmin
# and we include in our custom class  information about how to display model on the site
# and how interat wit it 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display: an attribute allows us to set the fields of our model that we want 
    # to display in administration object page.
    list_display = ["title","slug","author","publish","status"]
    # Here more options:
    list_filter = ["status","created","publish","author"]
    search_fields = ['title','body']
    raw_id_fields = ['author']
    date_hierarchy = "publish"
    ordering = ["status","publish"]
    prepopulated_fields = {'slug':('title',)}