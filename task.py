import heapq
from typing import List

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    # Ініціалізуємо мінімальну купу
    min_heap = []

    # Додаємо перші елементи з кожного списку у купу
    for i, sorted_list in enumerate(lists):
        if sorted_list:  # Перевіряємо, що список не порожній
            heapq.heappush(min_heap, (sorted_list[0], i, 0))

    merged_list = []

    # Виконуємо злиття списків
    while min_heap:
        # Отримуємо найменший елемент з купи
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)

        # Додаємо наступний елемент з того ж списку в купу, якщо він існує
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))

    return merged_list

# Приклад використання функції
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)