class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=sorted(zip(position,speed),reverse=True)
        fleet=0
        slower_at_time=0

        for pos,spd in pairs:
            time=(target-pos)/spd

            if time > slower_at_time:
                fleet+=1
                slower_at_time=time
        return fleet