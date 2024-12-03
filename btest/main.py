from .make_circle import create_cubes_in_circle
from .menu import register

def main():
    stage=1
    if stage == 1:
        # Example usage - change these values as needed
        NUM_CUBES = 35    # Number of cubes
        RADIUS = 5.0     # Circle radius
        CUBE_SIZE = 0.5  # Size of each cube
    
        # Create the cubes
    
        create_cubes_in_circle(NUM_CUBES, RADIUS, CUBE_SIZE)
        
    if stage == 2:
        register()
