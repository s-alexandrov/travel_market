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

Логирование реализовано через пакет logging

```angular2html
Подробнее: https://docs.python.org/3/library/logging.html
```

Проверка кода организована через pre-commit

```angular2html
Подробнее: https://pre-commit.com/
```

По результатам тестирования генерируется отчет Allure

```angular2html
Подробнее: https://docs.qameta.io/allure/
```

### План работы:
```angular2html
- Необходимо написать ui тесты на [cypress-tourism-app.herokuapp.com](https://cypress-tourism-app.herokuapp.com)
- Необходимо написать тесты на  3 раздела (авторизация, регистрация и бронирование отеля). Для каждого раздела необходимо добавить позитивные и негативные тесты (количество на выбор студента). Для раздела бронирования достаточно позитивного теста.
- Необходимо составить к тестам тестовую документацию. В тест кейсах должны быть предварительные шаги (если это необходимо), шаги, ожидаемый результат. Как и где ее хранить остается на выбор студента.
```
### Требования:
```angular2html
- [X] Проект должен быть выложен на github:
- [X] Необходимо настроить CI. В проекте должен присутствовать файл настроек, который описывают логику взаимодействия с CI.
- [X] Необходимо настроить линтер, который должен запускаться локально/на стороне CI
- [X] К каждому тесту должны присутствовать тест кейсы
- [X] README.md заполнен и содержит актуальную информацию
- :white_check_mark: В файле README.md стоят бейджики CI
```
