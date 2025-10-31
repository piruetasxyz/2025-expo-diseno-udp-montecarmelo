#include <Arduino.h>
#include "PantallaCaracteres.h"


// destructor
PantallaCaracteres::~PantallaCaracteres() {}

void PantallaCaracteres::configurar(uint8_t direccion) {


  for (int i = 0; i < PantallaCaracteres::columnas; i++) {
    PantallaCaracteres::lineaMostrar0 += " ";
    PantallaCaracteres::lineaMostrar1 += " ";
    PantallaCaracteres::lineaMostrar2 += " ";
    PantallaCaracteres::lineaMostrar3 += " ";
  }
  PantallaCaracteres::direccion = direccion;

  // PantallaCaracteres::lcd = LiquidCrystal_I2C(
  //   PantallaCaracteres::direccion,
  //   PantallaCaracteres::columnas,
  //   PantallaCaracteres::filas);

  PantallaCaracteres::lcd.init();
  PantallaCaracteres::lcd.backlight();
  PantallaCaracteres::lcd.noAutoscroll();
  PantallaCaracteres::lcd.clear();

  // PantallaCaracteres::mostrarMensaje();
}

void PantallaCaracteres::cargarTexto(String nuevoTexto) {

  int numCaracteres = nuevoTexto.length();

  PantallaCaracteres::lineaMostrar1 = " ";
  PantallaCaracteres::lineaMostrar2 = " ";
  PantallaCaracteres::lineaMostrar3 = " ";

  if (numCaracteres < 20) {
    PantallaCaracteres::lineaMostrar0 = nuevoTexto.substring(0, numCaracteres);
  } else {
    PantallaCaracteres::lineaMostrar0 = nuevoTexto.substring(0, 0 + 20);

    if (numCaracteres < 40) {
      PantallaCaracteres::lineaMostrar1 = nuevoTexto.substring(20, numCaracteres);
    } else {
      PantallaCaracteres::lineaMostrar1 = nuevoTexto.substring(20, 20 + 20);

      if (numCaracteres < 60) {
        PantallaCaracteres::lineaMostrar2 = nuevoTexto.substring(40, numCaracteres);
      } else {
        PantallaCaracteres::lineaMostrar2 = nuevoTexto.substring(40, 40 + 20);
        if (numCaracteres < 80) {
          PantallaCaracteres::lineaMostrar3 = nuevoTexto.substring(60, numCaracteres);
        } else {
          PantallaCaracteres::lineaMostrar3 = nuevoTexto.substring(60, 40 + 20);
        }
      }
    }
  }
}


void PantallaCaracteres::actualizar() {
  // pos0 = pos0 + 1;
  // pos1 = pos1 + 2;
  // pos2 = pos2 + 3;
  // pos3 = pos3 + 4;
  // PantallaCaracteres::mostrarMensaje();
  // PantallaCaracteres::lcd.autoscroll();
  // PantallaCaracteres::lcd.scrollDisplayLeft();
  // PantallaCaracteres::lcd.shiftIncrement();
  // delay(PantallaCaracteres::pausa);
}

void PantallaCaracteres::mostrarMensaje() {
  // PantallaCaracteres::lcd.clear();

  PantallaCaracteres::lcd.setCursor(0, 0);
  PantallaCaracteres::lcd.print(
    PantallaCaracteres::lineaMostrar0);


  PantallaCaracteres::lcd.setCursor(0, 1);
  PantallaCaracteres::lcd.print(
    PantallaCaracteres::lineaMostrar1);

  PantallaCaracteres::lcd.setCursor(0, 2);
  PantallaCaracteres::lcd.print(
    PantallaCaracteres::lineaMostrar2);

  PantallaCaracteres::lcd.setCursor(0, 3);
  PantallaCaracteres::lcd.print(
    PantallaCaracteres::lineaMostrar3);
}

String PantallaCaracteres::rellenarConEspacios(String original) {
  String resultado = original.substring(0);
  while (original.length() <= PantallaCaracteres::columnas) {
    resultado = resultado + " ";
  }
  return resultado;
}