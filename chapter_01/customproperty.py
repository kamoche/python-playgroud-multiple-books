
def quantity(attr_name):

    def qty_getter(instance):
        return instance.__dict_[attr_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict_[attr_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


