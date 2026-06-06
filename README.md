# File Organizer

Простой консольный скрипт на Python, который наводит порядок в папке
`Downloads`: определяет тип каждого файла по расширению и перемещает его в
подходящую категорию.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

## Возможности

- запрашивает подтверждение перед началом сортировки;
- обрабатывает только файлы в корне папки `Downloads`;
- автоматически создаёт папки категорий;
- не перезаписывает файлы с одинаковыми именами;
- продолжает работу при ошибке доступа к отдельному файлу;
- выводит итоговое количество перемещённых и пропущенных файлов;
- использует только стандартную библиотеку Python.

## Категории

| Папка | Расширения |
| --- | --- |
| `Images` | `.jpg`, `.jpeg`, `.png`, `.gif` |
| `Documents` | `.pdf`, `.doc`, `.docx`, `.txt` |
| `Archives` | `.zip`, `.rar`, `.7z` |
| `Videos` | `.mp4`, `.mkv`, `.avi`, `.mov` |
| `Music` | `.mp3`, `.wav`, `.flac`, `.ogg` |
| `Installers` | `.exe`, `.msi` |
| `Others` | все остальные расширения |

## Требования

- Python 3.10 или новее;
- Windows, Linux или macOS;
- папка `Downloads` в домашней директории пользователя.

Проект проверен с Python 3.14.4.

## Запуск

Клонируйте репозиторий:

```bash
git clone https://github.com/ayanamisuicide/avtostopompofazesna.git
cd avtostopompofazesna
```

Запустите скрипт:

```bash
python main.py
```

Подтвердите сортировку:

```text
Начать сортировку? (да/нет): да
```

## Пример

До запуска:

```text
Downloads/
├── archive.zip
├── photo.jpg
└── report.pdf
```

После запуска:

```text
Downloads/
├── Archives/
│   └── archive.zip
├── Documents/
│   └── report.pdf
└── Images/
    └── photo.jpg
```

## Безопасность

Скрипт перемещает все файлы, которые находятся непосредственно в корне
`Downloads`. Перед первым полноценным запуском рекомендуется проверить его на
нескольких тестовых файлах. Вложенные папки скрипт не изменяет.

Если файл с таким именем уже существует в целевой папке, исходный файл
остаётся на месте и учитывается как пропущенный.

## Структура проекта

```text
.
├── main.py
├── README.md
├── CHANGELOG.md
└── VERSION
```

## Разработка

- `main` — стабильная версия;
- `dev` — текущая разработка.

История изменений опубликована в [CHANGELOG.md](CHANGELOG.md).
