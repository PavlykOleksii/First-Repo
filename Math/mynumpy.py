import numpy as np

# # Створюємо матрицю 3×4
# A = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12]])


# print("Матриця A:")
# print(A)
# print(f"\nРозмірність: {A.shape[0]} рядків × {A.shape[1]} стовпців")

# # У Python індекси на 1 менше
# print(f"a(1,1) = {A[0, 0]}")   # 1
# print(f"a(2,3) = {A[1, 2]}")   # 7
# print(f"a(3,2) = {A[2, 1]}")   # 10


# # Перший рядок (всі стовпці)
# print(f"Перший рядок: {A[0, :]}")

# # Другий стовпець (всі рядки)
# print(f"Другий стовпець: {A[:, 1]}")

# # Перший рядок як матриця 1×4
# row_matrix = A[[0], :]
# print(f"Перший рядок (як матриця): {row_matrix}")
# print(f"Форма: {row_matrix.shape}")

# # Другий стовпець як матриця 3×1
# col_matrix = A[:, [1]]
# print(f"\nДругий стовпець (як матриця):\n{col_matrix}")
# print(f"Форма: {col_matrix.shape}")

# import numpy as np

# # Dataset: 5 людей, 3 ознаки (зріст, вага, вік)*

# data = np.array([
#     [170, 70, 25],  # людина 0*
#     [165, 60, 30],  # людина 1*
#     [180, 80, 22],  # людина 2*
#     [175, 75, 28],  # людина 3*
#     [160, 55, 35]   # людина 4*
# ])

# print("Dataset:")
# print(data)
# print(f"\nРозмірність: {data.shape[0]} зразків (людей) × {data.shape[1]} ознак")

# # Дані про першу людину перший рядок*
# print(f"Перша людина: {data[0, :]}")
# print(f"  Зріст: {data[0, 0]} см")
# print(f"  Вага: {data[0, 1]} кг")
# print(f"  Вік: {data[0, 2]} років")

# # Зріст всіх людей перший стовпець*
# heights = data[:, 0]
# print(f"\nЗріст всіх людей: {heights}")
# print(f"Середній зріст людини: {heights.mean():.1f} см")

# # Вага кожної людини другий стовпець*
# weights = data[:, 1]
# print(f"\nВаги кожної людини: {weights}")
# print(f"Середня вага людини: {weights.mean():.1f} кг")

# import numpy as np

# # Створюємо матрицю 3×2
# A = np.array([[1, 2],
#               [3, 4],
#               [5, 6]])

# print("Оригінальна матриця A (3×2):")
# print(A)

# # Транспонуємо
# A_T = A.T

# print("\nТранспонована A^T (2×3):")
# print(A_T)

# print(f"\nРозмірність A: {A.shape}")
# print(f"Розмірність A^T: {A_T.shape}")
# import numpy as np

# # Матриці з прикладу
# A = np.array([[1, 2, 3],
#               [4, 5, 6]]) # 2×3

# B = np.array([[7, 8],
#             [9, 10],
#             [11, 12]])  # 3×2

# # Множення A @ B
# C = A @ B

# print("Матриця A (2×3):")
# print(A)
# print("\nМатриця B (3×2):")
# print(B)
# print(f"\nРезультат C = A @ B ({C.shape[0]}×{C.shape[1]}):")
# print(C)

# import numpy as np

# # Матриця, у якій другий рядок — це подвоєний перший
# A = np.array([
#     [1, 2, 3],
#     [2, 4, 6],
#     [1, 1, 1]
# ])

# print("Матриця A:")
# print(A)
# print(f"\n Розмір матриці: {A.shape[0]} * {A.shape[1]}")

# rank = np.linalg.matrix_rank(A)
# print(f"Ранг матриці: {rank}")

# import numpy as np

# # П'ятивимірний вектор
# w = np.array([1, -2, 3, 0, 4])
# norm_w = np.linalg.norm(w)
# print(f"\n" + f"Вектор w = {w}")
# print(f"Норма ||w|| = {norm_w:.2f}")

# # Дві точки на площині (координати)
# A = np.array([1, 2])
# B = np.array([4, 6])

# # Відстань = норма вектора різниці
# distance = np.linalg.norm(B - A)

# print(f"Точка A: {A}", f"Точка B: {B}")
# print(f"Вектор B - A: {B - A}")
# print(f"Відстань d(A, B) = ||B - A|| = {distance}")

# Координати міст (широта, довгота) - звісно спрощено
# cities = np.array([
#     [50.45, 30.52],   # Київ
#     [48.29, 25.94],   # Чернівці
#     [49.84, 24.03],   # Львів
#     [46.48, 30.73],   # Одеса
#     [49.99, 36.23]    # Харків
# ])

# city_names = ['Київ', 'Чернівці', 'Львів', 'Одеса', 'Харків']

# # Наша поточна позиція де-не-будь в районі Вінниці ;)
# P = np.array([49.23, 28.47])

# print(f"Поточна локація P: {P}")
# print("\n" + "Відстані до міст:")

# # Обчислюємо відстані до всіх міст
# distances = []

# for i, city_coords in enumerate(cities):
#     dist = np.linalg.norm(city_coords - P)
#     distances.append(dist)
#     print(f"  {city_names[i]}: {dist:.2f}")

# # Знаходимо найближче місто
# nearest_idx = np.argmin(distances)

# print("\n" + f"Найближче місто: {city_names[nearest_idx]}")
# print(f"Відстань: {distances[nearest_idx]:.2f}")

import numpy as np

v = np.array([3, -4])

# Евклідова
norm_L2 = np.linalg.norm(v)
# або явно з параметром ord=2 np.linalg.norm(v, ord=2)

# Мангеттенська
norm_L1 = np.linalg.norm(v, ord=1)

# Максимуму
norm_Linf = np.linalg.norm(v, ord=np.inf)

print(f"Вектор: v = {v}")
print("\n" + f"Евклідова норма: {norm_L2}")
print(f"Мангеттенська норма: {norm_L1}")
print(f"Норма максимуму: {norm_Linf}")
