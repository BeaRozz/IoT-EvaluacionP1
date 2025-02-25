# Importación de librerías
import network
import urequests
import utime
import machine

#Declaramos el Pin donde conectamos el LM35
adc = machine.ADC(26)

# Configuración de la red WiFi
SSID = "Nombre_de_la_Red"
PASSWORD = "Contraseña_de_la_Red"

# Datos de ThingSpeak
THINGSPEAK_API_KEY = "WRITE_API_KEY"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Inicializar la conexión WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    utime.sleep(2)


# Función para enviar datos a ThingSpeak
def enviar_a_thingspeak(valor):
    try:
        # Construir la URL con el valor a enviar
        url = f"{THINGSPEAK_URL}?api_key={THINGSPEAK_API_KEY}&field1={valor}"
        
        # Realizar la petición HTTP GET
        respuesta = urequests.get(url)
        
        # Cerrar la conexión
        respuesta.close()

    except Exception as e:
        print("Error al enviar datos:", str(e))

#Función para leer los datos del LM35
def leer_temperatura():
    
    #Leemos el valor del pin
    valor_adc = adc.read_u16()
    
    #Convertimos según los datos de conversión (resolución de 16 bits para hasta 3.3v)
    voltaje = (valor_adc / 65535) * 3.3
    
    #Multiplicamos por el factor indicado por el sensor 10mV/°C
    temperatura_celsius = (voltaje * 100)

    return temperatura_celsius


# Enviar datos cada 180 segundos, es decir, 3 minutos
while True:
    temp = leer_temperatura() #Lee la temperatura
    enviar_a_thingspeak(temp) #Envía los datos
    utime.sleep(180)  # Esperar 180 segundos antes del próximo envío