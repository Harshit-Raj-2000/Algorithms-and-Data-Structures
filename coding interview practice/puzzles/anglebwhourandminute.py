H,M = [int(x) for x in input().strip().split()]
M = M%60
M_angle = 6*M
H_angle = 30*H + 30*(M/60)
angle = int(max(M_angle,H_angle)-min(M_angle,H_angle))
angle = min(angle,360-angle)
print(angle)