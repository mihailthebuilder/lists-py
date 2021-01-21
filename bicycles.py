"""Lists chapter"""

BICYCLES = ["trek", "cannondale", "redline", "specialized"]
print(BICYCLES)

print(BICYCLES[0].title())

del BICYCLES[1]

print(BICYCLES[1])

BICYCLES.sort(reverse=True)
print(BICYCLES)
