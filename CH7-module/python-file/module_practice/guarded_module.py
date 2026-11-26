# guarded_module.py

PI = 3.141592

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# 활용 예 (여기를 수정)
if __name__ == "__main__":
    print("get_circumference(10):", get_circumference(10))
    print("get_circle_area(10):", get_circle_area(10))
