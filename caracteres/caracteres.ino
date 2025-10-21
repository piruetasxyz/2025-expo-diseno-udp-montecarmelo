#include "PantallaCaracteres.h"
#include "Preguntas.h"
// #include "Respuestas.h"

PantallaCaracteres pantallita;

void setup() {

  pantallita.configurar();
  pantallita.cargarLinea(0, preguntas[0].texto);
  pantallita.cargarLinea(1, preguntas[1].texto);
  pantallita.cargarLinea(2, preguntas[2].texto);
  pantallita.cargarLinea(3, preguntas[3].texto);
}

void loop() {

  if (random(100) < 1 * 100 / 4) {
    pantallita.moverIzquierda(0);
  } else if (random(100) < 2 * 100 / 4) {
    pantallita.moverIzquierda(1);
  } else if (random(100) < 3 * 100 / 4) {
    pantallita.moverIzquierda(2);
  } else {
    pantallita.moverIzquierda(3);
  }


  // pantallita.moverIzquierda(1);
  // pantallita.moverIzquierda(2);
  // pantallita.moverIzquierda(3);
  // if (random(100) > 90) {
  //   Serial.println(random(100));
  //   pantallita.moverIzquierda(random(4));
  // }

  // pantallita.actualizar();
  pantallita.mostrarMensaje();
}
