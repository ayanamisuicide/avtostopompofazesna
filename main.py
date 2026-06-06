from pathlib import Path

VERSION = "1.0.0"

downloads_folder = Path.home() / "Downloads"

categories = {
    "Images": {".jpg", ".jpeg", ".png", ".gif"},
    "Documents": {".pdf", ".doc", ".docx", ".txt"},
    "Archives": {".zip", ".rar", ".7z"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Music": {".mp3", ".wav", ".flac", ".ogg"},
    "Installers": {".exe", ".msi"},
}

print(f"Организатор файлов v{VERSION} запущен.")
print(f"Папка для сортировки: {downloads_folder}")

answer = input("Начать сортировку? (да/нет): ").strip().lower()

if answer not in {"да", "д", "yes", "y"}:
    print("Сортировка отменена.")
    raise SystemExit

moved_count = 0
skipped_count = 0

if downloads_folder.exists():
    print("Папка существует.")
    for item in downloads_folder.iterdir():
        if item.is_file():
            extension = item.suffix.lower()
            category_name = "Others"

            for category, extensions in categories.items():
                if extension in extensions:
                    category_name = category
                    break

            print(f"{item.name} относится к категории {category_name}")
            destination_folder = downloads_folder / category_name
            destination_folder.mkdir(exist_ok=True)
            print(f"Будущая папка: {destination_folder}")
            destination_file = destination_folder / item.name
            print(f"Будущий путь файла: {destination_file}")

            if destination_file.exists():
                print("Файл с таким именем уже существует. Скипаем.")
                skipped_count += 1
            else:
                try:
                    item.rename(destination_file)
                    print(f"Перемещено: {item.name} -> {category_name}")
                    moved_count += 1
                except OSError as error:
                    print(f"Не удалось переместить {item.name}: {error}")
                    skipped_count += 1
else:
    print("Папка не найдена.")

print("Сортировка завершена.")
print(f"Перемещено файлов: {moved_count}")
print(f"Пропущено файлов: {skipped_count}")
