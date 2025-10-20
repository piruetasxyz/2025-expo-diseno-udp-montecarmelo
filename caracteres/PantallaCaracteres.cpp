

#include "PantallaCaracteres.h"

// constructor
PantallaCaracteres::PantallaCaracteres() {
}

// destructor
PantallaCaracteres::~PantallaCaracteres() {}

void PantallaCaracteres::configurar() {
  PantallaCaracteres::lcd.init();
  PantallaCaracteres::lcd.backlight();
  PantallaCaracteres::mostrarMensaje();
}

void PantallaCaracteres::actualizar() {
  pos0 = pos0 + 1;
  pos1 = pos1 + 2;
  pos2 = pos2 + 3;
  pos3 = pos3 + 4;
  PantallaCaracteres::mostrarMensaje();
  // PantallaCaracteres::lcd.autoscroll();
  // PantallaCaracteres::lcd.scrollDisplayLeft();
  // PantallaCaracteres::lcd.shiftIncrement();
  delay(500);
}

void PantallaCaracteres::mostrarMensaje() {
  PantallaCaracteres::lcd.clear();

  PantallaCaracteres::lcd.setCursor(
    PantallaCaracteres::pos0, 0);
  PantallaCaracteres::lcd.print(
    PantallaCaracteres::linea0);

  PantallaCaracteres::lcd.setCursor(pos1, 1);
  PantallaCaracteres::lcd.print(
    PantallaCaracteres::linea1);

  PantallaCaracteres::lcd.setCursor(pos2, 2);
  PantallaCaracteres::lcd.print(
    PantallaCaracteres::linea2);

  PantallaCaracteres::lcd.setCursor(pos3, 3);
  PantallaCaracteres::lcd.print(
    PantallaCaracteres::linea3);
}