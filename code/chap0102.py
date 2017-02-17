import nsfg

preg = nsfg.ReadFemPreg()

print(preg.pregnum.value_counts().sort_index())

