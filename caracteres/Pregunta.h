#ifndef PREGUNTA_H
#define PREGUNTA_H

#include <Arduino.h>

class Pregunta {
public:
  Pregunta(int numero, String texto);
  ~Pregunta();

  String texto;
  int numero;
};

#endif