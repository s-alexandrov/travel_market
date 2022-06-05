# TravelMarket

### Автоматизированное тестирование UI сайта https://cypress-tourism-app.herokuapp.com/
[![Python application](https://github.com/s-alexandrov/travel_market/actions/workflows/python-app.yml/badge.svg)](https://github.com/s-alexandrov/travel_market/actions/workflows/python-app.yml) ![TeamCity build status](http://188.120.227.87:8111/app/rest/builds/buildType:id:TravelMarket_Alexandrov/statusIcon.svg)

Итоговая аттестационная работа по курсу "Python QA Engineer".
Цель проекта - покрыть автотестами три раздела сайта: регистрация, авторизация и бронирование.

Для локального запуска необходим Python версии 3.8 и выше.
При первом запуске надо создать и активировать виртуальное окружение:

```angular2html
python3 -m venv env
```
```angular2html
source env/bin/activate
```

Установить зависимости проекта:

```angular2html
pip3 install -r requirements.txt
```

Запуск тестов:

```angular2html
pytest
```

Логирование реализовано через пакет logging

```angular2html
Подробнее: https://docs.python.org/3/library/logging.html
```

Локальная проверка кода организована через pre-commit

```angular2html
Подробнее: https://pre-commit.com/
```

По результатам тестирования генерируется отчет Allure.
Запуск тестов:

```angular2html
pytest --alluredir=allure_results
```

Генерация отчета:

```angular2html
allure serve allure_results
```

Тест-кейсы:

```angular2html
allure serve allure_results
```

### План работы:
- Необходимо написать ui тесты на https://cypress-tourism-app.herokuapp.com
- Необходимо написать тесты на  3 раздела (авторизация, регистрация и бронирование отеля). Для каждого раздела необходимо добавить позитивные и негативные тесты (количество на выбор студента). Для раздела бронирования достаточно позитивного теста.
- Необходимо составить к тестам тестовую документацию. В тест кейсах должны быть предварительные шаги (если это необходимо), шаги, ожидаемый результат. Как и где ее хранить остается на выбор студента.

### Требования:
- [x] Проект должен быть выложен на github
- [x] Необходимо настроить CI. В проекте должен присутствовать файл настроек, который описывают логику взаимодействия с CI.
- [x] Необходимо настроить линтер, который должен запускаться локально/на стороне CI
- [x] К каждому тесту должны присутствовать тест кейсы
- [x] README.md заполнен и содержит актуальную информацию
- [x] В файле README.md стоят бейджики CI
