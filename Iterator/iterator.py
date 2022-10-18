from dataclasses import dataclass, field


@dataclass
class SimpleListIterator:

    _arr: list = field(default_factory=(lambda: []))

    def __iter__(self):
        self._current_index = 0
        return self

    def __next__(self):
        current = None
        try:
            current = self._arr[self._current_index]
        except:
            raise StopIteration
        self._current_index += 1
        return current
        