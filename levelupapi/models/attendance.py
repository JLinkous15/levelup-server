from django.db import models

class Attendance(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="Attendees")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="Event_attendance")