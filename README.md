# Измени свою жизнь!

## Цели проекта
1. Помочь пользователя которые хотят улучшить свою жизнь привить нужные для них привычки

## Описание
- Это приложение написанное для поддержки человека который хочет менять свою жизнь в лучшую сторону.
- Оно поможет вам не забыть о важных для вас привычках.



## Описание проекта
1) Регистрация пользователя по email и паролю
2) Если указать chat_id то приложение будет напоминать о привычках в телеграмм
3) Создание привычки
4) Возможность настраивать напоминания по дням и времени
5) возможность публиковать привычки и смотреть публичные привычки других пользователей
6) Возможность редактировать свои привычки
7) Возможность удалять не нужные привычки

## Типы привычек
1) Основная привычка
   ## Имеет поля
   - место
   - время действия
   - действие
   - связную привычку
   - вознаграждение
   - периодичность
   - время на выполнение действия (максимум 2 минуты)
   - признак публикации

   * заполните строку вознаграждения (нельзя заполнять вместе со связной привычкой)
   * признак приятной привычки не нужно заполнять (он должен оставаться False)
   * добавьте связную привычку (нельзя заполнять вместе с вознаграждением)

2) приятная привычка (используется как связная привычка)
   - место
   - время действия
   - действие
   - признак приятной привычки
   - периодичность
   - время на выполнение действия (максимум 2 минуты)
   - признак публикации

  * поменяйте признак приятной привычки на True
  * не имеет связной привычки так как она сама используется как связная привычка
  * не имеет вознаграждения так как она сама заменяет вознаграждение

# Docker 
## Требования

Убедитесь, что на вашей системе установлены следующие компоненты:
- Docker
- Docker Compose

## Установка и настройка Docker

### Установка Docker

Следуйте официальной документации для установки Docker:
- [Установка Docker на Windows](https://docs.docker.com/docker-for-windows/install/)
- [Установка Docker на macOS](https://docs.docker.com/docker-for-mac/install/)
- [Установка Docker на Linux](https://docs.docker.com/engine/install/)

### Установка Docker Compose

Следуйте официальной документации для установки Docker Compose:
- [Инструкция по установке Docker Compose](https://docs.docker.com/compose/install/)

## Переменные окружения

Создайте файл `.env` в корневой директории проекта и добавьте следующие переменные:

```plaintext
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=habits
PGPORT=5433

Команда для сборки контейнера
docker-compose up -d --build   

Команда для входа в контейнер db
docker-compose exec db psql -U postgres  

Создать БД
create database habits;
выйти из БД
/q



