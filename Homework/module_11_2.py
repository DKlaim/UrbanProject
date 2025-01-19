def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__
    info['attributes'] = dir(obj)
    info['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    info['module'] = getattr(obj, "__module__", None)

    return info

number_info = introspection_info(42)
print(number_info)

any_obj = introspection_info(introspection_info)
print(any_obj)
