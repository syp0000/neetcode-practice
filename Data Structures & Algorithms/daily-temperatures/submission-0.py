class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        count = 0
        for x in range(len(temperatures)):
            
            while stack and temperatures[x] > temperatures[stack[-1]]:
                    prev= stack.pop()
                    output[prev] = x - prev
            stack.append(x)   
        return output


        