def asteroidsDestroyed(mass: int, asteroids: List[int]) -> bool:
    for a in sorted(asteroids):
        if mass < a:
            return False
        mass += a
    return True


mass = 10
asteroids = [3, 9, 19, 5, 21]
print(asteroidsDestroyed(mass, asteroids))
