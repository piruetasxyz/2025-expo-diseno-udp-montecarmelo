#ifndef PREGUNTA_H
#define PREGUNTA_H

#include <Arduino.h>

class Pregunta {
public:
  Pregunta(int numero, String texto);
  ~Pregunta();

  void agregarRespuestasEje1(int respuestas[]);
  void agregarRespuestasEje2(int respuestas[]);
  void agregarRespuestasEje3(int respuestas[]);

  String texto;
  int numero;

  // respuestas segun eje
  int respuestasEje1[];
  int respuestasEje2[];
  int respuestasEje3[];
};

#endif