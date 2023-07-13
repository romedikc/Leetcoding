def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            if abs(a) > stack[-1]:
                stack.pop()
            elif abs(a) == stack[-1]:
                stack.pop()
                break
            else:
                break
        else:
            stack.append(a)
    return stack


asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))
