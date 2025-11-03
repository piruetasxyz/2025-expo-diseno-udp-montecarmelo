# caracteres

## Apuntes

Con esta pantalla LCD 2004 con interfaz I2C y controlador interno HD44780, podrás mostrar datos en formato alfanumérico de manera clara y nítida, lo que le añadirá un toque más profesional a tus proyectos. Además, esta pantalla es muy útil para hacer debugging o para hacer correcciones en distintos proyectos, especialmente en el manejo de sensores y el procesamiento de datos.

El controlador interno HD44780 es un chip de control de pantalla muy utilizado y para el que hay mucha información disponible, lo que la hace fácil de usar y soportar. Para trabajar con esta pantalla, debes conectar los pines correctamente. El bus de comunicación es paralelo y puede trabajar a 4 bits o 8 bits, aunque lo más común es trabajar a 4 bits. Si quieres ahorrar pines, también puedes usar un adaptador de bus paralelo a serial I2C (incluido), lo que te permitirá trabajar con un solo puerto I2C.

Algunas de las características más importantes de esta pantalla son:

Voltaje de operación: 5V
Interfaz: paralelo, 4 bits o 8 bits
Color de texto: negro
Backlight: verde
Filas: 4
Columnas: 20
Interfaz i2c soldado a la pantalla

<https://naylampmechatronics.com/blog/34_tutorial-lcd-conectando-tu-arduino-a-un-lcd1602-y-lcd2004.html>

<https://naylampmechatronics.com/blog/35_tutorial-lcd-con-i2c-controla-un-lcd-con-solo-dos-pines.html>

<https://www.prometec.net/bus-i2c/>

## Conexiones I2C

En esta web encontramos un tutorial sobre cómo escanear y encontrar direcciones i2c

<https://learn.adafruit.com/scanning-i2c-addresses/arduino>
