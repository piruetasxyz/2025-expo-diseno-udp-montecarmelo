#ifndef RESPUESTA_H
#define RESPUESTA_H

#include <Arduino.h>

class Respuesta {
public:
  Respuesta(int numero, String texto);
  ~Respuesta();

  String texto;
  int numero;
};

#endif