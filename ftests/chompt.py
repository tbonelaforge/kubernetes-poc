import copy

import pprint

PP = pprint.PrettyPrinter(indent=4)


class Endpoint(object):
    def __init__(self, client_object, context):
        self.context = context
        self.dynamic_attributes = {}
        self.original_client_object = client_object
        for name in dir(self.original_client_object):
            if callable(getattr(self.original_client_object, name)):
                fn = getattr(self.original_client_object, name)
                self.dynamic_attributes[name] = self.create_wrapped_function(name, fn)

    def create_wrapped_function(self, original_name, fn):
        def wrapped_function(*args, **kwargs):
            expected_status_code = 200
            if 'status_code' in kwargs:
                expected_status_code = kwargs['status_code']
                del kwargs['status_code']
            result = fn(*args, **kwargs)
            assert result.status_code == expected_status_code, "Expected: %s, got: %s" % (
                expected_status_code,
                result.status_code
            )
            self.context.value = result
            return self.context
        return wrapped_function

    def __getattr__(self, item):
        value = self.__dict__.get(item, self.dynamic_attributes.get(item))
        return value


class Storage():
    def __init__(self):
        self.namespace = {}

    def __str__(self):
        return pp.pformat(self.namespace)

    def __repr__(self):
        return str(self)

    def store(self, key, value):
        self.namespace[key] = value

    def retrieve(self, *path):
        return Storage.follow_path(self.namespace, path)

    def resolve_leaf(self, value_or_path):
        resolved_value = None
        try:
            path = value_or_path.get_path()
            resolved_value = Storage.follow_path(self.namespace, path)
        except AttributeError:
            resolved_value = value_or_path
        return resolved_value

    def resolve(self, expr):
        if Storage.is_leaf(expr):
            resolved = self.resolve_leaf(expr)
            return resolved
        if isinstance(expr, dict):
            for key in expr:
                resolved = self.resolve(expr[key])
                expr[key] = resolved
            return expr
        if isinstance(expr, list):
            for i, x in enumerate(expr):
                resolved = self.resolve(x)
                expr[i] = resolved
            return expr
        raise AssertionError("Expression to resolve was not JSON")

    @staticmethod
    def follow_path(json_object, path):
            for key in path:
                json_object = json_object[key]
            return copy.deepcopy(json_object)

    @staticmethod
    def is_leaf(expr):
        if isinstance(expr, dict):
            return False
        if isinstance(expr, list):
            return False
        return True


class Chompt(object):
    def __init__(self):
        self.dynamic_attributes = {}
        self.value = None


    def __getattr__(self, item):
        value = self.__dict__.get(item, self.dynamic_attributes.get(item))
        return value


    def incorporate(self, client_object, field_name):
        self.dynamic_attributes[field_name] = Endpoint(client_object, self)


    def json(self, *path):
        json_value = self.value.json()
        json_value = Storage.follow_path(json_value, path)
        self.value = json_value
        return self


    def debug(self):
        printable_value = {
            "value": self.value,
        }
        PP.pprint(printable_value)
        return self
