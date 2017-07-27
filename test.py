
u={'Z':34, 'Yui':45, 'Koi': 32}
tes = [(value, key) for (key, value) in sorted([(value,key) for (key,value) in u.items()])]
print (dict(tes))