from django.contrib import admin
from .models import Class,Student,CustomUser


# Activate/Deactivate Student from Admin
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("class_name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user","first_name","last_name","status")
    actions = ["activate_students","deactivate_students"]

    def activate_students(self,request,queryset):
        queryset.update(status=True)
    activate_students.short_description = "Activate selected students"

    def deactivate_students(self,request,queryset):
        queryset.update(status=False)
    deactivate_students.short_description = "Deactivate selected students"


@admin.register(CustomUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ("phone",)