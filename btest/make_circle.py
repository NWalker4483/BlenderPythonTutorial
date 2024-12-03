import bpy
import math
import logging
from math import radians, pi

logger = logging.getLogger(__name__)

def delete_all_objects():
    """Delete all objects in the scene"""
    logger.debug("Deleting all objects from scene")
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    logger.info("All objects deleted")

def create_cubes_in_circle(num_cubes, radius, cube_size=1.0):
    """
    Create num_cubes cubes arranged in a circle with given radius
    
    Args:
        num_cubes (int): Number of cubes to create
        radius (float): Radius of the circle
        cube_size (float): Size of each cube (default: 1.0)
    """
    logger.info(f'Creating {num_cubes} cubes in circle with radius {radius}')
    
    # Delete existing objects
    # delete_all_objects()
    
    # Calculate angle between each cube
    angle_step = (2 * pi) / num_cubes
    logger.debug(f'Angle step between cubes: {angle_step} radians')
    
    # Create cubes
    for i in range(num_cubes):
        # Calculate position
        angle = i * angle_step
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        z = i + cube_size / 2  # Place cube so its bottom is on the ground
        
        logger.debug(f'Creating cube {i+1} at position ({x:.2f}, {y:.2f}, {z:.2f})')
        
        # Create cube
        bpy.ops.mesh.primitive_cube_add(
            size=cube_size,
            location=(x, y, z)
        )
        
        # Name the cube
        current_cube = bpy.context.active_object
        current_cube.name = f"Cube_{i+1}"
        logger.debug(f'Named cube as {current_cube.name}')
        
        # Optionally rotate cube to face center
        current_cube.rotation_euler.z = angle + radians(90)
        logger.debug(f'Rotated {current_cube.name} to face center')
    
    logger.info(f'Successfully created {num_cubes} cubes')