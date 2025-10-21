#include "PantallaCaracteres.h"
#include "Preguntas.h"

PantallaCaracteres pantallita;

void setup() {

  pantallita.configurar();
  pantallita.cargarPregunta(0, preguntas[0]);
  pantallita.cargarPregunta(1, preguntas[1]);
  pantallita.cargarPregunta(2, preguntas[2]);
  pantallita.cargarPregunta(3, preguntas[3]);
}

void loop() {

  if (random(100) > 50) {
    pantallita.moverIzquierda(random(4));
  }

  // pantallita.actualizar();
}
