def total_salary(path):
    """
    Аналізує файл із заробітними платами розробників і повертає загальну та середню суму заробітної плати.

    Параметри:
    path (str): Шлях до текстового файлу, який містить дані про заробітні плати.

    Повертає:
    tuple: Кортеж із двох чисел - загальна сума заробітної плати (int) та середня заробітна плата (float).
           У випадку помилки повертає (0, 0.0).
    """
    total = 0
    count = 0

    try:
        # Відкриваємо файл із кодуванням UTF-8
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на прізвище та зарплату
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue  # Пропускаємо рядки з неправильним форматом
                try:
                    salary = int(parts[1])
                    total += salary
                    count += 1
                except ValueError:
                    continue  # Пропускаємо рядки з некоректною зарплатою

        if count == 0:
            return 0, 0.0  # Якщо немає даних, повертаємо 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0.0
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return 0, 0.0

if __name__ == "__main__":
    total, average = total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")