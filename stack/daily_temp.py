class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #initializing an empty stack
        stack = []
        #initializing an empty array
        result  = [0]*len(temperatures) # way to initialize array

        #using enumerate to track index and temperature
        for i,temperature in enumerate(temperatures):
            #stack is not empty and temperatures is less then last element
            while stack and temperatures[stack[-1]]<temperature:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i) 
        return result
