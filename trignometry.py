import math

def trig_calculator():
    print("📐 Python Trigonometric Value Calculator 📐")
    
    try:
        # 1. Get angle in degrees and convert to radians
        degrees = float(input("Enter the angle in degrees (e.g., 30, 45, 90): "))
        radians = math.radians(degrees)
        
        print("\nResults:")
        
        # 2. Calculate standard functions
        # Rounding to 4 decimal places fixes floating-point precision issues (like sin(180) showing as 1e-16)
        sin_val = round(math.sin(radians), 4)
        cos_val = round(math.cos(radians), 4)
        
        print(f"🔹 sin({degrees}°) = {sin_val}")
        print(f"🔹 cos({degrees}°) = {cos_val}")
        
        # 3. Handle undefined Tan cases (e.g., 90, 270 degrees)
        if degrees % 180 == 90:
            print("🔹 tan({degrees}°) = Undefined (Infinity)")
        else:
            tan_val = round(math.tan(radians), 4)
            print(f"🔹 tan({degrees}°) = {tan_val}")
            
    except ValueError:
        print("Please enter a valid numerical angle.")

if __name__ == "__main__":
    trig_calculator()
