def main():
    # Example usage - change these values as needed
    NUM_CUBES = 18    # Number of cubes
    RADIUS = 5.0     # Circle radius
    CUBE_SIZE = 0.5  # Size of each cube

    # Create the cubes

    from btest.make_circle import create_cubes_in_circle
    create_cubes_in_circle(NUM_CUBES, RADIUS, CUBE_SIZE)