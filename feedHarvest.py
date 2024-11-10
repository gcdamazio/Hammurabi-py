import random
acers = 10
bushelsBeingUsedAsSeed = 40


def harvest(acres, bushelsBeingUsedAsSeed):
    yield_per_acre = random.randint(1, 7)
    print(str(yield_per_acre))
    harvested_bushels = (acres - bushelsBeingUsedAsSeed) * yield_per_acre
    return harvested_bushels
print(harvest(acers, bushelsBeingUsedAsSeed))