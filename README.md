# TravelMarket
[![Python application](https://github.com/s-alexandrov/travel_market/actions/workflows/python-app.yml/badge.svg)](https://github.com/s-alexandrov/travel_market/actions/workflows/python-app.yml) ![TeamCity build status](http://188.120.227.87:8111/app/rest/builds/buildType:id:TravelMarket_Alexandrov/statusIcon.svg)

Автотесты для сайта https://cypress-tourism-app.herokuapp.com/

Для локального запуска необходим Python версии 3.8 и выше.
При первом запуске надо создать и активировать виртуальное окружение.

```angular2html
python3 -m venv env
```
```angular2html
source env/bin/activate
```

Установить зависимости проекта.

```angular2html
pip3 install -r requirements.txt
```

Запуск тестов

```angular2html
pytest
```
---
## Логирование реализовано через пакет logging
Подробнее https://docs.python.org/3/library/logging.html

---
