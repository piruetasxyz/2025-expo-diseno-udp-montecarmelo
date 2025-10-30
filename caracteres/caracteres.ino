#include "PantallaCaracteres.h"
// #include "Preguntas.h"
// #include "Texto.h"
// #include "Respuestas.h"

PantallaCaracteres izquierda;
PantallaCaracteres centro;
PantallaCaracteres derecha;

uint8_t direccionIzquierda = 0x26;
uint8_t direccionCentro = 0x25;
uint8_t direccionDerecha = 0x23;

void setup() {

  izquierda.configurar(direccionIzquierda);
  centro.configurar(direccionCentro);
  derecha.configurar(direccionDerecha);



  // izquierda.cargarLinea(0, preguntas[0].texto);
  // izquierda.cargarLinea(1, preguntas[1].texto);
  // izquierda.cargarLinea(2, preguntas[2].texto);
  // izquierda.cargarLinea(3, preguntas[3].texto);

  // centro.cargarLinea(0, preguntas[0].texto);
  // centro.cargarLinea(1, preguntas[1].texto);
  // centro.cargarLinea(2, preguntas[2].texto);
  // centro.cargarLinea(3, preguntas[3].texto);

  // derecha.cargarLinea(0, preguntas[0].texto);
  // derecha.cargarLinea(1, preguntas[1].texto);
  // derecha.cargarLinea(2, preguntas[2].texto);
  // derecha.cargarLinea(3, preguntas[3].texto);
}

void loop() {

  if (random(100) < 1 * 100 / 4) {
    izquierda.moverIzquierda(0);
    centro.moverIzquierda(0);
    derecha.moverIzquierda(0);

  } else if (random(100) < 2 * 100 / 4) {
    izquierda.moverIzquierda(1);
    centro.moverIzquierda(1);
    derecha.moverIzquierda(1);

  } else if (random(100) < 3 * 100 / 4) {
    izquierda.moverIzquierda(2);
    centro.moverIzquierda(2);
    derecha.moverIzquierda(2);

  } else {
    izquierda.moverIzquierda(3);
    centro.moverIzquierda(3);
    derecha.moverIzquierda(3);
  }

  // pantallita.actualizar();
  izquierda.mostrarMensaje();
  centro.mostrarMensaje();
  derecha.mostrarMensaje();
}
