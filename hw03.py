import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama з автоматичним скиданням кольорів
init(autoreset=True)

def visualize_directory(path, indent=0):
    """
    Рекурсивно виводить структуру директорії з кольоровим маркуванням.

    Параметри:
    path (Path): Шлях до директорії або файлу.
    indent (int): Рівень відступу для відображення вкладеності.
    """
    if path.is_dir():
        # Виводимо ім'я директорії синім кольором
        print(Fore.BLUE + Style.BRIGHT + '  ' * indent + f"📂 {path.name}")
        # Обходимо всі елементи в директорії
        for item in path.iterdir():
            visualize_directory(item, indent + 1)
    elif path.is_file():
        # Виводимо ім'я файлу зеленим кольором
        print(Fore.GREEN + '  ' * indent + f"📜 {path.name}")

def main():
    """
    Головна функція: отримує шлях з командного рядка та запускає візуалізацію.
    """
    # Перевірка кількості аргументів
    if len(sys.argv) != 2:
        print("Використання: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    # Перетворення аргументу в об'єкт Path
    dir_path = Path(sys.argv[1])

    # Перевірка існування шляху та чи є він директорією
    if not dir_path.exists():
        print(f"Помилка: Шлях '{dir_path}' не існує.")
        sys.exit(1)
    if not dir_path.is_dir():
        print(f"Помилка: '{dir_path}' не є директорією.")
        sys.exit(1)

    # Виведення структури директорії
    print(f"Структура директорії '{dir_path}':")
    visualize_directory(dir_path)

if __name__ == "__main__":
    main()