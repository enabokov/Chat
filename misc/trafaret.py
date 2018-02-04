import trafaret as t


def are_equal(main, extra, msg):

    def transform(value):
        assert isinstance(value, dict)

        data = value.copy()
        if data.get(main) != data.get(extra):
            return t.DataError(error={main: msg})
        data.pop(extra, None)
        return data

    return transform
