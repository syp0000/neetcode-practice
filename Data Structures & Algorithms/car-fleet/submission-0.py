class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = set()
        for x in range(len(position)):
            cars.add((position[x],speed[x]))
        sorted_cars = sorted(cars,key=lambda item: item[0], reverse = True)
        print(sorted_cars)
        time = []
        fleet_time = []
        for position, speed in sorted_cars:
            time.append((target-position)/speed)
        for x in range(len(time)):
            if len(fleet_time) == 0:
                fleet_time.append(time[x])
            if time[x] <= fleet_time[-1]:
                continue
            if time[x] > fleet_time[-1]:
                fleet_time.append(time[x])
        return len(fleet_time)