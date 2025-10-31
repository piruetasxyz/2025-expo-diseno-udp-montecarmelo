#include "PantallaCaracteres.h"


uint8_t direccionIzquierda = 0x26;
uint8_t direccionCentro = 0x25;
uint8_t direccionDerecha = 0x23;

PantallaCaracteres izquierda = PantallaCaracteres(direccionIzquierda, 20, 4);
PantallaCaracteres centro = PantallaCaracteres(direccionCentro, 20, 4);
PantallaCaracteres derecha = PantallaCaracteres(direccionDerecha, 20, 4);


void setup() {


  izquierda.configurar(direccionIzquierda);
  centro.configurar(direccionCentro);
  derecha.configurar(direccionDerecha);

  izquierda.cargarTexto(izquierda.textos.textos[0][0]);
  centro.cargarTexto(centro.textos.textos[1][0]);
  derecha.cargarTexto(derecha.textos.textos[2][0]);

}

void loop() {

  // if (random(100) < 1 * 100 / 4) {
  //   // izquierda.moverIzquierda(0);
  //   // centro.moverIzquierda(0);
  //   // derecha.moverIzquierda(1);
  //   // izquierda.moverIzquierda(1);
  //   // centro.moverIzquierda(1);
  //   // derecha.moverIzquierda(1);
  //   // izquierda.moverIzquierda(2);
  //   // centro.moverIzquierda(2);
  //   // derecha.moverIzquierda(2);
  //   // izquierda.moverIzquierda(3);
  //   // centro.moverIzquierda(3);
  //   // derecha.moverIzquierda(3);
  // }

  // } else if (random(100) < 2 * 100 / 4) {
  //   izquierda.moverIzquierda(1);
  //   centro.moverIzquierda(1);
  //   derecha.moverIzquierda(1);

  // } else if (random(100) < 3 * 100 / 4) {
  //   izquierda.moverIzquierda(2);
  //   centro.moverIzquierda(2);
  //   derecha.moverIzquierda(2);

  // } else {
  //   izquierda.moverIzquierda(3);
  //   centro.moverIzquierda(3);
  //   derecha.moverIzquierda(3);
  // }

  // // pantallita.actualizar();
  izquierda.mostrarMensaje();
  centro.mostrarMensaje();
  derecha.mostrarMensaje();
}
