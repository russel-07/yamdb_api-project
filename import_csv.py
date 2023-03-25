import csv, sqlite3


def import_csv_to_db(from_file_path, to_db_name, to_table_name):
    connect = sqlite3.connect(to_db_name)
    cursor = connect.cursor()

    with open(from_file_path, 'r', encoding='utf8') as file:
        dr = csv.DictReader(file, delimiter=',') # csv.DictReader по умолчанию использует первую строку под заголовки столбцов
        csv_headers = tuple(dr.fieldnames)
        to_db = [[value for value in str.values()] for str in dr]

    get_model_headers = connect.execute(f'SELECT * FROM {to_table_name}')
    model_headers = tuple(str[0] for str in get_model_headers.description)

    import_headers = list(csv_headers)
    for header in model_headers:
        if header not in import_headers:
            import_headers.append(header)

    import_values = '('
    i = 0
    for header in import_headers:
        if header in csv_headers:
            import_values += '?'
        else:
            import_values += "''"
        i += 1

        if i < len(import_headers):
            import_values += ', '
        else:
            import_values += ')'

    cursor.executemany(f"INSERT INTO {to_table_name} {tuple(import_headers)} VALUES {import_values};", to_db)
    connect.commit()
    connect.close()


def import_all(csv_to_table_dict, from_files_path, to_db_name):
    for key in csv_to_table_dict:
        from_path = from_files_path + csv_to_table_dict[key] + '.csv'
        to_table_name = key
        import_csv_to_db(from_path, to_db_name, to_table_name)


def export_db_to_csv(to_file_path, from_db_name, from_table_name):
    connect = sqlite3.connect(from_db_name)
    connect.text_factory = str
    cursor = connect.cursor()

    data = cursor.execute(f'SELECT * FROM {from_table_name}')
    with open(to_file_path, 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        model_headers = (str[0] for str in data.description)
        writer.writerow(model_headers)
        writer.writerows(data)


def export_all(table_to_csv_dict, from_db_name, to_files_path):
    for key in table_to_csv_dict:
        to_path = to_files_path + table_to_csv_dict[key] + '.csv'
        from_table_name = key
        export_db_to_csv(to_path, from_db_name, from_table_name)


yamdb_dict = {
    'auth_and_users_user': 'users',
    'categories_genres_titles_genre': 'genre',
    'categories_genres_titles_category': 'category',
    'categories_genres_titles_title_genre': 'genre_title',
    'categories_genres_titles_title': 'titles',
    'reviews_comments_review': 'review',
    'reviews_comments_comment': 'comments'
}

#import_all(yamdb_dict, './import_csv/', 'db.sqlite3')
#export_all(yamdb_dict, 'db.sqlite3', './export_csv/')

