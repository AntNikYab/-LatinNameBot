# -LatinNameBot

Телеграм-Бот принимает ФИО в кириллице и отдает ФИО на латинице в соответствии с Приказом МИД России от 12.02.2020 № 2113

1. Установить докер (через терминал) - sudo snap install docker
2. Далее в терминале наберите - docker build .
3. С помощью команды - docker images - выведите созданные образы
4. Скопируйте IMAGE ID последнего изображения
5. В терминале введите команду - docker run -d -p 80:80 'здесь IMAGE ID'
6. Телеграм-Бот работает