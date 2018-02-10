from django.db import models

class Ngo(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=30)
    about = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Event(models.Model):
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    event_name=models.CharField(max_length=250)
    event_about=models.CharField(max_length=500)
    event_date=models.DateField(null=True)
    event_time = models.TimeField(null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name + ' - ' + str(self.ngo)