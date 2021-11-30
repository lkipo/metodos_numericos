import optparse
import sympy as sp
from matplotlib import pyplot as plt

x, y = sp.symbols('x, y')

parser = optparse.OptionParser(description = 'Resolucion numerica dun problema de valor inicial utilizando o metodo Runge-Kutta de orde 4 (RK4). Exemplo de uso: python runge-kutta.py -n 15 -p 0.1 -x 0 -y 1 -d 3*x*y. Valores por defecto: numero = 10, paso = 0.1, inicial_x = 1, inicial_y = 1, derivada = 2*x*y')

parser.add_option('-n', '--numero', help = 'Numero de pasos nos que se desenvolvera o metodo', action = 'store')
parser.add_option('-p', '--paso', help = 'Tamaño do paso co que se iterará para obter as solucions numericas', action = 'store')
parser.add_option('-x', '--inicial_x', help = 'Valor X inicial', action = 'store')
parser.add_option('-y', '--inicial_y', help = 'Valor Y inicial', action = 'store')
parser.add_option('-d', '--derivada', help = 'Primeira derivada da solucion', action = 'store')
parser.set_defaults(numero = '10', paso = '0.1', inicial_x = '1', inicial_y = '1', derivada = '2*x*y')

options, arguments = parser.parse_args()


numero_pasos = eval(str(options.numero))
paso = eval(str(options.paso))
valor_inicial_x = eval(str(options.inicial_x))
valor_inicial_y = eval(str(options.inicial_y))
derivada = eval(str(options.derivada))

valores_x = []
valores_y = []

valores_x.append(valor_inicial_x)
valores_y.append(valor_inicial_y)

for i in range(numero_pasos):
    k1 = derivada.subs(x, valores_x[i]).subs(y, valores_y[i])
    k2 = derivada.subs(x, valores_x[i] + 0.5 * paso).subs(y, valores_y[i] + 0.5 * paso * k1)
    k3 = derivada.subs(x, valores_x[i] + 0.5 * paso).subs(y, valores_y[i] + 0.5 * paso * k2)
    k4 = derivada.subs(x, valores_x[i] + paso).subs(y, valores_y[i] + paso * k3)

    valores_y.append(valores_y[i] + paso/6 * (k1 + 2*k2 + 2*k3 + k4))
    valores_x.append(valores_x[i] + paso)

print('Valores de X: \t Valores de Y:')
for i in range(numero_pasos+1):
    print('%6f \t %6f' %(valores_x[i], valores_y[i]))  

fig, ax = plt.subplots()
ax.plot(valores_x, valores_y, label="Solucion numérica")
ax.legend()

plt.show()