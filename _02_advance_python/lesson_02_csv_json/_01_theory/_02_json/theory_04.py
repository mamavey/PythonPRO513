import json


class MyCat:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_data(self):
        return self.name, self.age, self.gender


class MyCatEncoder(json.JSONEncoder):
    def default(self, o):
        return {'ClassName': o.__class__.__name__,
                'fields': {
                    'name': o.name,
                    'age': o.age,
                    'gender': o.gender
                },
                'methods':
                    {'get_data': o.get_data()}
                }


def write_data_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as fp:
        json.dump(obj=data, fp=fp,
                  cls=MyCatEncoder,
                  ensure_ascii=False, indent=4)
    return True


if __name__ == '__main__':
    cat = MyCat('Мурзик', 4, 'самец')
    write_data_json(r'json_files\encode_cat.json', cat)
    cat_string = json.dumps(obj=cat, cls=MyCatEncoder, ensure_ascii=False, indent=4)
    print(cat_string)
