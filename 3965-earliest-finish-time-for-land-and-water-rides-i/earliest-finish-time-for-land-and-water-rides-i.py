class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(
                    land_finish,
                    waterStartTime[j]
                )

                ans = min(
                    ans,
                    water_start + waterDuration[j]
                )

                # Water -> Land
                water_finish = (
                    waterStartTime[j]
                    + waterDuration[j]
                )

                land_start = max(
                    water_finish,
                    landStartTime[i]
                )

                ans = min(
                    ans,
                    land_start + landDuration[i]
                )

        return ans
