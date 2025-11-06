#include "PantallaCaracteres.h"
#include "Cunas.h"

// ejes pueden valer 1, 2, 3
// numeroArduino puede valer 1, 2, 3

// pantalla 1 no esta soldada
// pantalla 2 tiene soldada A0
// pantalla 3 tiene soldada A1
// pantalla 4 tiene soldada A2

const int eje = 1;
const int numeroArduino = 1;

const uint8_t direccion1 = 0x27;
const uint8_t direccion2 = 0x26;
const uint8_t direccion3 = 0x25;
const uint8_t direccion4 = 0x23;

const int ancho = 20;
const int alto = 4;

PantallaCaracteres pantalla1 = PantallaCaracteres(direccion1, ancho, alto);
PantallaCaracteres pantalla2 = PantallaCaracteres(direccion2, ancho, alto);
PantallaCaracteres pantalla3 = PantallaCaracteres(direccion3, ancho, alto);
PantallaCaracteres pantalla4 = PantallaCaracteres(direccion4, ancho, alto);

Cunas cunas;

void setup() {


  pantalla1.configurar(direccion1);
  pantalla2.configurar(direccion2);
  pantalla3.configurar(direccion3);
  pantalla4.configurar(direccion4);

  // cunas.textos[eje][numeroArduino]
  if (numeroArduino == 1) {
    pantalla1.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 0]);
    pantalla2.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 1]);
    pantalla3.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 2]);
  } else if (numeroArduino == 2) {
    pantalla1.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 3]);
    pantalla2.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 4]);
    pantalla3.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 5]);
  } else if (numeroArduino == 3) {
    pantalla1.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 6]);
    pantalla2.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 7]);
    pantalla3.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 8]);
    pantalla4.cargarTexto(cunas.textos[eje - 1][numeroArduino - 1 + 9]);
  }
}

void loop() {

  pantalla1.mostrarMensaje();
  pantalla2.mostrarMensaje();
  pantalla3.mostrarMensaje();
  pantalla4.mostrarMensaje();
  // pausa de un minuto
  delay(1000 * 60);
}
