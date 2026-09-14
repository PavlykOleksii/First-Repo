# import numpy as np

# # Система: 2x₁ + 3x₂ = 8
# #          x₁ - x₂ = 1

# A = np.array([
#     [2, 3],
#     [1, -1]
# ])

# b = np.array([8, 1])

# print("Матриця коефіцієнтів A:")
# print(A)
# print(f"Вектор правої частини b: {b}")

# # Розв'язуємо систему
# x = np.linalg.solve(A, b)

# print(f"Розв'язок системи x: {x}")
# print(f"  x₁ = {x[0]}")
# print(f"  x₂ = {x[1]}")

# # Перевірка: A @ x має дорівнювати b
# result = A @ x
# print(f"Перевірка A @ x = {result}")

# import numpy as np

# # Несумісна система
# A_inconsistent = np.array([
#     [1, 1],
#     [1, 1]
# ])

# b_inconsistent = np.array([2, 3])

# try:
#     x = np.linalg.solve(A_inconsistent, b_inconsistent)
#     print(f"Розв'язок: {x}")
# except np.linalg.LinAlgError as e:
#     print(f"Помилка: {e}")
#     print("Система не має розв'язку або матриця вироджена")

# import numpy as np

# # Система трьох рівнянь з трьома невідомими
# A_3d = np.array([
#     [1, 1, 1],
#     [2, -1, 1],
#     [1, 2, -1]
# ])
# b_3d = np.array([6, 3, 2])

# # Розв'язуємо систему
# x_sol_3d = np.linalg.solve(A_3d, b_3d)
# print(f"Розв'язок системи 3×3:")
# print(f"  x₁ = {x_sol_3d[0]:.2f}")
# print(f"  x₂ = {x_sol_3d[1]:.2f}")
# print(f"  x₃ = {x_sol_3d[2]:.2f}")

# # Перевірка
# print(f"\\nПеревірка: A @ x = {A_3d @ x_sol_3d}")
# print(f"Має дорівнювати b = {b_3d}")

# import numpy as np

# # Система 4 рівняння, 4 невідомих
# A_4d = np.array([
#     [1, 2, -1, 3],
#     [2, -1, 1, 1],
#     [1, 1, 1, -1],
#     [3, 1, -2, 2]
# ])
# b_4d = np.array([5, 4, 6, 7])

# # Розв'язуємо
# x_sol_4d = np.linalg.solve(A_4d, b_4d)

# print(f"\\nРозв'язок:")
# for i, val in enumerate(x_sol_4d, 1):
#     print(f"  x_{i} = {val:.4f}")

# # Перевірка розв'язку
# residual = A_4d @ x_sol_4d - b_4d
# print(f"\\nПохибка: {np.linalg.norm(residual):.2e}")
# import numpy as np

# def analyze_system(A, b) -> dict:
#     """
#     Аналізує систему лінійних рівнянь Ax = b.
    
#     Returns:
#         dict: Словник з інформацією про ситуацію розв'язку:
#             - 'compatible': bool - чи сумісна система
#             - 'solution_type': 'unique' | 'infinite' | 'none'
#             - 'case_description': str - опис випадку
#             - 'rank_A': int - ранг матриці A
#             - 'rank_Ab': int - ранг розширеної матриці [A|b]
#             - 'n': int - кількість невідомих
#             - 'm': int - кількість рівнянь
#             - 'solution': Optional[np.ndarray] - розв'язок (якщо єдиний)
#     """
#     # Обчислюємо ранг матриці коефіцієнтів A
#     rank_A = np.linalg.matrix_rank(A)

#     # Створюємо розширену матрицю [A|b] і знаходимо її ранг
#     rank_Ab = np.linalg.matrix_rank(np.column_stack([A, b]))

#     # Кількість невідомих — це кількість стовпців у A
#     n = A.shape[1]
#     m = A.shape[0]  # кількість рівнянь

#     result = {
#         'rank_A': rank_A,
#         'rank_Ab': rank_Ab,
#         'n': n,
#         'm': m,
#         'compatible': False,
#         'solution_type': 'none',
#         'solution': None,
#         'case_description': ''
#     }

#     # Порівнюємо ранги згідно з критерієм Кронекера–Капеллі
#     if rank_A == rank_Ab:
#         result['compatible'] = True
        
#         if rank_A == n:
#             # Якщо rank(A) = n, то розв'язок єдиний
#             x = np.linalg.solve(A, b)
#             result['solution_type'] = 'unique'
#             result['solution'] = x
#             result['case_description'] = 'Сумісна визначена система - єдиний розвязок'
#         else:
#             # Якщо rank(A) < n, то розв'язків безліч
#             result['solution_type'] = 'infinite'
#             result['case_description'] = 'Сумісна система - нескінченно багато розвязків'
#     else:
#         # Якщо rank(A) < rank([A|b]), система несумісна
#         result['compatible'] = False
#         result['solution_type'] = 'none'
#         result['case_description'] = 'Несумісна система - розвязку немає'

#     return result

# A1 = np.array([
#     [2, 1, -1],
#     [1, 3, 2],
#     [3, -1, 1]
# ])
# b1 = np.array([8, 13, 5])

# result1 = analyze_system(A1, b1)
# print(result1['case_description'])
# if result1['solution'] is not None:
#     print("x =", result1['solution'])
# print()

# import numpy as np

# A = np.array([
#     [2, 1, -1],
#     [1, 3, 2],
#     [-1, 2, 1]
# ], dtype=float)

# det_A = np.linalg.det(A)
# print(f"\\nВизначник det(A) = {det_A:.4f}")

# if abs(det_A) > 1e-10:
#     print("Обернена матриця існує")
    
#     A_inv = np.linalg.inv(A)
#     print("\\nОбернена матриця:")
#     print(A_inv)
    
#     # Розв'язуємо систему
#     b = np.array([8, 13, 5])
#     x = A_inv @ b
    
#     print(f"\\nРозв'язок системи через обернену матрицю:")
#     print(f"x = {x}")
    
#     # Порівняємо з np.linalg.solve
#     x_solve = np.linalg.solve(A, b)
#     print(f"\\nРозв'язок через np.linalg.solve:")
#     print(f"x = {x_solve}")
    
#     print(f"\\nРізниця між методами: {np.linalg.norm(x - x_solve):.2e}")

import numpy as np
from scipy import linalg

# Матриця системи
A = np.array([
    [2, 1, -1],
    [4, -1, 2],
    [-2, 2, 1]
], dtype=float)

# Обчислюємо LU-розклад один раз
P, L, U = linalg.lu(A)

print("Нижня трикутна матриця L:")
print(L)
print("\\nВерхня трикутна матриця U:")
print(U)
print()

# Тепер можемо швидко розв'язувати системи для різних b
b = np.array([3, 13, 4], dtype=float)

print(f"Розв'язуємо Ax = b, де b = {b}")
print()

# Крок 1: Застосовуємо перестановку до b
Pb = P @ b
print(f"Після перестановки: Pb = {Pb}")

# Крок 2: Прямий хід - розв'язуємо Ly = Pb
y = linalg.solve_triangular(L, Pb, lower=True)
print(f"Після прямого ходу: y = {y}")

# Крок 3: Зворотний хід - розв'язуємо Ux = y
x = linalg.solve_triangular(U, y, lower=False)
print(f"Розв'язок: x = {x}")
print()

# Перевірка
print(f"Перевірка: Ax = {A @ x}")
print(f"Має дорівнювати b = {b}")
