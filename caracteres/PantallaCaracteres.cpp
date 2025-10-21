

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

void PantallaCaracteres::cargarPregunta(int nuevaLinea, Pregunta nuevaPregunta) {
  if (nuevaLinea == 0) {
    PantallaCaracteres::linea0 = nuevaPregunta.texto;
  } else if (nuevaLinea == 1) {
    PantallaCaracteres::linea1 = nuevaPregunta.texto;
  } else if (nuevaLinea == 2) {
    PantallaCaracteres::linea2 = nuevaPregunta.texto;
  } else if (nuevaLinea == 3) {
    PantallaCaracteres::linea3 = nuevaPregunta.texto;
  }
}

void PantallaCaracteres::moverIzquierda(int linea) {
  if (linea == 0) {
    pos0 = pos0 + 1;
  } else if (linea == 1) {
    pos1 = pos1 + 1;
  } else if (linea == 2) {
    pos2 = pos2 + 1;
  } else if (linea == 3) {
    pos3 = pos3 + 1;
  }
  PantallaCaracteres::mostrarMensaje();
  delay(PantallaCaracteres::pausa);
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
  delay(PantallaCaracteres::pausa);
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