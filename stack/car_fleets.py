class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_sort = sorted(zip(position, speed), reverse=True)
        bottle_neck = float('-inf') # current speed set to lowest value
        fleets=0 # current fleet is set to 0
        for d,s in cars_sort:
            remaining = target-d
            time = remaining/s
            if time > bottle_neck:
                bottle_neck = time
                fleets +=1
        return fleets
