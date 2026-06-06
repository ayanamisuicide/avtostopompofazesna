from pathlib import Path

# Хранит текущую версию программы для отображения при запуске.
VERSION = "1.1.0"

# Указывает папку, содержимое которой программа будет сортировать.
downloads_folder = Path.home() / "Downloads"

# Сопоставляет названия целевых папок с поддерживаемыми расширениями файлов.
categories = {
    "Images": {".jpg", ".jpeg", ".png", ".gif"},
    "Documents": {".pdf", ".doc", ".docx", ".txt"},
    "Archives": {".zip", ".rar", ".7z"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Music": {".mp3", ".wav", ".flac", ".ogg"},
    "Installers": {".exe", ".msi"},
}

# Определяет папку назначения по расширению файла.
def get_category(extension: str) -> str:
    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "Others"

# Сообщает версию программы и выбранную папку для сортировки.
print(f"Организатор файлов v{VERSION} запущен.")
print(f"Папка для сортировки: {downloads_folder}")

# Запрашивает подтверждение, чтобы сортировка не началась случайно.
answer = input("Начать сортировку? (да/нет): ").strip().lower()

# Завершает программу, если пользователь не подтвердил сортировку.
if answer not in {"да", "д", "yes", "y"}:
    print("Сортировка отменена.")
    raise SystemExit

# Считает успешно перемещённые и пропущенные файлы.
moved_count = 0
skipped_count = 0

# Проверяет наличие папки Downloads перед началом работы с файлами.
if downloads_folder.exists():
    print("Папка существует.")

    # Перебирает только элементы, расположенные непосредственно в Downloads.
    for item in downloads_folder.iterdir():
        if item.is_file():
            # Определяет расширение файла и соответствующую ему категорию.
            extension = item.suffix.lower()
            category_name = get_category(extension)

            print(f"{item.name} относится к категории {category_name}")

            # Создаёт папку категории, если она ещё не существует.
            destination_folder = downloads_folder / category_name
            destination_folder.mkdir(exist_ok=True)
            print(f"Будущая папка: {destination_folder}")

            # Формирует полный путь, по которому должен находиться файл.
            destination_file = destination_folder / item.name
            print(f"Будущий путь файла: {destination_file}")

            # Не перезаписывает существующий файл с таким же именем.
            if destination_file.exists():
                print("Файл с таким именем уже существует. Скипаем.")
                skipped_count += 1
            else:
                # Перемещает файл и продолжает работу при ошибке файловой системы.
                try:
                    item.rename(destination_file)
                    print(f"Перемещено: {item.name} -> {category_name}")
                    moved_count += 1
                except OSError as error:
                    print(f"Не удалось переместить {item.name}: {error}")
                    skipped_count += 1
else:
    print("Папка не найдена.")

# Выводит итоговую статистику после завершения сортировки.
print("Сортировка завершена.")
print(f"Перемещено файлов: {moved_count}")
print(f"Пропущено файлов: {skipped_count}")
