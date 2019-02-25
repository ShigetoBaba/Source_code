def func_kwargs(**kwargs):
    print('kwargs: ', kwargs)
    print('type: ', type(kwargs))

kwargs = {"key1":1, "key2":2, "key3":3}
print(kwargs["key2"])
