def squarert(x):
    return x ** (1/2)

points = []
for i in range(1, 7, 2):
    x, y = map(int, input(f"{i} ve {i+1}. sayıyı girin: ").split())
    points.append((x,y))

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = (squarert((x1 - x2)**2 + (y1 - y2)**2))
    return distance

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_dist = min(distances)

print(f"The minimum distance is: {min_dist}")