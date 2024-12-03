bl_info = {
    "name": "Circle Cube Generator",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Object > Generate Circle of Cubes",
    "description": "Creates cubes arranged in a circle",
    "category": "Object",
}

import bpy
from bpy.types import Operator, Menu
from bpy.props import IntProperty, FloatProperty
from .make_circle import create_cubes_in_circle

class OBJECT_OT_create_circle_cubes(Operator):
    """Create cubes arranged in a circle"""
    bl_idname = "object.create_circle_cubes"
    bl_label = "Generate Circle of Cubes"
    bl_options = {'REGISTER', 'UNDO'}
    
    num_cubes: IntProperty(
        name="Number of Cubes",
        description="Number of cubes to create",
        default=18,
        min=1,
        max=100
    )
    
    radius: FloatProperty(
        name="Circle Radius",
        description="Radius of the circle",
        default=5.0,
        min=0.1
    )
    
    cube_size: FloatProperty(
        name="Cube Size",
        description="Size of each cube",
        default=0.5,
        min=0.1
    )
    
    def execute(self, context):
        create_cubes_in_circle(self.num_cubes, self.radius, self.cube_size)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_create_circle_cubes.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_create_circle_cubes)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_circle_cubes)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()