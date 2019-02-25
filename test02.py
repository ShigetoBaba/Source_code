def func_kwargs(**kwargs):
    print('kwargs: ', kwargs)
    print('type: ', type(kwargs))

#d = {"key1":1, "key2":2, "key3":3}
func_kwargs(key1=1, key2=2, key3=3)
#func_kwargs(d)
#print(kwargs["key2"])
