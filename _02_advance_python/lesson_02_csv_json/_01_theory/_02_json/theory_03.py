import json


class MyCat:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


def write_mycat_to_json(filepath, cat_obj):
    with open(filepath, 'w', encoding='utf-8') as fp:
        json.dump(obj=cat_obj, fp=fp,
                  default=lambda cat_obj: cat_obj.__dict__,
                  ensure_ascii=False, indent=4)
        return True


def get_json_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as fp:
        data = json.load(fp=fp)
    return data


if __name__ == '__main__':
    cat = MyCat('Барсик', 3, 'самец')
    write_mycat_to_json(r'json_files\cat_data.json', cat)

    cat_data_from_file = get_json_data(r'json_files\cat_data.json')
    new_cat = MyCat(cat_data_from_file['name'], cat_data_from_file['age'], cat_data_from_file['gender'])
    print(new_cat.name)
    print(new_cat.age)
    print(new_cat.gender)
