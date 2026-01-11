import json


class Airplane:

    def __init__(self, model, seats, plane_range):
        self.__model = model
        self.__seats = seats
        self.__plane_range = plane_range

    @property
    def model(self):
        return self.__model

    @property
    def seats(self):
        return self.__seats

    @property
    def plane_range(self):
        return self.__plane_range

    def print_airplane_props(self):
        print(
            f'Airplane model: {self.model} has {self.seats} available seats'
            f'And has {self.plane_range} km max distance flight'
        )


class PlaneJSONAdapter:
    @classmethod
    def to_json(cls, obj: Airplane):
        if isinstance(obj, Airplane):
            return json.dumps({
                'class': obj.__class__.__name__,
                'fields': {
                    'model': obj.model,
                    'seats': obj.seats,
                    'plane_range': obj.plane_range,
                },
                'getters_methods': {
                    'model': obj.model,
                    'seats': obj.seats,
                    'plane_range': obj.plane_range,
                },
                'methods': {
                    'print_airplane_props': f'printed data {
                    [
                        f'Airplane model: {obj.model} has {obj.seats} available seats'
                        f'And has {obj.plane_range} km max distance flight'
                    ]
                    }'
                }
            }, ensure_ascii=False, indent=4)
        raise TypeError('Объект неподходящего класса.')

    @classmethod
    def from_json(cls, obj):
        obj = json.loads(obj)
        try:
            model = obj['fields']['model']
            seats = obj['fields']['seats']
            plane_range = obj['fields']['plane_range']
            plane_obj = Airplane(model, seats, plane_range)
            return plane_obj
        except AttributeError:
            print(f'Неверная структура объекта')
            return None
        except KeyError:
            print(f'Перепроверьте атрибуты')
            return None


if __name__ == '__main__':
    plane = Airplane('Boeing 737-200', 110, 4000)
    plane_json = PlaneJSONAdapter.to_json(plane)
    print(plane_json)
    print()
    my_plane_obj = PlaneJSONAdapter.from_json(plane_json)
    my_plane_obj.print_airplane_props()
