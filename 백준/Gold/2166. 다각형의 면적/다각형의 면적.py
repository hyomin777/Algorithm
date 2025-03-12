import sys


input = sys.stdin.readline
N = int(input())

vertices = []
for _ in range(N):
    vertices.append(list(map(int, input().split())))
vertices.append(vertices[0])

area = 0
for i in range(N):
    area += (vertices[i][0] * vertices[i+1][1]) - (vertices[i+1][0] * vertices[i][1])

print((abs(area) / 2))