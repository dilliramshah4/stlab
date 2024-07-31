#4) Design and develop a program in a language of your choice to solve the triangle problem
#defined as follows: Accept three integers which are supposed to be the three sides of a
#triangle and determine if the three values represent an equilateral triangle, isosceles
#triangle, scalene triangle, or they do not form a triangle at all. Assume that the upper limit
#for the size of any side is 10. Derive test cases for your program based on boundary-value
#analysis, equivalence class partitioning and decision-table approach and execute the test
#cases and discuss the results.






def classify_triangle(side_a, side_b, side_c):
    """
    Classify a triangle based on its sides.
    
    Args:
    side_a (int): Side A of the triangle
    side_b (int): Side B of the triangle
    side_c (int): Side C of the triangle
    
    Returns:
    str: The type of triangle (Equilateral, Isosceles, Scalene, or Not a Triangle)
    """
    
    # Boundary Value Analysis: Check for valid input
    if not (0 < side_a <= 10 and 0 < side_b <= 10 and 0 < side_c <= 10):
        return "Invalid input. Sides must be positive integers no larger than 10."
    
    # Check if the sides can form a triangle using the triangle inequality theorem
    if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
        return "Not a Triangle"
    
    # Equivalence Class Partitioning
    if side_a == side_b == side_c:
        return "Equilateral triangle"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

# Test Cases
test_cases = [
    (0, 0, 0),       # Invalid input
    (1, 1, 1),       # Equilateral triangle
    (1, 1, 10),      # Not a Triangle
    (1, 10, 1),      # Not a Triangle
    (10, 10, 10),    # Equilateral triangle
    (10, 10, 11),    # Not a Triangle
    (2, 2, 2),       # Equilateral triangle
    (2, 3, 2),       # Isosceles triangle
    (2, 3, 4),       # Scalene triangle
    (10, 10, 5),     # Isosceles triangle
    (10, 5, 10),     # Isosceles triangle
    (3, 3, 3),       # Equilateral triangle
    (3, 4, 3),       # Isosceles triangle
    (3, 4, 5),       # Scalene triangle
    (5, 5, 10),      # Not a Triangle
]

for test_case in test_cases:
    print(f"Test Case: {test_case} -> {classify_triangle(*test_case)}")
