from django.db import models

class sensors(models.Model):
    sensorname =  models.CharField(max_length=255)
    sensordatatype =  models.CharField(max_length=255)
    sensormodel =  models.CharField(max_length=255)


class tempdata(models.Model):
    time = models.DateTimeField(auto_now_add=True)

    sensor1 = models.ForeignKey(sensors, on_delete=models.CASCADE)
    temperature = models.FloatField()

class humidata(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    sensor2 = models.ForeignKey(sensors, on_delete=models.CASCADE)
    humidity = models.FloatField()


class infradata(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    sensor3 = models.ForeignKey(sensors, on_delete=models.CASCADE)
    infra = models.FloatField()




class alarm(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    data=  models.ForeignKey(infradata, on_delete=models.CASCADE)
    buzzer = models.BooleanField()




