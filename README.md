
![airendercover](https://github.com/user-attachments/assets/2da6bf31-ce74-4092-a44b-1645aa64d32c)
![Untitled-1](https://github.com/user-attachments/assets/f968c4ed-a8c8-4991-9af2-735669d8b80d)

Installation and Usage:

Pre-Installation:

1) Install Stable Diffusion by AUTOMATIC (https://github.com/AUTOMATIC1111/stable-diffusion-webui).
2) Download the default MLL model or your own models that you plan to use.
3) Open the C4DtoAI.py script and edit it to include the paths for the render import file and the save location for the edited image.
4) Open Cinema 4D (version S24). Navigate to Extensions > User Scripts > Run Script, and select your script.

Usage:

1) Specify the texture you want (it is recommended to use PROMPT generators for Stable Diffusion).
2) Enter negative keywords.
3) Start the process and wait for the rendering to complete. The rendering progress will be displayed in the terminal window.

F.A.Q

Can I change IMG2IMG parameters?
Yes, this can be done in the script file. Open it in a text editor and adjust the values.

What if the script fails to start or shows a "server not found" error?
Check that the IP address and port specified in the script match those shown in the terminal.

Still not working?
Use the --api flag when launching the launch.py script in SDwebUI.


Установка и использование:

Пред. установка:
1) Установите Stable Diffusion от AUTOMATIC ( https://github.com/AUTOMATIC1111/stable-diffusion-webui )
2) Скачайте модель MLL по умолчанию или свои модели, которые будете использовать. 
3) Открываем скрипт C4DtoAI.py и редактируем туда путь к файлу импорта рендера и путь сохранения для отредактированной картинке
5) Открываем C4D S24   Находим пункт Extensions> User Scripts > Run Script и выбираем наш скрипт

Использование:
- Вписываем какую текстуру хотим ( советую использовать PROMPT генераторы для Stable Diffusion ) 
- Вводим негативные слова
- Запускаем и ждём рендера, прогрессия рендера будет видна в окне терминала

F.A.Q
-  Могу ли я изменить параметры IMG2IMG? 
Да, это делается в файле скрипта, открываем в блокноте и редактируем значения

- Если скрипт не запускается или выдаёт ошибку не найденного сервера? 
Посмотрите что IP и порт указаны верно и совпадают с тем что указано в терминале

- Всё ещё не запускается? 
Воспользуйтесь флагами —api при старте скрипта launch.py в SDwebUI
