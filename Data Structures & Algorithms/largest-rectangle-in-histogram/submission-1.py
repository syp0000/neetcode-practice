class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # Stores pairs: (start_index, height)

        for current_index, current_height in enumerate(heights):
            start = current_index

            # While stack is not empty and the top height is greater than current_height
            while stack and stack[-1][1] > current_height:
                previous_start, previous_height = stack.pop()
                width = current_index - previous_start
                area = previous_height * width
                
                # Update max_area with the larger value between max_area and area
                max_area = max(max_area, area)
                
                # The current taller bar can extend back to where this shorter bar started
                start = previous_start

            # Push the new evaluated bar with its adjusted start index onto the stack
            stack.append((start, current_height))

        # For each remaining pair in the stack, calculate its area to the end of the histogram
        for start_index, height in stack:
            width = len(heights) - start_index
            area = height * width
            
            # Update max_area with the larger value between max_area and area
            max_area = max(max_area, area)
        return max_area