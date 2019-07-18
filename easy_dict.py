from copy import deepcopy


class EasyDictError(Exception):
    """Custom exception for working with EasyDict instances"""


class EasyAccessDict:
    def __init__(self, raw_data, make_copy=True):
        if make_copy:
            self.raw_data = deepcopy(raw_data)
        else:
            self.raw_data = raw_data

        if isinstance(self.raw_data, list):
            self.clean_data = [EasyAccessDict(v) if isinstance(v, dict) else v for v in self.raw_data]
        else:
            self.clean_data = self.raw_data

    def __getattr__(self, attribute_name):
        try:
            if attribute_name == 'first':
                if isinstance(self.clean_data, list):
                    return self.clean_data[0]

            value = self.clean_data[attribute_name]

            if isinstance(value, (dict, list)):
                return EasyAccessDict(value)

            return value

        except KeyError:
            raise EasyDictError('No attr/key called "{}"'.format(attribute_name))

    def get(self, key, default=None):
        try:
            return self.clean_data[key]
        except KeyError:
            return default

    @property
    def json(self):
        return self.raw_data

    def __getitem__(self, index):
        if isinstance(self.clean_data, list):
            return self.raw_data[index]
        else:
            raise ValueError('EasyDict __getitem__ "{}" failed!'.format(index))

    def __eq__(self, other):
        return self.raw_data == other.raw_data

    def __iter__(self):
        return iter(self.clean_data)

    def __str__(self):
        return str(self.raw_data)

    def __repr__(self):
        return str(self.raw_data)
