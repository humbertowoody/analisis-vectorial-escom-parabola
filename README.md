# Graficación de una Parábola a un punto de impacto

Este programa toma un punto de impacto definido por el usuario (x,y) así como una altura máxima y calcula la ecuación paramétrica que describe la parábola así como grafica y muestra dicha gráfica en un espacio tridimensional.

## Análisis del problema

Los datos que conocemos:

- `Xf`: La coordenada `x` del punto de impacto.
- `Yf`: La coordenada `y` del punto de impacto.
- `hmax`: La altura máxima de la parábola.

Para resolver el problema se plantean las siguientes ecuaciones paramétricas para cada una de las dimensiones del espacio, en este caso: tres:

- `x = at^2 + bt + c`
- `y = dt^2 + et + f`
- `z = gt^2 + ht + i`

Conocemos tres puntos de nuestra parábola: el orígen `(0,0,0)`, el punto máximo `(Xf/2, Yf/2, hmax)` y el punto de impacto `(Xf, Yf, 0)`, por lo que podemos obtener sus ecuaciones iniciales parametrizadas , siendo:

- Orígen `(0,0,0)`:
  - `x = 0 = at^2 + bt + c`
  - `y = 0 = dt^2 + et + f`
  - `z = 0 = gt^2 + ht + i`
- Punto Máximo `(Xf/2,Yf/2,hmax)`:
  - `x = (Xf/2) = at^2 + bt + c`
  - `y = (Yf/2) = dt^2 + et + f`
  - `z = hmax = gt^2 + ht + i`
- Punto de Impacto `(0,0,0)`:
  - `x = Xf = at^2 + bt + c`
  - `y = Yf = dt^2 + et + f`
  - `z = 0 = gt^2 + ht + i`

Reordenando en sistemas de ecuaciones lineales:

- Coeficientes `a`, `b` y `c`:
  - `x = 0 = at^2 + bt + c`
  - `x = (Xf/2) = at^2 + bt + c`
  - `x = Xf = at^2 + bt + c`
- Coeficientes `e`, `d` y `f`:
  - `y = 0 = dt^2 + et + f`
  - `y = (Yf/2) = dt^2 + et + f`
  - `y = Yf = dt^2 + et + f`
- Coeficientes `g`, `h` y `i`:
  - `z = 0 = gt^2 + ht + i`
  - `z = 0 = gt^2 + ht + i`
  - `z = hmax = gt^2 + ht + i`

En cada uno sustituiremos `t` por las componentes `i`  de cada vector, en este caso: `0`, `Xf/2`y `Xf`. Se resuelve el sistema de ecuaciones y con eso obtendremos los resultados para los coeficientes: `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h` e `i` con los cuales podremos formar la ecuación paramétrica que describe la curva de la siguiente forma:

- `(x(t), y(t), z(t))`

La cual podemos reescribir como:

- `(at^2 + bt + c, dt^2 + et + f, gt^2 + ht + i)`

Dicha ecuación puede ser ingresada _directamente_ en algún software de graficación como GeoGebra (o similares) para visualizar la gráfica y manipularla de manera dinámica.

El programa mostrará una graficación simple dónde se muestra el punto de impacto determinado por el usuario así como la curva resultante que satisface dicha ecuación paramétrica.

## Tecnologías

- Python
- Librerías:
  - `matplotlib`
  - `numpy`

## Dependencias

Para instalar las dependencias:

`$ pip install -r requirements.txt`

## Ejecución

Para ejecutar el programa:

`$ python main.py`

Deberán introducir los siguientes datos de entrada:

- Coordenada x del punto de impacto: Un número real cualquiera.
- Coordenada y del punto de impacto: Un número real cualquiera.
- Altura máxima del tiro parabólico.

## Créditos

Este programa fué realizado para la materia Análisis Vectorial de la Escuela Superior de Cómputo del Instituto Politécnico Nacional impartida por el Dr. Dárwin Gutiérrez Mejía.

Alumno: *Humberto Alejandro Ortega Alcocer*

Mayo 2021