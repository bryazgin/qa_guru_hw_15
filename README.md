# Проект автоматизации тестирования сайта Sportmaster LAB.

## Краткое описание.
Проект содержит UI автотесты на функционал сайта [Sportmaster LAB](https://smlab.digital/?utm_lang=en). 

UI тесты реализованы в связке `Python`+`Selene`.  
Запуск тестов осуществляется в `Jenkins`.  
Для отчетов по результатам прогона используется `Allure` + отправляется уведомление в телеграм с краткими результатами.

## Что покрыто тестами
- отображение баннера на главной странице
- баннер главной страницы содержит нужное изображение
- на главной странице отображается верный номер аккредитации
- на странице "о нас" содержится требуемое видео
- при нажатии на элемент страницы E-commerce пояляется требуемое изображение

## Технологии.
<img src="resources/icons/python-original.svg" width="50"> <img src="resources/icons/pytest-original-wordmark.svg" width="50">
<img src="resources/icons/selene.png" width="50"> <img src="resources/icons/jenkins.png" width="50">
<img src="resources/icons/selenoid.png" width="50"> <img src="resources/icons/allure_report.png" width="50">
<img src="resources/icons/allure_testops.png" width="50"> <img src="resources/icons/tg.png" width="50">

## Запуск на сервере.

Запуск тестов выполняется в проекте [Jenkins](https://jenkins.autotests.cloud/job/008-Bryazgin-hw15/).

1. Перейти в [проект](https://jenkins.autotests.cloud/job/008-Bryazgin-hw15/) и нажать кнопку `Build with Parameters`.
<img src="resources/screenshots/Build with Parameters.png" width="1000">
2. Указать параметры сборки  
`COMMENT` - комментарий, указывающий особенности сборки  
`ENVIRONMENT` - выбор среды запуска тестов  
<img src="resources/screenshots/select parameters.png" width="1000">
3. Дождаться окончания прогона
<img src="resources/screenshots/finish run.png" width="1000"> 
4. Для просмотра отчета нажать одну из иконок 
<img src="resources/screenshots/report icons.png" width="1000"> 




## Локальный запуск.
