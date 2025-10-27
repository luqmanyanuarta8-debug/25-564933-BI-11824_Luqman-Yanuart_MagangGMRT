import math

print("=== Program Forward Kinematics 2-DoF Robot Lengan ===")
print("Semua sudut dalam derajat (°)")
print()

L1 = float(input("Masukkan panjang lengan pertama (Femur): "))
L2 = float(input("Masukkan panjang lengan kedua (Tibia): "))

theta1_deg = float(input("Masukkan sudut servo 1 (θ1, dalam °): "))
theta2_deg = float(input("Masukkan sudut servo 2 (θ2, dalam °): "))

theta1 = math.radians(theta1_deg)
theta2 = math.radians(theta2_deg)

x = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
y = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)

print("\n=== HASIL PERHITUNGAN ===")
print(f"Panjang Femur (L1): {L1}")
print(f"Panjang Tibia (L2): {L2}")
print(f"Sudut Servo 1 (θ1): {theta1_deg}°")
print(f"Sudut Servo 2 (θ2): {theta2_deg}°")
print(f"Koordinat ujung kaki robot (x, y): ({x:.2f}, {y:.2f})")
