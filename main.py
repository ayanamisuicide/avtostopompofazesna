from pathlib import Path

downloads_folder = Path.home() / "Downloads"

print("Организатор файлов запущен.")
print(f"Папка для сортировки: {downloads_folder}")

if downloads_folder.exists():
    print("Папка существует.")
else:
    print("Папка не найдена.")
