# The social network pulseshare
>_Проект небольшой социальной сети, которая позволяет вести свой блог с возможностью подписки на других авторов и  комментирования их постов. Можно добавлять, редактировать или удалять свои записи. Загружать картинки в пост и радоваться жизни_ ✨

## Tech
- Python 3.9
- Django framework 2.2.16

## Installation
1.Клонируйте репозиторий:
```sh
git clone https://github.com/PortnDar/pulseshare.git
```
```sh
cd pulseshare
```
2.Установите и активируйте виртуальное окружение
```sh
python -m venv venv
```
```sh
source venv/Scripts/activate
```
3.Установите зависимости из файла requirements.txt
```sh
pip install -r requirements.txt
```
4.Выполните миграции в папке с файлом manage.py:
```sh
python manage.py migrate
```
5.Запустите сервер в папке с файлом manage.py:
```sh
python manage.py runserver
```
## Author
Портнова Дарья и корги Эми

![2c4449e5-86e4-4690-b462-caedd0b9](https://user-images.githubusercontent.com/122153098/222242638-70ba9cdd-774b-4cbf-9ca1-7557ed823c73.jpg)

## License
MIT