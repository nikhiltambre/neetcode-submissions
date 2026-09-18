class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people array
        # people[i]=weight of ithperson
        # infinite boats
        # boat weight limit=limit
        # boats carries 2 people
        # p1+p2<=limit
        # 1<=p.len
        #Optimal
        people.sort()  # O(N logN)
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if left == right:
                if people[left] <= limit:
                    boats += 1
                break
            if people[left] + people[right] <= limit:
                left += 1
                boats += 1

            elif people[right] <= limit:
                boats += 1
            right -= 1
        return boats
