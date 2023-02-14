from django.db import models
from models import Gamer, Event

class Attendance(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="Attendees")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="Event_attendance")