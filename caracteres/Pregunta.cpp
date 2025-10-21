#include "Pregunta.h"

Pregunta::Pregunta(int numero, String texto) {
  Pregunta::numero = numero;
  Pregunta::texto = "                 ";
  Pregunta::texto += "Pregunta ";
  Pregunta::texto += String(numero);
  Pregunta::texto += ". ";
  Pregunta::texto += texto;
}

Pregunta::~Pregunta() {}

void Pregunta::agregarRespuestasEje1(int respuestas[]) {

  for (int i = 0; i < sizeof(respuestas) / sizeof(respuestas[0]); i++) {}
}
void Pregunta::agregarRespuestasEje2(int respuestas[]) {}
void Pregunta::agregarRespuestasEje3(int respuestas[]) {}