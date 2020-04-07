import math

def distance(x1, y1, x2, y2):
        form = (x2-x1)**2+(y2-y1)**2
        dist = math.sqrt(form)
        distance = round(dist, 2)
        return distance