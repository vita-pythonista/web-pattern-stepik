# metaclass for automation change string of attribute to tuple (type_locator, locator)

class MetaLocator(type):
    def __new__(cls, name, bases, attrs):
        """When class is creating, class attribute will be checked and rebuild to tuple"""
        for key, value in attrs.items():
            if isinstance(value, str):
                if value.startswith(("//", ",//")):
                    attrs[key] = ("xpath", value)
                elif value.startswith(("#", ".", "input", "[", "td", "div")):
                    attrs[key] = ("css selector", value)
        return type.__new__(cls, name, bases, attrs)