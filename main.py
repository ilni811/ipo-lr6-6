import random

# 1. Создание случайного списка из 20 значений по 4 случайных целых числа от -10 до 10
random_list = [tuple(random.randint(-10, 10) for _ in range(4)) for _ in range(20)]
print("Случайный список:", random_list)

# 2. Нахождение всех уникальных комбинаций пар из этих значений
unique_pairs = []
for i in range (len(random_list)):
    for j in range(i + 1, len(random_list)):
        unique_pairs.append((random_list[i], random_list[j]))

print("Уникальные пары:", unique_pairs)

# 3. Пользователь вводит целое число
user_input = int(input("Введите целое число: "))

# 4. Вычисление количества пар, чья сумма меньше заданного значения
count = 0
for pair in unique_pairs:
    # Суммируем все элементы в паре
    total_sum = sum(pair[0]) + sum(pair[1])
    if total_sum < user_input:
        count += 1

print(f"Количество пар, сумма которых меньше {user_input}: {count}")
