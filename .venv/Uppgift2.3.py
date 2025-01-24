#3a
filmNames = ["Film name 1", "Film name 2", "Film name 3", "Film name 4"]
print(filmNames)

#3b
filmNames.append("Fellowship of the ring")
print(filmNames)

#3c
filmNames.insert(0, "The two towers")
print(filmNames)

#3d
print(filmNames.index("Fellowship of the ring"))

#3e
filmNames.pop(0)
print(filmNames.index("Fellowship of the ring"))

#3f
print(len(filmNames))

#3g
filmNames.reverse()
print(filmNames)

#3h
filmNames.sort()
print(filmNames)