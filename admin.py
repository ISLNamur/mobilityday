from django.contrib import admin

from .models import SchoolMobilityModel, StudentMobilityModel, TransportationMobilityModel, MeetingMobilityModel


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'track', 'name',)


class StudentMobilityAdmin(admin.ModelAdmin):
    list_display = ('school', 'last_name', 'first_name', 'meeting_point',)


admin.site.register(SchoolMobilityModel)
admin.site.register(StudentMobilityModel, StudentMobilityAdmin)
admin.site.register(TransportationMobilityModel)
admin.site.register(MeetingMobilityModel, MeetingAdmin)
