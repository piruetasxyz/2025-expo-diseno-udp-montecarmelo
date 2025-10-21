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