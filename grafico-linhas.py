#visualizando dados
#tabela basica

import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

x2 = [2, 4, 6, 8, 10]
y2 = [4, 8, 12, 16, 20]

titulo = "Gráfico de dispersão (pontos)"
eixox = "Eixo X"
eixoy = "Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x1, y1, label="Grupo 1", color="g", marker="h", s=100)

plt.plot(x1, y1)
plt.legend()

plt.savefig("Figura1.pdf")

plt.show()

