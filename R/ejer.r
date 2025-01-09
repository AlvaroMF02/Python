# Generar datos simulados
x <- rnorm(50)  # 50 valores aleatorios de una distribución normal
y <- rnorm(50)  # 50 valores aleatorios de otra distribución normal

# Crear un gráfico de dispersión
plot(x, y, main = "Gráfico de Dispersión", xlab = "Eje X", ylab = "Eje Y", col = "blue", pch = 19)
