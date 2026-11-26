# test_module_with_output.py

PI = 3.141592

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# Example test code
print("get_circumference(10):", get_circumference(10))
print("get_circle_area(10):", get_circle_area(10))
