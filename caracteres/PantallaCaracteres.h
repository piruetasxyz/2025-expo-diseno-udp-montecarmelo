#ifndef PANTALLA_CARACTERES_H
#define PANTALLA_CARACTERES_H

#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>


class PantallaCaracteres {

public:
  // constructor
  PantallaCaracteres();

  // destructor
  ~PantallaCaracteres();

  void configurar();

  void actualizar();

  void mostrarMensaje();

  uint8_t direccion = 0x27;
  uint8_t columnas = 20;
  uint8_t filas = 4;

  String linea0 = "discusiones";
  String linea1 = "contemporaneas";
  String linea2 = "del";
  String linea3 = "diseno";

  uint8_t pos0 = 0;
  uint8_t pos1 = 0;
  uint8_t pos2 = 0;
  uint8_t pos3 = 0;

  LiquidCrystal_I2C lcd = LiquidCrystal_I2C(
    direccion,
    columnas,
    filas);
};

#endif