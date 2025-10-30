#ifndef TEXTO_H
#define TEXTO_H

#include <Arduino.h>

class Texto {
public:
  Texto(int numero, String texto);
  ~Texto();

  void mostrarTexto(int eje, int numero);

  void agregarTextoEje1(int textos[]);
  void agregarTextoEje2(int textos[]);
  void agregarTextoEje3(int textos[]);

  String texto;
  int numero;

  // respuestas segun eje
  int textosEje1[];
  int textosEje2[];
  int textosEje3[];
};

#endif