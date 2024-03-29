## **Инструкция по работе с Git**

### **Установка Git**

Необходимо скачать программу для вашей операционной системы по [ссылке](https://git-scm.com/downloads).


Для первичной инициализации необходимо создать папку, сделать ее текущей и ввести комманду *__git init__*  в терминале.

В результате в папке будет создана скрытая директория .git, что говорит о том, что инициализация успешна и git готов отслеживать изменения.

При первом использовании Git необходимо заполнить **config** файл и указать имя пользователя и электронную почту. Делается это командами:
* __*git config --global user.email "название_ящика@домен.com"*__
* __*git config --global user.name "Имя пользователя"*__

## **Основные комманды по работе с Git**

* _**git status**_ – получить информацию от git о его текущем состоянии

* _**git add**_ – добавить файл или файлы к следующему коммиту

*  _**git commit**_ -m “message” – создание коммита.

* _**git log**_ – вывод на экран истории всех коммитов с их хеш-кодами

* _**git checkout**_ – переход от одного коммита к другому

* _**git checkout master**_ – вернуться к актуальному состоянию и продолжить работу (делает ветку мастер текущей)
*  _**git diff**_ – увидеть разницу между текущим файлом и закоммиченным файлом

## **Работа с ветками в Git**

Для проверки текущей ветки необходимо ввести команду _**git branch**_ 


Для создания новой ветки необходимо использовать комманду _**git branch <Имя ветки>**__

Для переключения между ветками необходимо использовать комманду _**git checkout <Имя ветки>**_


## **Работа с удаленными репозиториями**

**Авторизация в GitHub**

+ ***New*** – Создаём репозиторий
+ ***HTTPS*** – переключаем “Quick setup” для доступа по HTTPS
+ ***git remote add origin …*** – добавляем адрес удалённого репозитория
+ ***git branch -M main*** – меняем название основной ветки
+ ***git log*** – вывод на экран истории всех коммитов с их хеш-кодами
+ ***git push -u origin main*** – отправляем изменения на удалённый репозиторий
+ ***Sign in with browser*** – Выбираем авторизацию через браузер
+ ***Authorize GitCredentialManager*** – подтверждаем доступ

При необходимости авторизацию можно удалить:
+ ***https://github.com/settings/applications*** – удаляем авторизацию при
необходимости

**Fork в GitHub**
+ Заходим в репозиторий по ссылке на GitHub
+ ***Fork*** – копируем к себе репозиторий
+ ***Create a new branch for this commit and start a pull request*** – создаём новую ветку
+ ***Compare & pull request*** – отправляем PR (pull request)

**Основные команды по работе с удаленными репозиториями**

+ ***git clone <url-адрес репозитория>*** – клонирование внешнего репозитория на
локальный ПК
+ ***git pull*** – получение изменений и слияние с локальной версией
+ ***git push*** – отправляет локальную версию репозитория на внешний










