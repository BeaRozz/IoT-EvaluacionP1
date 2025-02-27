# IoT-EvaluacionP1
Repositorio para la Evaluación del Parcial 1 de la materia de IoT. Envío de datos a ThingSpeak con Raspberry Pico W

## Descripción del Proyecto:
Este es un proyecto simple hecho con MicroPython para la lectura y envío de datos con una LM35 y una Raspberry Pi Pico W. Igualmente, la visualización y procesamiento de datos con ThingSpeak y MathWork.

## Requisitos:
- Protoboard y jumpers.
- Sensor LM35.
- Raspberry Pi Pico W.
- Cuenta en ThingSpeak y MathWorks.

## Instalación:
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/mi-proyecto.git
   ```  
2. Copia el archivo `main.py` (que se encuentra en src/Raspberry_code) a tu dispositivo que corre MicroPython.

## Uso
### 1. Raspberry
  Usar los archivos en `src/Raspberry_code`.
  1. Conecta tu dispositivo y para ejecutar el archivo `main.py`.
  2. Cambiar los valores solicitados en el script (SSID, PASSWORD y THINGSPEAK_API_KEY).
  3. Ejecutar el código, que deberá resultar en algo parecido a la siguiente imagen:
     <img src="https://raw.githubusercontent.com/BeaRozz/IoT-EvaluacionP1/refs/heads/main/Evidencia/2-C%C3%B3digo%20funcionando.jpg"> <br>
  Con esto ya estaremos enviando datos y pasamos a la configuración en ThingSpeak.
### 2. ThingSpeak
  Usar los archivos en `src/MatLab_code`.
  1. Dentro de ThingSpeak, en la cinta de menú ir a Apps->MATHLab Analysis.
  2. Hacer clic en "New" y pega el código de `Send_email.m`
     1. Cambiar el alertApiKey por el proporcionado en ThingSpeak en My Profile -> Alerts API Key.
     2. En la parte inferior, en la opción React configurar para que en cada inserción de datos ejecute el script si se escribe un valor de más de 35.
  4. Hacer clic en "New" y pega el código de `Average.m`
     1. Cambiar los valores del canal y APIWrite y APIRead.
     2. En la parte inferior, en la opción TimeControl configurar para que se ejecute el script cada 30 minutos (es decir que se recolectaron 10 datos).

## Descripción de carpetas:
/IOT-EvaluacionP1<br>
├── Evidencia             # Carpeta con imágenes de evidencia<br>
├── /src                  # Código fuente<br>
│   ├── /MatLab_code         # Carpeta con código de MathLab<br>
│       ├── Average.m          # Cáluculo del promedio y envío<br>
│       ├── Send_email.m       # Envío de email<br>
│   ├── /Raspberry_code      # Carpeta con código para la Raspeberry<br>
│       ├── main.py            # Lectura de LM35 y envío de datos<br>
├── .gitignore            # Archivos a ignorar por Git<br>
└── README.md             # Archivo de lectura<br>
