# Практическое задание "Анализатор прайс-листов"

## Описание и требования:

Ваша задача: написать анализатор прайс-листов.

В папке находятся несколько файлов, содержащих прайс-листы от разных поставщиков.
Количество и название файлов заранее неизвестно, однако точно известно, что в названии файлов прайс-листов есть слово "price".
Файлы, не содержащие слово "price", следует игнорировать.
Формат файлов: данные, разделенные запятой.
Порядок колонок в файле заранее неизвестен, но известно, что столбец с названием товара называется одним из вариантов: "название", "продукт", "товар", "наименование".
Столбец с ценой может называться "цена" или "розница".
Столбец с весом имеет название "фасовка", "масса" или "вес" и всегда указывается в килограммах.
Остальные столбцы игнорировать.

### Особенности реализации:

1. Программа должна загрузить данные из всех прайс-листов и предоставить интерфейс для поиска товара по фрагменту названия с сортировкой по цене за килограмм.
2. Интерфейс для поиска реализовать через консоль, циклически получая информацию от пользователя.
3. Если введено слово "exit", то цикл обмена с пользователем завершается, программа выводит сообщение о том, что работа закончена и завершает свою работу.
4. В противном случае введенный текст считается текстом для поиска.
5. Программа должна вывести список найденных позиций в виде таблицы:


| №   | Наименование                | Цена | Вес | Файл          | Цена за кг |
|-----|-----------------------------|------|-----|---------------|------------|
| 1   | филе гигантского кальмара    | 617  | 1   | price_0.csv   | 617.0      |
| 2   | филе гигантского кальмара    | 639  | 1   | price_4.csv   | 639.0      |
| 3   | филе гигантского кальмара    | 639  | 1   | price_6.csv   | 639.0      |
| 4   | филе гигантского кальмара    | 683  | 1   | price_1.csv   | 683.0      |
| 5   | филе гигантского кальмара    | 1381 | 2   | price_5.csv   | 690.5      |
| 6   | кальмар тушка                | 3420 | 3   | price_3.csv   | 1140.0     |
| 7   | кальмар тушка                | 4756 | 4   | price_0.csv   | 1189.0     |


6. Список должен быть отсортирован по возрастанию стоимости за килограмм.
7. Предусмотреть вывод массива данных в текстовый файл в формате HTML.

