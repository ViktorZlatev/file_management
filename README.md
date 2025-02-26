
# File Management System

Това е система за управление на файлове, която използва Flask за бекенд, MinIO за съхранение на файлове, и Keycloak за управление на потребителската автентикация.

## Съдържание
- [Изисквания]
- [Стартиране на проекта]
- [Използване на системата]
- [Структура на проекта]
- [Често срещани проблеми]

---

## Изисквания

За да стартирате проекта, са необходими:
- **Docker** и **Docker Compose** (за стартиране на сървърите)
- **Python 3.10+** (ако стартирате бекенда локално)
- `pip` (за управление на зависимости)

## Стартиране на проекта

### 1. Клониране на хранилището

git clone <URL на хранилището>
cd <папка на проекта>
2. Стартирайте Docker Compose
Стартиране на всички услуги, дефинирани в docker-compose.yml:


docker-compose up --build
Това ще стартира:

MinIO на порт 9000 (интерфейс на порт 9001)
Keycloak на порт 8080
Flask приложение на порт 5000

3. Конфигуриране на Keycloak
Влезте в Keycloak Admin Console: http://localhost:8080
Потребителско име: admin
Парола: admin
Създайте Realm, клиент и роли според вашите нужди.
Конфигурирайте URL на Keycloak в бекенда:
Във файла docker-compose.yml намерете средата KEYCLOAK_URL и се уверете, че тя сочи към http://keycloak:8080.


Използване на системата
API Ендпойнти

Качване на файл:
POST /upload

Полета:
file: Файл за качване
Изтегляне на файл:
GET /download/<filename>

Списък с файлове:
GET /files
Достъп до MinIO
Интерфейс на MinIO: http://localhost:9001
Потребител: minioadmin
Парола: minioadmin



4. Примерни API заявки( чрез cURL )


Качване на файл:
curl -X POST -H "Authorization: Bearer <TOKEN>" -F "file=@example.txt" http://localhost:5000/upload


Сваляне на файл:
curl -X GET -H "Authorization: Bearer <TOKEN>" http://localhost:5000/download/<file_id>


Обновяване на файл:
curl -X PUT -H "Authorization: Bearer <TOKEN>" -F "file=@new_example.txt" http://localhost:5000/update/<file_id>


Изтриване на файл:
curl -X DELETE -H "Authorization: Bearer <TOKEN>" http://localhost:5000/delete/<file_id>


Структура на проекта

file_management/
├── app/
│   ├── app.py               # Основен файл на Flask приложението
│   ├── minio_config.py      # Конфигурация за MinIO клиента
│   ├── requirements.txt     # Зависимости
│   └── templates/           # HTML шаблони (ако има)
├── docker-compose.yml        # Docker Compose конфигурация
└── README.md                 # Инструкции за стартиране

