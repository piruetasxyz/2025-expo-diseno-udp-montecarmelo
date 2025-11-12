#include "PantallaCaracteres.h"
#include "Cunas.h"

// 11 OK
// 12 
// 13 OK
// 21 OK
// 22 OK
// 23 OK
// 31 OK
// 32 OK
// 33 OK

// eje puede ser 1, 2, 3
// numeroArduino puede ser 1, 2, 3

// pantalla 1 no esta soldada
// pantalla 2 tiene soldada A0
// pantalla 3 tiene soldada A1
// pantalla 4 tiene soldada A2

const int eje = 3;
const int numeroArduino = 2;

const uint8_t direccion1 = 0x27;
const uint8_t direccion2 = 0x26;
const uint8_t direccion3 = 0x23;
const uint8_t direccion4 = 0x25;

const int ancho = 20;
const int alto = 4;

PantallaCaracteres pantalla1 = PantallaCaracteres(direccion1, ancho, alto);
PantallaCaracteres pantalla2 = PantallaCaracteres(direccion2, ancho, alto);
PantallaCaracteres pantalla3 = PantallaCaracteres(direccion3, ancho, alto);
// PantallaCaracteres pantalla4 = PantallaCaracteres(direccion4, ancho, alto);

Cunas cunas;

void setup() {

  pantalla1.configurar(direccion1);
  pantalla2.configurar(direccion2);
  pantalla3.configurar(direccion3);
  // pantalla4.configurar(direccion4);

  // cunas.textos[eje][numeroArduino]

  pantalla1.cargarTexto(cunas.textos[eje - 1][3 * (numeroArduino - 1) + 0]);
  pantalla2.cargarTexto(cunas.textos[eje - 1][3 * (numeroArduino - 1) + 1]);
  pantalla3.cargarTexto(cunas.textos[eje - 1][3 * (numeroArduino - 1) + 2]);
}

void loop() {
  pantalla1.mostrarMensaje();
  pantalla2.mostrarMensaje();
  pantalla3.mostrarMensaje();
  // pantalla4.mostrarMensaje();
  // pausa de un minuto
  delay(1000 * 60);
}
