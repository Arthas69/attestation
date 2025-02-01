import csv
import os


class PriceMachine(object):
    NAMES = ['товар', 'название', 'наименование', 'продукт']
    PRICES = ['розница', 'цена']
    WEIGHTS = ['вес', 'масса', 'фасовка']

    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def _print_header(self):
        """
            Выводит заголовок таблицы
        """
        header = " №"
        header += "Наименование".center(self.name_length)
        header += "Цена".rjust(7)
        header += " Вес"
        header += "Файл".center(12)
        header += " Цена за кг."
        print(header)

    def _print_line(self, idx, item):
        """
            Выводит строчку с данными о товаре
        """
        print(f"{idx:>2} {item['name']:<{self.name_length}} {item['price']:>5} {item['weight']:^3} "
              f"{item['file']} {item['price_per_kg']}")

    def _search_product_price_weight(self, headers):
        """
            Возвращает номера столбцов
        """
        weight, price, name = None, None, None
        # Ищем столбцы с названием товара, ценой и весом
        # Так как названия столбцов могут быть любыми, проверяем все возможные варианты

        for idx, col in enumerate(headers):
            if col in self.NAMES:
                name = idx
            elif col in self.WEIGHTS:
                weight = idx
            elif col in self.PRICES:
                price = idx
        return weight, price, name

    def load_prices(self, file_path=''):
        """
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
                
            Допустимые названия для столбца с ценой:
                розница
                цена
                
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        """

        # Проходит по всем файлам в целевой папке, и если в названии файла присутствует слово 'price'
        # обрабатывает его и добавляет все строчки в self.data.
        # После этого сортируем получившийся список по параметру цена за кг.

        for path, dirs, files in os.walk(file_path):
            for file in files:
                if 'price' in file.lower():
                    with open(os.path.join(path, file), encoding='utf-8') as f:
                        price_list = csv.reader(f, delimiter=',')
                        headers = next(price_list)
                        weight, price, product_name = self._search_product_price_weight(headers)
                        for row in price_list:
                            product = {
                                'name': row[product_name],
                                'price': int(row[price]),
                                'weight': int(row[weight]),
                                'file': file,
                            }
                            product['price_per_kg'] = round(product['price'] / product['weight'], 2)
                            self.data.append(product)
        self.data.sort(key=lambda x: x['price_per_kg'])

    def export_to_html(self, filename='output.html'):
        """
            Экспортирует данные в HTML-файл
        """
        if not self.result:
            self.result = '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Позиции продуктов</title>
            </head>
            <body>
                <table>
                    <tr>
                        <th>Номер</th>
                        <th>Название</th>
                        <th>Цена</th>
                        <th>Фасовка</th>
                        <th>Файл</th>
                        <th>Цена за кг.</th>
                    </tr>
            '''

            for idx, item in enumerate(self.data, start=1):
                self.result += f'''
                <tr>
                    <td>{idx}</td>
                    <td>{item['name']}</td>
                    <td>{item['price']}</td>
                    <td>{item['weight']}</td>
                    <td>{item['file']}</td>
                    <td>{item['price_per_kg']}</td>
                </tr>
                '''

            self.result += '''
                </table>
            </body>
            </html>
            '''

        with open(filename, 'w') as f:
            f.write(self.result)

    def find_text(self, txt):
        """
            Находит позиции с указанным текстом в названии, форматирует их и выводит
        """
        curr_search = []

        # Находит позиции с указанным текстом в названии и добавляет их в список curr_search
        for item in self.data:
            if txt in item['name'].lower():
                curr_search.append(item)
                self.name_length = max(self.name_length, len(item['name']))

        if curr_search:
            # Печатает заголовок таблицы для вывода найденных результатов
            self._print_header()

            # Выводит найденные позиции с учетом форматирования и выделения текста поиска
            for idx, product in enumerate(curr_search, start=1):
                self._print_line(idx, product)
            print('----------------------------------------------------------------')
        else:
            print(f'Ничего не найдено по запросу "{txt}".')

        self.name_length = 0


if __name__ == '__main__':

    pm = PriceMachine()
    pm.load_prices(os.path.join(os.getcwd(), 'pricelists'))

    while True:
        print('Выберите действие:')
        print('Чтобы выгрузить все позиции в файл, введите - 1')
        print('Чтобы выйти введите - exit')
        print('Введите наименование продукции, чтобы найти: ')
        print('----------------------------------------------------------------')
        text = input('Ваш выбор: ')

        if text == '1':
            pm.export_to_html()
            print('Файл output.html создан.')
        elif text == 'exit':
            break
        else:
            pm.find_text(text)
