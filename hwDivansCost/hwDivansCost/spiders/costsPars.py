import scrapy

class CostsparsSpider(scrapy.Spider):
    name = "costsPars"
    allowed_domains = ["divan.ru"]
    # start_urls - это та ссылка, от которой начинается парсинг
    start_urls = ["https://www.divan.ru/category/divany"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        # response.css(’div._Ud0k’) — поиск по тегу. Будет создан целый список
        divans = response.css('div.lsooF')

        # Настраиваем работу с каждым отдельным диваном в списке
        for divan in divans:
            # оператор "yield" помогает обрабатывать одно отдельное действие
            # С его помощью мы можем управлять потоком выполнения,
            # останавливать и возобновлять работу парсера (С другими операторами мы такого делать не можем)
            # Ссылки и теги получаем с помощью консоли на сайте
            yield {
                # Создаём словарик названий, используем поиск по диву, а внутри дива — по тегу span
                'name' : divan.css('div.lsooF span::text').get(),
                # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
                'price' : divan.css('div.pY3d2 span::text').get(),
                'exist' : divan.css('div.MYKz_::text').get()
            }

            # Создали новый запрос для перехода на следующую страницу
            # `self.parse` - функция, которая будет вызвана для обработки ответа с новой страницы.
            # Мы повторно вызываем метод `parse`, чтобы извлечь данные с новой страницы точно так же,как и с первой.
            # `yield` возвращает новый запрос в очередь Scrapy. Это асинхронный подход,
            # который позволяет Scrapy эффективно управлять многими запросами параллельно
            # Поиск ссылки на след страницу из атрибута href в теге <a> класс ZIuae
            next_page = response.css('a.ZIuae::attr(href)').get()
            if next_page:
                yield response.follow(next_page, self.parse)













