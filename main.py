import time
import random
import pandas as pd
import matplotlib.pyplot as plt

def funcion_lineal(array,objetivo): 
  lista = []

  for i in range(len(array)):
    menor = 0 
    mayor = 0
    menor = objetivo - array[i]
    mayor = objetivo +  array[i]

    if (array[i] == objetivo and 0 in array and [array[i],0] not in lista):
      lista.append([0, array[i]])

    if (array[i] < objetivo and menor in array and [array[i],menor] not in lista):
      lista.append([menor, array[i]])

    if (array[i] > objetivo and mayor in array and [array[i],mayor] not in lista):
      lista.append([mayor, array[i]])

  return (lista)

def funcion_constante(lista, resultado):
    if len(lista) <= 1:
        return "La lista debe tener al menos dos elementos para formar parejas."

    parejas = []
    inicio = 0
    fin = len(lista) - 1

    while inicio < fin:
        suma_actual = lista[inicio] + lista[fin]

        if suma_actual == resultado:
            parejas.append((lista[inicio], lista[fin]))
            inicio += 1
            fin -= 1
        elif suma_actual < resultado:
            inicio += 1
        else:
            fin -= 1

    if not parejas:
        return "No es posible organizar en parejas para obtener el resultado deseado."

    return parejas

def funcion_fuerza_bruta(lista, num):
  parejas = []
  for i in range(len(lista)):
    for j in range(len(lista)-1):
      if lista[i] + lista[j+1] == num and (lista[i], lista[j+1]) not in parejas:
        parejas.append((lista[i], lista[j+1]))
  return parejas


def dividir_vencer(nums, target):
    pairs = []

    def dp(index, remaining, path):
        if remaining == 0 and len(path) == 2:
            pairs.append(path)
            return
        if index >= len(nums) or remaining < 0 or len(path) >= 2:
            return

        # Caso 1: No utilizar el número actual
        dp(index + 1, remaining, path)

        # Caso 2: Utilizar el número actual
        dp(index + 1, remaining - nums[index], path + [nums[index]])

    dp(0, target, [])

    return pairs

def main():
    n = [10, 100, 1000, 10000]
    tiempos = {'funcion_constante': [], 'funcion_fuerza_bruta':[], 'dividir_vencer':[], 'funcion_lineal':[] }

    for i in n:
        nums = [random.randint(1, 5) for _ in range(i)]  # Generar lista de números aleatorios
        target = -1

        start = time.perf_counter()
        funcion_constante(nums, target)
        end = time.perf_counter()
        dif = end - start
        tiempos['funcion_constante'].append(dif)

        start = time.perf_counter()
        funcion_fuerza_bruta(nums, target)
        end = time.perf_counter()
        dif = end - start
        tiempos['funcion_fuerza_bruta'].append(dif)

        
        start = time.perf_counter()
        funcion_fuerza_bruta(nums, target)
        end = time.perf_counter()
        dif = end - start
        tiempos['dividir_vencer'].append(dif)

        start = time.perf_counter()
        funcion_fuerza_bruta(nums, target)
        end = time.perf_counter()
        dif = end - start
        tiempos['funcion_lineal'].append(dif)

    print("Tiempos de ejecución para funcion_constante:")
    for i, tipo in zip(n, tiempos['funcion_constante']):
        print(f"{i} -> {tipo} segundos")

    print("Tiempos de ejecución para funcion_fuerza_bruta:")
    for i, tipo in zip(n, tiempos['funcion_fuerza_bruta']):
        print(f"{i} -> {tipo} segundos")

    print("Tiempos de ejecución para funcion_fuerza_bruta:")
    for i, tipo in zip(n, tiempos['dividir_vencer']):
        print(f"{i} -> {tipo} segundos")

    print("Tiempos de ejecución para funcion_fuerza_bruta:")
    for i, tipo in zip(n, tiempos['funcion_lineal']):
        print(f"{i} -> {tipo} segundos")

    df = pd.DataFrame(tiempos, index=n)
    df.index.name = 'n'
    df.reset_index(inplace=True)

    plt.plot(df['n'], df['funcion_constante'], label='funcion_constante')
    plt.plot(df['n'], df['funcion_fuerza_bruta'], label='funcion_fuerza_bruta')
    plt.plot(df['n'], df['dividir_vencer'], label='dividir_vencer')
    plt.plot(df['n'], df['funcion_lineal'], label='funcion_lineal')
    plt.xlabel('n')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución para funcion_constante y funcion_fuerza_bruta')
    plt.legend()

    plt.savefig("ejercicio2.png")
    plt.show()
    
main()