class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif int(key) in self:
                key = int(key)
            elif str(key) in self:
                key = str(key)
        except ValueError:
            pass
        return super().__getitem__(key)


slovnik = FlexibleDict()

slovnik[1] = "jablko"
slovnik['89'] = "hruška"

print(slovnik[1])
print(slovnik['1'])
print(slovnik[89])
print(slovnik.__class__)
slovnik()