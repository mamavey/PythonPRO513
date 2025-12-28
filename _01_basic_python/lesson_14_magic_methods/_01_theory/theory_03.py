class Group:

    def __init__(self, members: list[str]):
        self.members = members

    def __len__(self):
        return len(self.members)


if __name__ == '__main__':
    group_members = ['Иван', "Мария", "Петр"]
    group = Group(group_members)
    print(len(group))
