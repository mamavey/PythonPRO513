import csv


def display_csv_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def get_csv_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def write_csv_data(filepath, data):
    with open(filepath, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return True


if __name__ == '__main__':
    display_csv_data(r'csv_files\data.csv')
    print(get_csv_data(r'csv_files\data.csv'))
    data_to_write = [
        ['Name', 'Age', 'City'],
        ['Alice', '30', 'New York'],
        ['Bob', '25', 'Los Angeles'],
        ['Charlie', '35', 'Chicago']
    ]
    write_csv_data(r'csv_files\write_data.csv', data_to_write)
