#include <Arduino.h>
#include "PantallaCaracteres.h"

// constructor
PantallaCaracteres::PantallaCaracteres() {
  for (int i = 0; i < PantallaCaracteres::columnas; i++) {
    PantallaCaracteres::lineaMostrar0 += " ";
    PantallaCaracteres::lineaMostrar1 += " ";
    PantallaCaracteres::lineaMostrar2 += " ";
    PantallaCaracteres::lineaMostrar3 += " ";
  }
}

// destructor
PantallaCaracteres::~PantallaCaracteres() {}

void PantallaCaracteres::configurar() {
  PantallaCaracteres::lcd.init();
  PantallaCaracteres::lcd.backlight();
  PantallaCaracteres::lcd.noAutoscroll();
  PantallaCaracteres::lcd.clear();

  // PantallaCaracteres::mostrarMensaje();
}


void PantallaCaracteres::cargarLinea(int linea, String nuevoTexto) {
  if (linea == 0) {
    PantallaCaracteres::linea0 = nuevoTexto;
  } else if (linea == 1) {
    PantallaCaracteres::linea1 = nuevoTexto;
  } else if (linea == 2) {
    PantallaCaracteres::linea2 = nuevoTexto;
  } else if (linea == 3) {
    PantallaCaracteres::linea3 = nuevoTexto;
  }
}

void PantallaCaracteres::moverIzquierda(int linea) {
  if (linea == 0) {
    PantallaCaracteres::pos0 += 1;
    PantallaCaracteres::pos0 = PantallaCaracteres::pos0 % PantallaCaracteres::linea0.length();
    PantallaCaracteres::lineaMostrar0 = PantallaCaracteres::linea0.substring(pos0);
    if (PantallaCaracteres::lineaMostrar0.length() < PantallaCaracteres::columnas) {
      PantallaCaracteres::lineaMostrar0 = PantallaCaracteres::rellenarConEspacios(lineaMostrar0);
    } else {
      PantallaCaracteres::lineaMostrar0 = PantallaCaracteres::lineaMostrar0.substring(0, PantallaCaracteres::columnas);
    }
  } else if (linea == 1) {
    PantallaCaracteres::pos1 += 1;
    PantallaCaracteres::pos1 = PantallaCaracteres::pos1 % PantallaCaracteres::linea1.length();
    PantallaCaracteres::lineaMostrar1 = PantallaCaracteres::linea1.substring(pos1);
    if (PantallaCaracteres::lineaMostrar1.length() < PantallaCaracteres::columnas) {
      PantallaCaracteres::lineaMostrar1 = PantallaCaracteres::rellenarConEspacios(lineaMostrar1);
    } else {
      PantallaCaracteres::lineaMostrar1 = PantallaCaracteres::lineaMostrar1.substring(0, PantallaCaracteres::columnas);
    }
  } else if (linea == 2) {
    PantallaCaracteres::pos2 += 1;
    PantallaCaracteres::pos2 = PantallaCaracteres::pos2 % PantallaCaracteres::linea2.length();
    PantallaCaracteres::lineaMostrar2 = PantallaCaracteres::linea2.substring(pos2);
    if (PantallaCaracteres::lineaMostrar2.length() < PantallaCaracteres::columnas) {
      PantallaCaracteres::lineaMostrar2 = PantallaCaracteres::rellenarConEspacios(lineaMostrar2);
    } else {
      PantallaCaracteres::lineaMostrar2 = PantallaCaracteres::lineaMostrar2.substring(0, PantallaCaracteres::columnas);
    }
  } else if (linea == 3) {
    PantallaCaracteres::pos3 += 1;
    PantallaCaracteres::pos3 = PantallaCaracteres::pos3 % PantallaCaracteres::linea3.length();
    PantallaCaracteres::lineaMostrar3 = PantallaCaracteres::linea3.substring(pos3);
    if (PantallaCaracteres::lineaMostrar3.length() < PantallaCaracteres::columnas) {
      PantallaCaracteres::lineaMostrar3 = PantallaCaracteres::rellenarConEspacios(lineaMostrar3);
    } else {
      PantallaCaracteres::lineaMostrar3 = PantallaCaracteres::lineaMostrar3.substring(0, PantallaCaracteres::columnas);
    }
  }
  // PantallaCaracteres::lcd.scrollDisplayLeft();

  PantallaCaracteres::mostrarMensaje();
  delay(PantallaCaracteres::pausa);
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
  delay(PantallaCaracteres::pausa);
}

void PantallaCaracteres::mostrarMensaje() {
  PantallaCaracteres::lcd.clear();

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
  String resultado = original;
  while (original.length() <= PantallaCaracteres::columnas) {
    resultado = resultado + " ";
  }
  return resultado;
}