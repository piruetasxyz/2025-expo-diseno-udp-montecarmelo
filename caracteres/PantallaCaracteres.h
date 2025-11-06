#ifndef PANTALLA_CARACTERES_H
#define PANTALLA_CARACTERES_H

#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>


class PantallaCaracteres {

private:
  LiquidCrystal_I2C lcd;

public:
  // constructor
  PantallaCaracteres(uint8_t direccion, int columnas, int filas): lcd(direccion, columnas, filas) {}

  // destructor
  ~PantallaCaracteres();

  void configurar(uint8_t direccion);

  void cargarTexto(String nuevoTexto);

  void actualizar();

  void mostrarMensaje();

  String rellenarConEspacios(String original);

  uint8_t direccion = 0x25;
  int columnas = 20;
  int filas = 4;

  String lineaMostrar0 = "";
  String lineaMostrar1 = "";
  String lineaMostrar2 = "";
  String lineaMostrar3 = "";

  String linea0 = "discusiones";
  String linea1 = "contemporaneas";
  String linea2 = "del";
  String linea3 = "diseno";

  int pos0 = 0;
  int pos1 = 0;
  int pos2 = 0;
  int pos3 = 0;

  int pausa = 10;

  // Cunas cunas;

  // LiquidCrystal_I2C lcd = LiquidCrystal_I2C(
  //   direccion,
  //   columnas,
  //   filas);
};

#endif