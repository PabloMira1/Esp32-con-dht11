import machine , network , time , urequests 
from machine import Pin
from time import sleep
import ubinascii
import dht

ssid = 'FLIA MIRA'
password = 'PAEZBE2022'
url = "https://api.thingspeak.com/update?api_key=EMM0B64U1ISXOX3Y"

red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(ssid, password)
print('Conexión correcta')
#print(red.ifconfig())

# Our DHT Module
dht_sensor = dht.DHT11(Pin(22))
pin_02 = Pin(2, Pin.OUT)
pin_02.off()        #El LED debe estar inicialmente apagado
pin_12 = Pin(12, Pin.OUT)
pin_12.off()        #El LED debe estar inicialmente apagado

#declaracion de mensajes whatsapp
Aviso_Temperatura = "Aviso%20%2C%20cuidado%20la%20temperatura%20es%20mayor%20a%20la%20requerida"      #Aviso , cuidado la temperatura es mayor a la requerida
Aviso_Humedad = "Aviso%20%2C%20cuidado%20la%20Humedad%20es%20mayor%20a%20la%20requerida"      #Aviso , cuidado la Humedad es mayor a la requerida





def send_whatsapp_message(message):
    url = 'https://api.callmebot.com/whatsapp.php?phone=+573024319814&text='+ message+'&apikey=1635832'
    response = urequests.get(url)
    print(response.text)  # Puedes mostrar la respuesta del servidor si lo deseas
    response.close()

while True:
        try:
             dht_sensor.measure()
             temperature = dht_sensor.temperature()
             humidity = dht_sensor.humidity()
             if str(temperature) > "23":
                 pin_02.on()
                 send_whatsapp_message(Aviso_Temperatura)
             else:
                 pin_02.off()       
                 
             if str(humidity) > "60":
                 pin_12.on()
                 send_whatsapp_message(Aviso_Humedad)
             else:
                 pin_12.off()
                 
             print(f"Temperatura:  {temperature:.2f}")
             print(f"Humedad:  {humidity:.2f}")
             respuesta = urequests.get(url + "&field1=" + str(temperature) + "&field2=" + str(humidity))
             #print ("Respuesta: " + str(respuesta.status_code))
             respuesta.close ()
             ultima_peticion = time.time()
             sleep(5)
        except OSError as e:
            print(e)
            #print("dht_sensor reading failed")
            





# Ejemplo de uso
send_email("Asunto del correo", "Cuerpo del correo", "pablomirab03@gmail.com")
