# test-blog
Данный блог является реализацией тестового задания на позицию Junior Django Developer
### Описание
Веб-приложение на Django, которое будет отображать список пользователей и их посты, а также позволять добавлять и удалять посты
### Требования:
- [x] Создайте две модели данных: User и Post. 
  Модель User: id (уникальный идентификатор), name (имя пользователя), email (электронная почта пользователя). 
  Модель Post: id (уникальный идентификатор), user (ссылка на пользователя, который создал пост), title (заголовок поста), body (текст поста).
- [x] Создайте пользовательский интерфейс с использованием Django templates, который будет отображать список всех пользователей. При клике на имя пользователя, должен открываться список его постов. 
- [x] Реализуйте механизм аутентификации и авторизации.
- [x] Добавьте формы для добавления и удаления постов.Только аутентифицированные пользователи могут добавлять и удалять посты. Пользователи могут удалять только свои посты.
- [x] Напишите unit-тесты для вашего приложения
### Работа с Django REST Framework
- [x] Создайте несколько API-конечных пунктов. Первый должен возвращать список всех пользователей, второй - список всех постов конкретного пользователя, третий - добавление нового поста, четвертый - удаление существующего поста.
- [ ] Создайте способы аутентификации и авторизации через API
- [ ] Напишите unit-тесты для проверки корректности работы вашего API, включая тесты аутентификации и авторизации.
### Бонусные задания
- [ ] Добавьте систему комментариев для постов. Пользователи должны иметь возможность оставлять комментарии к постам.
- [ ] Добавьте пагинацию на страницу со списком постов, чтобы ограничить количество отображаемых постов на одной странице.
- [ ] Добавьте возможность редактирования постов. Пользователи должны видеть кнопку редактирования рядом с каждым своим постом.