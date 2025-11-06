#ifndef CUNAS_H
#define CUNAS_H

#include <Arduino.h>

class Cunas {
public:
  Cunas();
  ~Cunas();
  String textos[3][10] = {
    { "El diseno especulativo ensaya futuros que cuestionan lo existente",
      "De que sirve la interdisciplina en el diseno y por que es valioso incorporarla?",
      "Que entendemos por creacion en diseno?",
      "En diseno, los resultados pueden ser sistemas mas que productos finales",
      "Los procesos que generamos son el resultado mas alla de un producto determinado",
      "Los procesos generan sentido mas alla del objeto final",
      "Integrar lo tecnologico y lo ecologico exige pensar mas alla de lo humano",
      "La cultura hacker nos plantea que la tecnologia es un lugar en constante disputa",
      "No solo consumimos tecnologia, sino que la tecnologia transforma nuestras vidas",
      "Que particularidades tienen las practicas que se gestan en America Latina?" },
    {
      "Toda forma es memoria de decisiones tecnicas y culturales pasadas",
      "El reciclaje estetico del pasado debilita toda funcion utopica",
      "Una cultura que recicla el pasado anula el potencial utopico del diseno",
      "Como podemos hacernos cargo de aquello que aparece como marginalidad del diseno?",
      "Como podemos establecer limites en el diseno? Donde empieza y donde termina?",
      "Disenar con otros implica reconocer su saber y capacidad creativa",
      "No se trata solo de disenar objetos o servicios, sino de disenar mundos",
      "El diseno se vuelve medio para afirmar identidades y formas de vida",
      "El diseno es clave para crear futuros justos, sostenibles y comunes",
      "Como activar desde el diseno una imaginacion politica transformadora?",
    },
    { "Que tipo de educacion en arte, arquitectura y diseno se necesita en Chile?",
      "El diseno no es solo disciplina, es una actividad esencial de la vida humana",
      "Disenar es transformar el mundo y, con ello, las formas de humanidad",
      "Al disenar objetos, transformamos el mundo y lo que significa ser humano",
      "Si bien el diseno se presenta como al servicio del humano, tiene como ambicion redisenarlo",
      "Como el diseno moldea nuestras conductas, deseos y formas de habitar?",
      "Necesitamos tecnologias situadas, fuera de la hegemonia del norte global",
      "Disenar tecnologias desde el sur global es clave para pensar otros futuros",
      "Como podriamos, desde el diseno, proponer nuevas maneras de entender la tecnologia?",
      "La tecnologia no es neutra, es politica" }

  };
};

#endif