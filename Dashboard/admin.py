from django.contrib import admin

from .models import WorkPackage, TestPackage

# Register your models here.
# admin.site.register(BadRating)
admin.site.site_header = "MLA Projekt"
admin.site.site_title = "MLA"
admin.site.index_title = "Welcome to Your MLA Portal"

class WorkPackageAdmin(admin.ModelAdmin):
    # ...
    list_display = ["kpi", "rg_area", "recipient", "recipient_rating"]
    readonly_fields = ('recipient_rating', 'performer_rating', 'pub_date')

#admin.site.register(TestPackage, WorkPackageAdmin)
admin.site.register(WorkPackage, WorkPackageAdmin)