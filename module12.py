# 1. Друзья.
#
# Создайте класс "Friends", который должен содержать данные о людях (их имена) и о связях между ними.
# Имена представлены в виде текстовых строк, чувствительных к регистру.
# Связи не имеют направлений, то есть, если существует связь "sofia" с "nikola", это справедливо и в обратную сторону.
#
# class Friends(connections)
#
# Возвращает новый объект, экземпляр класса Friends.
# Параметр "connections" имеет тип "итерируемый объект", содержащий множества (set) с двумя элементами в каждом.
# Каждая связь содержит два имени в виде текстовых строк.
# Связи могут повторяться в параметре инициализации, но в объекте хранятся только уникальные пары.
# Каждая связь имеет только два состояния - присутствует или не присутствует.
#
# add(connection)
#
# Добавляет связь в объект. Параметр "connection" является множеством (set) из двух имен (строк).
# Возвращает True, если заданная связь новая и не присутствует в объекте.
# Возвращает False, если заданная связь уже существует в объекте.
#
# remove(connection)
#
# Удаляет связь из объекта. Параметр "connection" является множеством (set) из двух имен (строк).
# Возвращает True, если заданная связь существует в объекте.
# Возвращает False, если заданная связь не присутствует в объекте.
#
# names()
#
# Возвращает множество (set) имён. Множество содержит имена, которые имеют хотя бы одну связь.
#
# connected(name)
#
# Возвращает множество (set) имён, которые связаны с именем, заданным параметром "name".
# Если "name" не присутствует в объекте, возвращается пустое множество (set).

class Friends:

    name_connections = {}
    friend_connections = []

    def __init__(self, connections):
        for connection in connections:
            self.add(connection)

    def __str__(self):
        return str(self.friend_connections)

    def __repr__(self):
        return f'Friends({self.friend_connections})'

    def add(self, connection: set) -> bool:
        if connection in self.friend_connections:
            return False

        self.friend_connections.append(connection.copy())
        one_friend = connection.pop()
        other_friend = connection.pop()
        self.name_connections.setdefault(one_friend, set()).add(other_friend)
        self.name_connections.setdefault(other_friend, set()).add(one_friend)
        return True

    def remove(self, connection: set) -> bool:
        if connection not in self.friend_connections:
            return False

        self.friend_connections.remove(connection)
        one_friend = connection.pop()
        other_friend = connection.pop()
        self.name_connections[one_friend].discard(other_friend)
        self.name_connections[other_friend].discard(one_friend)
        return True

    def names(self):
        return set(self.name_connections.keys())

    def connected(self, name: str) -> set:
        return self.name_connections.setdefault(name, set())


some_dudes = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
print(str(some_dudes))
some_dudes.remove({'c', 'b'})
print(some_dudes.name_connections)
print(some_dudes.friend_connections)
print(some_dudes.names())
print(some_dudes.connected('b'))
