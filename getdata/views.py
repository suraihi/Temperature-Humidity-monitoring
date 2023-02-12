from django.shortcuts import render
from getdata.models import sensors, tempdata,humidata,infradata, alarm
from django.http import HttpResponse,JsonResponse
import json
def save_data(request):
    sensorH = request.GET.get("sensorH")
    sensorT = request.GET.get("sensorT")
    sensorI = request.GET.get("sensorI")
    id1 = request.GET.get("id1")
    id2 = request.GET.get("id2")
    id3 = request.GET.get("id3")
    sensor_instance1 = sensors.objects.get(id=id1)
    sensor_instance2 = sensors.objects.get(id=id2)
    sensor_instance3 = sensors.objects.get(id=id3)

    ######




    ######

    Tempdata = tempdata()
    Humidata = humidata()
    Infradata = infradata()
   # Alarm = alarm()

    Tempdata.temperature = sensorT
    Humidata.humidity = sensorH
    Infradata.infra = sensorI
    Tempdata.sensor1 = sensor_instance1
    Humidata.sensor2 = sensor_instance2
    Infradata.sensor3 = sensor_instance3

    Tempdata.save()
    Humidata.save()
    Infradata.save()

    alarmdata = list(alarm.objects.values())


    infradatas = list(infradata.objects.values())
    infra_ids = list(map(lambda data: data['id'], infradatas))

    infid = infra_ids[-1]


    buzzer = list(map(lambda alarm: alarm['buzzer'], alarmdata))

   # datainstance2 = infradata.objects.get(time=id2)
    if (int(sensorI)) == 0 :
        if buzzer[-1] == False :
            Alarm = alarm()
            Alarm.data = infradata.objects.get(id=infid)
            Alarm.buzzer = True
            Alarm.save()

    if (int(sensorI)) > 0 :
        if buzzer[-1] == True :
            Alarm = alarm()
            Alarm.data = infradata.objects.get(id=infid)
            Alarm.buzzer = False
            Alarm.save()





    return HttpResponse("done")

def share_data(request):
    datashare = list(infradata.objects.values())


    #data2 = data.objects.all()
   # return render(request, 'show_graph.html', {'data2': data2})
    return JsonResponse(datashare,safe=False)
# Create your views here.



def show_graph(request,template_name='show_graph.html'):
    datasharet = list(tempdata.objects.values())
    datashareh = list(humidata.objects.values())
    datasharea = list(alarm.objects.values())
    temps = list(map(lambda data: data['temperature'], datasharet))
    humis = list(map(lambda data: data['humidity'], datashareh))
    buzs = list(map(lambda data: data['buzzer'], datasharea))

    id = list(map(lambda data: data['id'], datasharet))

    return render(request, 'show_graph.html', {'temps': json.dumps(temps),'humis': json.dumps(humis),'id': json.dumps(id),'buzs': json.dumps(buzs) })
    #return render(request,template_name,{'temps':temps,'humis':humis})

def live_graph(request,template_name='live_graph.html'):
    datashare = list(infradata.objects.values())
    temps = list(map(lambda data: data['temperature'], datashare))
    humis = list(map(lambda data: data['humidity'], datashare))
    id = list(map(lambda data: data['id'], datashare))
    lastT = temps[len(temps)-1]


    return render(request, 'live_graph.html', {'temps': json.dumps(temps),'humis': json.dumps(humis),'id': json.dumps(id),'lastT': json.dumps(lastT) })