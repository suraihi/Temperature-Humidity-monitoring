# **Temperature-Humidity-monitoring**

## Tech Turtules 
### Group Member
1. Hassan Fahmy 
2. Ahmed Amer
3. Abdullah Elsuruhi


# 1.0 Problem Statment
There’s a delicate balance when it comes to your indoor space’s temperature and humidity levels. Ideally, your indoor air will vary between 20ºC to 25ºC, and 30% to 50% relative humidity.

Indoor environments that are too hot can lead to a variety of health risks, including heat exhaustion, heat stroke, and feelings of lethargy. In fact, the difference between 20ºC and 28ºC can result in a 15% decline in workplace productivity. In extreme cases, sustained exposure to extreme heat can lead to increased illnesses and hospitalization. On the other hand, a space that’s too cold can result in higher blood pressure, asthma, and poor mental health. Viruses are also more likely to survive and spread in cool, dry indoor conditions.

In addition to viral infections and respiratory illnesses, an overly dry environment can also contribute to skin problems, nosebleeds, and sore throats. But increase the humidity in a building, and your space will become damp. This can make it susceptible to mold, which is often associated with breathing issues.

As climate change persists, it’s more important than ever for landlords and business owners to consider the impacts of seasonal heat waves and cold fronts in order to keep their tenants and employees safe. Electronic equipment, exterior building construction, window composition, lack of airflow, and certain industrial practices may also play a part into your space’s temperature and humidity levels.

Most buildings don’t have the ability to widely track temperature and humidity, with readings being confined to a single heating zone. A system that includes a temperature and humidity monitor can help you uncover areas that are too hot, cold, or humid in more detail. This can help you prevent your occupants from being exposed to dangerous indoor environments that could lead to serious health issues. Above 25ºC and 50% moisture can cause serious heat illnesses, cognitive impairment, and mold.Below 20ºC and 30% moisture can impact mental health, viral survivability, and blood pressure. S we are going to implement IOT System that can track Tempreture And Humidity and Display them on DashBoard, this DashBoard will be updated continuously as we will use Cloud Platform


# 2.0 System Arctitecture 

This section present an overview of the system architecture of IoT Temperature-Humidity-monitoring system 
our system architecture will be divided on three main sections
- Sensor and device
- Cloud platform using Django Rest Framework and Python Everywhere
- Dashboard

![image](https://user-images.githubusercontent.com/117296912/220284808-d7cac4b4-5ad4-4e85-8529-be5c7bdb6d45.png)

# 3.0 Sensors
-  ESP32


 ![image](https://user-images.githubusercontent.com/117296912/220287244-e1f1b117-0457-4925-9b8e-abe97c576d78.png)

-  Tempreture and Humidity Sensor (DHT22)


![image](https://user-images.githubusercontent.com/117296912/220287560-3a289079-3253-42a0-b4fc-02eea6a4e418.png)

## Sensors OverView


![image](https://user-images.githubusercontent.com/117296912/220292150-c8a5a636-2e2e-4ede-9e5d-18a7ee88a7e1.png)





# 4.0 Cloud Platform

Cloud Platform
In order to transfer data between all the hardware components and people smart phones, we need to set up a cloud platform. We will update the cloud platform in real time data as the Tempreture and Humidity Changes. We also need to get the data from the cloud platform and present them to the people in our Dashboard. 
A server is created using Django with pythonanywhere host. As we learnt from stage one, we created a new unique server for our project using ubuntu. Django in pythonanywhere was a great option. Then we will push the server project files into GITHUB to share and edit them all together  
To send our web pages online we need to use one of the hosting providers online, PythonAnywhere is a great one.

![image](https://user-images.githubusercontent.com/117296912/220292241-2ad28915-db23-4de4-8a9e-4dbe1b018044.png)




# 5.0 DashBoard

The Tempreture and Humidity Monitoring Dashboad is connected to the ESP32 IoT Device through the intermediate cloud interface. There are one cluster of dashboard meant to provide monitoring to 2 variables that is Tempreture and Humidity and fire detection. Each variable come with a chart that will collect and display the data overtime to provide better grasp on the evironment of the plant. for fire detection it check the tempeture and check if it is too high so give alarm of fire and set fire to True, if not set fire to false

![image](https://user-images.githubusercontent.com/117296912/220290265-29fe70ad-70f3-471f-9047-ef43ed5d52e7.png)




