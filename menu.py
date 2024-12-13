import bpy
from bpy.props import FloatProperty, IntProperty
from bpy.types import Operator

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
    ) # type: ignore
    
    radius: FloatProperty(
        name="Circle Radius",
        description="Radius of the circle",
        default=5.0,
        min=0.1
    ) # type: ignore
    
    cube_size: FloatProperty(
        name="Cube Sizes",
        description="Size of each cubes",
        default=0.5,
        min=0.1
    ) # type: ignore
    
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
