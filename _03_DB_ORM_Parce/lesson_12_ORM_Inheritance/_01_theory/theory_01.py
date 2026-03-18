class BaseModel:
    def __init__(self, m_id):
        self.__m_id = m_id

    @property
    def m_id(self):
        return self.__m_id

    def save(self):
        print(f'Объект с id {self.m_id} сохранен в БД')


class UserModel(BaseModel):
    def __init__(self, m_id, name):
        super().__init__(m_id)
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'Пользователь {self.m_id}, name: {self.name}'


if __name__ == '__main__':
    user = UserModel(1, "Alice")
    user.save()
    print(user)
    print(issubclass(UserModel, BaseModel))
    print(isinstance(user, UserModel))
    print(isinstance(user, BaseModel))

    base_model = BaseModel(2)
    print(isinstance(base_model, UserModel))
    print(isinstance(base_model, BaseModel))
