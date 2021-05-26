# Graficación de una Parábola a un punto de impacto

Este programa toma un punto de impacto definido por el usuario (x,y) así como una altura máxima y calcula la ecuación paramétrica que describe la parábola así como grafica y muestra dicha gráfica en un espacio tridimensional.

## Análisis del problema

Para resolver el problema se plantean las siguientes ecuaciones paramétricas para cada uno de las dimensiones del espacio:

- `x = at^2 + bt + c`
- `y = dt^2 + et + f`
- `z = gt^2 + ht + i`

Sabemos tres puntos de nuestra parábola, el orígen, el punto máximo y el punto de impacto, por lo que podemos plantear tres sistemas de ecuaciones distintos y en cada uno sustituiremos `t` por las componentes `i`  de cada vector.

Al resolver los sistemas de ecuaciones, obtendremos los resultados para los coeficientes: `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h` e `i` con los cuales podremos formar la ecuación paramétrica que describe la curva de la siguiente forma:

- `(x(t), y(t), z(t))`

La cual podemos reescribir como:

- `(at^2 + bt + c, dt^2 + et + f, gt^2 + ht + i)`

Dicha ecuación puede ser ingresada _directamente_ en algún software de graficación como GeoGebra (o similares) para visualizar la gráfica y manipularla de manera dinámica.

El programa mostrará una graficación simple dónde se muestra el punto de impacto determinado por el usuario así como la parábola resultante que satisface dicha ecuación paramétrica.

## Tecnologías

- Python
- Librerías:
  - `matplotlib`
  - `numpy`

## Dependencias

Para instalar las dependencias basta con ejecutar:

`$ pip install -r requirements.txt`

## Ejecución

Para ejecutar el programa basta con usar:

`$ python main.py`

Deberá introducir los siguientes datos de entrada:

- Coordenada x del punto de impacto: Un número real cualquiera.
- Coordenada y del punto de impacto: Un número real cualquiera.
- Altura máxima del tiro parabólico.

## Créditos

Este programa fue realizado para la materia Análisis Vectorial de la Escuela Superior de Cómputo del Instituto Politécnico Nacional impartida por el Dr. Dárwin Gutiérrez Mejía.

Alumno: *Humberto Alejandro Ortega Alcocer*

Mayo 2021