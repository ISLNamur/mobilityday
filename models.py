import uuid

from django.db import models


class SchoolMobilityModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MeetingMobilityModel(models.Model):
    meeting = models.IntegerField(primary_key=True, unique=True)
    track = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TransportationMobilityModel(models.Model):
    transport = models.CharField(max_length=100)

    def __str__(self):
        return self.transport


class StudentMobilityModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    school = models.ForeignKey(SchoolMobilityModel, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    classe = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    by_bike = models.BooleanField(default=True)
    address_start = models.CharField(max_length=200, blank=True, null=True)
    no_meeting = models.BooleanField(default=False)
    custom_return = models.BooleanField(default=False)
    modality_return = models.CharField(max_length=200, blank=True, null=True)
    meeting_point = models.ForeignKey(MeetingMobilityModel, on_delete=models.CASCADE, blank=True, null=True)
    contact_return = models.CharField(max_length=200, blank=True, null=True)
    contact_phone_return = models.CharField(max_length=20, blank=True, null=True)
    transportation = models.ForeignKey(TransportationMobilityModel, on_delete=models.CASCADE, blank=True, null=True)
