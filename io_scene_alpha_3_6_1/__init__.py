# unlicense

bl_info = {
    "name": "alpha world Model File Format (.mesh,.weight,.skel,.anim)",
    "author": "Pathomporn \"YukiSnowy\" Niamraksa",
    "version": (13, 8, 2023),
    "blender": (3, 6, 1),
    "location": "File > Import-Export",
    "description": "Export For The Adventure World, "
                   "Support: Mesh ,Animation",
    "category": "alpha world"}

if "bpy" in locals():
    import importlib
    if "export_mesh" in locals():
       importlib.reload(export_mesh)
    if "export_weight" in locals():
       importlib.reload(export_weight)
    if "export_skeleton" in locals():
       importlib.reload(export_skeleton)
    if "export_animation" in locals():
       importlib.reload(export_animation)

import bpy
import math
from bpy.types import Operator
from bpy.props import BoolProperty
from bpy_extras.io_utils import ExportHelper

class ExportMesh(Operator, ExportHelper):
    bl_idname = "export_scene.mesh"
    bl_label = "Export alpha world Mesh (.mesh)"
    bl_options = {'PRESET', 'UNDO'}

    filename_ext = ".mesh"
    
    normal: BoolProperty(
            name="Normal",
            description="",
            default=False,
            )
			
    texture: BoolProperty(
            name="Texture",
            description="",
            default=False,
            )			

    def execute(self, context):
        from . import export_mesh
        export_mesh.export(self.filepath,self.normal,self.texture)
        return {'FINISHED'}
    def draw(self, context):
        layout = self.layout
        #layout.use_property_split = True
        #layout.use_property_decorate = False

        sfile = context.space_data
        operator = sfile.active_operator

        layout.prop(operator, 'normal')
        layout.prop(operator, 'texture')


class ExportWeight(Operator, ExportHelper):
    bl_idname = "export_scene.weight"
    bl_label = "Export alpha world Weight (.weight)"
    bl_options = {'PRESET', 'UNDO'}

    filename_ext = ".weight"
			
    def execute(self, context):
        from . import export_weight
        export_weight.export(self.filepath)
        return {'FINISHED'}

class ExportSkeleton(Operator, ExportHelper):
    bl_idname = "export_scene.skel"
    bl_label = "Export alpha world Skeleton (.skel)"
    bl_options = {'PRESET', 'UNDO'}

    filename_ext = ".skel"

    def execute(self, context):
        from . import export_skeleton
        export_skeleton.export(self.filepath)
        return {'FINISHED'}
        
class ExportAnimation(Operator, ExportHelper):
    bl_idname = "export_scene.anim"
    bl_label = "Export alpha world Animation (.anim)"
    bl_options = {'PRESET', 'UNDO'}

    filename_ext = ".anim"

    def execute(self, context):
        from . import export_animation
        export_animation.export(self.filepath)
        return {'FINISHED'}
	
def menu_func_mesh_export(self, context):
    self.layout.operator(ExportMesh.bl_idname, text="alpha world Mesh (.mesh)")
def menu_func_weight_export(self, context):
    self.layout.operator(ExportWeight.bl_idname, text="alpha world Weight (.weight)")
def menu_func_skeleton_export(self, context):
    self.layout.operator(ExportSkeleton.bl_idname, text="alpha world Skeleton (.skel)")
def menu_func_animation_export(self, context):
    self.layout.operator(ExportAnimation.bl_idname, text="alpha world Animation (.anim)")

classes = (
    ExportMesh,
    ExportWeight,
    ExportSkeleton,
    ExportAnimation
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.TOPBAR_MT_file_export.append(menu_func_mesh_export)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_weight_export)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_skeleton_export)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_animation_export)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_mesh_export)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_weight_export)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_skeleton_export)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_animation_export)

if __name__ == "__main__":
    register()
