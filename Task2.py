def get_cats_info(path):
    """
    Зчитує файл із інформацією про котів і повертає список словників з даними про кожного кота.

    Параметри:
    path (str): Шлях до текстового файлу, який містить дані про котів.

    Повертає:
    list: Список словників, де кожен словник містить 'id', 'name' та 'age' кота.
          У випадку помилки повертає порожній список.
    """
    cats_list = []

    try:
        # Відкриваємо файл із кодуванням UTF-8
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на id, ім'я та вік
                parts = line.strip().split(',')
                if len(parts) != 3:
                    continue  # Пропускаємо рядки з неправильним форматом
                cat_id, name, age = parts
                # Створюємо словник для кота
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                # Додаємо словник до списку
                cats_list.append(cat_info)

        return cats_list

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return []

if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)