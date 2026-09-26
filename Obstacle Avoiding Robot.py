# Obstacle Avoiding Robot using Python

def obstacle_avoiding_robot(distance):
print("\n===== OBSTACLE AVOIDING ROBOT =====")
print(f"Distance from obstacle: {distance} cm")

```
if distance > 30:
    print("No obstacle detected.")
    print("Robot: Moving FORWARD")

elif distance > 15:
    print("Obstacle detected nearby.")
    print("Robot: Slowing down")

else:
    print("Obstacle too close!")
    print("Robot: STOP")
    print("Robot: Turning RIGHT")
```

while
