D1={}
print("empty dictionary",D1)

D2={'abc':3 , 'xyz':5}
print("\ndictionary with 2 key and value pairs",D2)
print(D2.keys())
print(D2.values())
print(D2.items())
print(D2.copy())
print(D2.update())
#print(D2.get(key,default))
print(D2['abc'])

D3={'marks':{'maths':50, 'physics': 60 , 'gk':70}}
print("\nnested dictionary ",D3)

D4=dict(name='dhana',age=40)
print(f"\n{D4}")

D5=dict(zip(('a','b','c'),(10,20,30)))
print(f"\n{D5}")

D6=dict.fromkeys(['a','b'])
print(f"\n{D6}")
