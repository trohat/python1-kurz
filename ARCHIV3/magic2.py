class MyList(list):
    def __getitem__(self, key):
        print (f"Klíč je {key}")
        return self[key]
        return "ale stejně máš smůlu"

    def __setitem__(self, key, value):
        print (f"Klíč je {key}")
        print (f"Hodnota je {value}")
        print("jdu to zapsat")
        super().__setitem__(key,value)

a = MyList()

print(type(a))

a.append(5)
a.append(6)
a.append(7)
a.append(8)
a[2] = "jablko"

print(a[3])
print(a[78])

print(a)