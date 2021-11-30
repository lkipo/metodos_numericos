# metodos_numericos
Resolución de PVI con metodos de Euler/RK4

Instruccións de uso:

Executar en terminal. 
Parámetros: 
-n = numero de pasos
-p = tamaño do paso
-x = valor inicial da variable x
-y = valor inicial da variable y
-d = primeira derivada da solución, seguindo o criterio de signos utilizado en Python, é dicir
, suma +, resta -, multiplicación *, división /, potencias **.
En caso de conter caracteres especiais, introducilos cun \, por exemplo \(x+y-1\)**2
Valores por defecto: -n = 10, -p = 0.1, -x = 1, -y = 1, -d = 2*x*y

Exemplo de uso:
python runge-kutta.py -n 15 -p 0.1 -x 0 -y 1 -d 3*x*y
python euler.py -n 20 -p 0.05 -x 2 -y 1 -d x*y
