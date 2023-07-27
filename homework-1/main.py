"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


def csv_read(file_name: str) -> list:
    """
    Функция для чтения файлов csv. Возвращает список строк файла
    """
    try:
        with open(file_name) as read_file:
            data = []

            for row_file in csv.reader(read_file):
                data.append(row_file)

            return data
    except Exception as ex:
        print(ex)


def query_insert_into(table_name: str, data_for_add: list, first_line=True) -> str:
    """
    Функция, которая формирует sql команду insert
    table_name: название таблицы
    data_for_add: данные для добавления
    first_line: Назначение первой строки =  False - содержит данные
                                            True - содержит название столбцов
    """
    columns_numbers = len(data_for_add[0])  # количество столбцов
    data_numbers = len(data_for_add)  # длина списка

    query = f"INSERT INTO {table_name} "  # заголовок запроса

    # если первая строка списка содержит названия столбцов, то добавляем их в запрос
    if first_line:
        query += "("
        for i in range(columns_numbers):
            query += data_for_add[0][i]

            # если не последний столбец, то ставим запятую
            if i != columns_numbers - 1:
                query += ", "

        query += ") "

    query += "VALUES \n"

    for i in range(1, data_numbers):
        query += "("
        for j in range(columns_numbers):
            if data_for_add[i][j].isdecimal():
                query += data_for_add[i][j]
            else:
                parameter = "".join([symbol for symbol in list(data_for_add[i][j]) if symbol != "'"])
                query += f"'{parameter}'"

            if j != columns_numbers - 1:
                query += ", "

        if i != data_numbers - 1:
            query += "), \n"
        else:
            query += ");\n"

    return query


def main():
    """
    Функция, заполняющая таблицы customers, employees, orders данные из .csv файла
    """
    # считываем данные из .csv файла в массив
    customers = csv_read(file_name="north_data/customers_data.csv")
    employees = csv_read(file_name="north_data/employees_data.csv")
    orders = csv_read(file_name="north_data/orders_data.csv")

    # открываем коннект с БД
    try:
        with psycopg2.connect(host="localhost", database="north", user="postgres", password="postgres") as dbconnect:
            cursor = dbconnect.cursor()

            # формируем запросы
            query_1 = query_insert_into(table_name='customers', data_for_add=customers)
            query_2 = query_insert_into(table_name='employees', data_for_add=employees)
            query_3 = query_insert_into(table_name='orders', data_for_add=orders)

            cursor.execute(query_1 + query_2)
            dbconnect.commit()

            cursor.execute(query_3)
            dbconnect.commit()

        dbconnect.close()
    except Exception as ex:
        print(ex)


# вызываем главную функцию
main()
