import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y), where θ=theta.
def polar_to_cartesian(r,θ):
  x = r * math.cos(θ)
  x = round(x, 5)
  y = r * math.sin(θ)
  y = round(y, 5)
  return x,y
# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ) , where θ=theta.
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x,y):
  r = (x**2 + y**2)**0.5
  r = round(r, 5)
  θ = math.atan(y/x)
  θ = round(θ, 5)
  return r,θ

# Function 3 (40): Calculate the position of pendulum for (A, f, Φ, t), where Φ=phi.
# This function should take (A, f, Φ, t) as input and return the position value x=A*sin(2*π*f*t+Φ) .
def calculate_position(A, f, Φ, t):
  x = A * math.cos(2 * math.pi * f * t + Φ)
  x = round(x, 5)
  return x

