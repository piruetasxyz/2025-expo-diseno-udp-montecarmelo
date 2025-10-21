#include "PantallaCaracteres.h"
#include "Preguntas.h"
#include "Respuestas.h"

PantallaCaracteres pantallita;

void setup() {

  pantallita.configurar();
  pantallita.cargarLinea(0, preguntas[0].texto);
  // pantallita.cargarLinea(1, preguntas[1].texto);
  // pantallita.cargarLinea(2, preguntas[2].texto);
  // pantallita.cargarLinea(3, preguntas[3].texto);
}

void loop() {

  pantallita.moverIzquierda(0);
  // if (random(100) > 90) {
  //   Serial.println(random(100));
  //   pantallita.moverIzquierda(random(4));
  // }

  // pantallita.actualizar();
  pantallita.mostrarMensaje();
}
