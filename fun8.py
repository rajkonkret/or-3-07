def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)
allparams(1, 2, 3)  # 3
# allparams(b=5, a=7, c=9)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / - oddziela argumenty pozycyjne od takich co mogą byc podane tez po nazwie, a i b nie moze byc podane po nazwie
allparams(1, 2, c=9)  # c, d 9 256
# allparams(1, 2, c=9, 1, 2, 3, 4, 5, 6, 7)  # SyntaxError: positional argument follows keyword argumental
allparams(1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 0, 100)
# a, b 1 2
# c, d 3 256
# args (3, 4, 5, 6, 7, 8, 9, 0, 100)
wej1 = 1
allparams(wej1, 1, 2, 3, 4, 5, 6)
allparams(1, 2, 3, 3, 4, 5, 6, 7, 710, d=18)
# a, b 1 2
# c, d 3 18
# args (3, 4, 5, 6, 7, 710)
allparams(1, 2, 3, 3, 4, 5, 6, 7, 710, d=18, root="/")  # kwargs {'root': '/'}
allparams(1, 2, 3, 3, 4, 5, 6, 7, 710, d=18, root="/", user="Radek")  # kwargs {'root': '/', 'user': 'Radek'}
allparams(1, 2, 3, 3, 4, 5, 6, 7, 710, d=18, root="/", user="Radek", a=9)
# kwargs {'root': '/', 'user': 'Radek', 'a': 9}
# allparams(a=1, user="radek") bez /
# # a, b 1 0
# # c, d 42 256
# # args ()
# # kwargs {'user': 'radek'}
