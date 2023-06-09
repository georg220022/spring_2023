import os


def black_book(page: int):
    status_code = os.system(f"./black-book -n {page}")
    return True if status_code == 0 else False


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.

    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_book) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.

    Уточнение:
        black_box возвращает True, если страница есть в книге
                  возвращает False, если страницы нет в книге.


    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    start = 1
    end = 10000000

    while start < end:
        middle = (start + end) // 2
        if black_book(middle):
            start = middle + 1
        else:
            end = middle
    print(end)


if __name__ == "__main__":
    # тут явно нужен алгоритм
    main()
