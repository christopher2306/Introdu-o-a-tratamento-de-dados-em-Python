#visualizando dados
#tabela basica

import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

x2 = [2, 4, 6, 8, 10]
y2 = [4, 8, 12, 16, 20]

titulo = "Gráfico de barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label="Grupo 1")
plt.bar(x2, y2, label="Grupo 2")
plt.legend()

plt.show()



