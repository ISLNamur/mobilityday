from django.contrib import admin

from .models import SchoolMobilityModel, StudentMobilityModel, TransportationMobilityModel, MeetingMobilityModel

admin.site.register(SchoolMobilityModel)
admin.site.register(StudentMobilityModel)
admin.site.register(TransportationMobilityModel)
admin.site.register(MeetingMobilityModel)
