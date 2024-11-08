from collections import OrderedDict


class SortedDict(OrderedDict):
    def __init__(self, **kwargs):
        super(SortedDict, self).__init__()

        for key, value in sorted(kwargs.items()):
            if isinstance(value, dict):
                self[key] = SortedDict(**value)
            else:
                self[key] = value
