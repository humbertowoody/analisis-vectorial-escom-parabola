# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

# Entradas del usuario.
xf = float(input("Coordenada x final: "))
yf = float(input("Coordenada y final: "))
hmax = float(input("Altura máxima: "))

# Planteamiento de matrices del sistema de ecuaciones lineales.
primerMatriz = np.array([
    [0, 0, 1],
    [(xf/2)**2, xf/2, 1],
    [xf**2, xf, 1]
])
segundaMatriz = np.array([
    [0, 0, 1],
    [(xf/2)**2, xf/2, 1],
    [xf**2, xf, 1]
])
tercerMatriz = np.array([
    [0, 0, 1],
    [(xf/2)**2, xf/2, 1],
    [xf**2, xf, 1]
])

# Términos independientes para nuestro sistema de ecuaciones lineales.
terminosIndependientes1 = np.array([0, xf/2, xf])
terminosIndependientes2 = np.array([0, yf/2, yf])
terminosIndependientes3 = np.array([0, hmax, 0])

# Cálculo de las soluciones de los sistemas 3x3
solucionesX = np.linalg.solve(primerMatriz, terminosIndependientes1)
solucionesY = np.linalg.solve(segundaMatriz, terminosIndependientes2)
solucionesZ = np.linalg.solve(tercerMatriz, terminosIndependientes3)

# Imprimir en la terminal la ecuación paramétrica de la parábola resultante.
print("Ecuación paramétrica:")
print(f"({solucionesX[0]:.2f}t²+{solucionesX[1]:.2f}t+{solucionesX[2]:.2f}, {solucionesY[0]:.2f}t²+{solucionesY[1]:.2f}t+{solucionesY[2]:.2f}, {solucionesZ[0]:.2f}t²+{solucionesZ[1]:.2f}t+{solucionesZ[2]:.2f})")

# Creamos la figura de Matplotlib
fig = plt.figure()

# Creamos la gráfica
ax = fig.add_subplot(projection='3d')

# Creamos los ejes.
xx, yy = np.meshgrid(range(20), range(20))

# Creamos el rango de valores para t
t_line = np.linspace(0, 10, 100)

# Planteamos las ecuaciones paramétricas en función de t
x_line = (solucionesX[0] * (t_line ** 2)) + \
    (solucionesX[1] * t_line) + solucionesX[2]
y_line = (solucionesY[0] * (t_line ** 2)) + \
    (solucionesY[1] * t_line) + solucionesY[2]
z_line = (solucionesZ[0] * (t_line ** 2)) + \
    (solucionesZ[1] * t_line) + solucionesZ[2]

# Añadimos el punto de impacto
punto = ax.plot([xf], [yf], [0], markerfacecolor='k',
                markeredgecolor='k', marker='o', markersize=5, alpha=0.6)

# Añadimos las ecuaciones paramétricas a nuestra gráfica en 3D
curva = ax.plot3D(x_line, y_line, z_line,
                  label='Curva Paramétrica', color="red")

# Colocamos los límites de graficación en los ejes.
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 15)
ax.set_zlim(-1, 15)

# Colocamos las etiquetas en los ejes.
ax.set_xlabel('x', color='blue')
ax.set_ylabel('y', color='blue')
ax.set_zlabel('z', color='blue')

# Colocamos el título de la gráfica
ax.set_title("Curva Paramétrica de Tiro Parabólico")

# Proxies para colores de la leyenda.
proxy_grafica = plt.Rectangle((0, 0), 1, 1, fc='r')
proxy_punto = plt.Line2D(
    [0], [0], linestyle="none", marker='o', alpha=0.6, markersize=10, markerfacecolor='black')

# Mostrar la leyenda
ax.legend([proxy_grafica, proxy_punto], [f"({solucionesX[0]:.2f}t²+{solucionesX[1]:.2f}t+{solucionesX[2]:.2f}, {solucionesY[0]:.2f}t²+{solucionesY[1]:.2f}t+{solucionesY[2]:.2f}, {solucionesZ[0]:.2f}t²+{solucionesZ[1]:.2f}t+{solucionesZ[2]:.2f})",
          f"Impacto ({xf:.2f},{yf:.2f},0)"], numpoints=1, loc='lower left')


# Mostramos la gráfica
plt.show()
