# caracteres

## Bill of materials

Pantalla LCD Verde 20x04 2004 con i2c

<https://afel.cl/products/pantalla-lcd-verde-20x04-2004-con-i2c>

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

Las pantallas sin modificaciones están en la dirección 0x27

Veamos las otras direcciones cuando se sueldan A0, A1 o A2.

Soldado A0: 0x26

Soldado A1: 0x25

Soldado A2: 0x23

## Cableado

 Arduino A4 a SDA (Datos) y A5 a SCL (Clock), más GND y alimentación. Vamos con el programa.

This library allows an Arduino board to control LiquidCrystal displays (LCDs) based on the Hitachi HD44780 (or a compatible) chipset, which is found on most text-based LCDs. The library works with in either 4- or 8-bit mode (i.e. using 4 or 8 data lines in addition to the rs, enable, and, optionally, the rw control lines).

Cable rojo a 5V

Cable verde a GND

Cable blanco a A4 SDA

Cable azul a A5 SCL

## Código
