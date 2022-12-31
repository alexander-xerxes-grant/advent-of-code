class Node:
    def __init__(self, parent=None, size=None):
        self._parent = parent
        self._size = size
        self._children = {}

    @property
    def parents(self):
        return self._parent

    @property
    def children(self):
        return self._children


class DirBase(Node):
    def add_subdir(self, name):
        if name not in self._children:
            self._children[name] = Dir(self)

        return self._children[name]

    def add_file(self, name, size):
        if name not in self._children:
            self._children[name] = File(self, size)

        return self._children[name]

    @property
    def size(self):
        if self._size is None:
            self._size = sum(child.size for child in self._children_values())

        return self._size


class Dir(DirBase):
    def __init__(self, parent):
        if not isinstance(parent, DirBase):
            raise ValueError("Parent must be a subclass of type DirBase")

        super().__init__(parent)


class Root(DirBase):
    def __init__(self):
        super().__init__()


class File(Node):
    def __init__(self, parent, size):
        if not isinstance(parent, DirBase):
            raise TypeError("Parent must be a sblcass of type DirBase")

        if not isinstance(size, int):
            raise TypeError("Size my be of type int")

        super().__init__(parent, size)

    @property
    def size(self):
        return self._size
