import datetime as dt
# datetime kütüphanesini ekledik.
print(dt.datetime.now())

from datetime   import datetime
# datetime modülü içinden sadece datetime classını almak için bunu yaptık.
a = [3,6,8,9]
x = datetime.now()
print(type(x))
print(dt.datetime.now())