#include "Respuesta.h"

Respuesta::Respuesta(int numero, String texto) {
  Respuesta::numero = numero;
  Respuesta::texto = "                 ";
  Respuesta::texto += "Pregunta ";
  Respuesta::texto += String(numero);
  Respuesta::texto += ". ";
  Respuesta::texto += texto;
}

Respuesta::~Respuesta() {}