import heapq


def min_cost_to_connect_cables(cables):
    # Перетворюємо список кабелів на мінімальну купу
    heapq.heapify(cables)

    total_cost = 0

    # Продовжуємо з'єднувати кабелі, поки в купі більше одного елемента
    while len(cables) > 1:
        # Вилучаємо два найменших елементи
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо ці два кабелі
        cost = first + second

        # Додаємо витрати на об'єднання до загальних витрат
        total_cost += cost

        # Поміщаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


# Приклад використання функції
cables = [4, 3, 2, 6]
print(min_cost_to_connect_cables(cables))  # Виведе 29