# unlicense

# alpha world Animation Exporter

import os
import bpy
from math import degrees
from mathutils import *

"""
def get_pose_bone_matrix(pose_bone)
by: Graeme Hill's
http://graemehill.ca/exporting-armature-animation-with-the-blender-25-python-api/
"""

def get_pose_bone_matrix(pose_bone):
    if pose_bone.parent is None:
        return pose_bone.matrix_channel.transposed()
    else:
        return pose_bone.parent.matrix_channel.transposed() @ pose_bone.matrix_channel.transposed().inverted()
	
def export(filepath):
    file = open( filepath, 'w' )
    fscanf = file.write
    armature = [object for object in bpy.data.objects if object.type == 'ARMATURE']
    
    scene_context = bpy.context.scene
    
    if armature:
       for arm in armature:
           root = arm.data.bones
           range_frame = scene_context.frame_end - scene_context.frame_start + 1
           fscanf('frame ')
           if scene_context.frame_start == 0:
               fscanf('%i+0 \n' % (range_frame - 1))
           else:
               fscanf('%i \n' % range_frame)
           fscanf('fps ')
           fscanf('%i ' % scene_context.render.fps)
           fscanf('%.3f \n' % scene_context.render.fps_base)
           fscanf('\n')
                           
           for frame in range(range_frame+1):
               if frame == 0:
                   if scene_context.frame_start == 0:
                       fscanf('frameid %d\n' % frame)
                       scene_context.frame_set(frame)
                       
                       for pose_bone in arm.pose.bones:
                           pose_bone_rotation = get_pose_bone_matrix(pose_bone).to_euler() 
                       
                           id = root.find(pose_bone.name)
                           fscanf('boneid %d\n' % id)
                           local_euler = pose_bone.matrix_channel.to_euler()
                           fscanf('rotation ')                   
                           if pose_bone.parent is None:
                               fscanf('%.3f %.3f %.3f \n' % ( -pose_bone_rotation[0], -pose_bone_rotation[2], -pose_bone_rotation[1]))
                           else:
                               fscanf('%.3f %.3f %.3f \n' % ( -pose_bone_rotation[0], -pose_bone_rotation[2], -pose_bone_rotation[1]))
                           
                       fscanf('\n')
               else:
                   fscanf('frameid %d\n' % frame)
                   scene_context.frame_set(frame)
                   
                   for pose_bone in arm.pose.bones:
                       pose_bone_rotation = get_pose_bone_matrix(pose_bone).to_euler() 
                       
                       id = root.find(pose_bone.name)
                       fscanf('boneid %d\n' % id)
                       local_euler = pose_bone.matrix_channel.to_euler()
                       fscanf('rotation ')                   
                       if pose_bone.parent is None:
                           fscanf('%.3f %.3f %.3f \n' % ( -pose_bone_rotation[0], -pose_bone_rotation[2], -pose_bone_rotation[1]))
                       else:
                           fscanf('%.3f %.3f %.3f \n' % ( -pose_bone_rotation[0], -pose_bone_rotation[2], -pose_bone_rotation[1]))
                       
                   fscanf('\n')    
               
    file.close()

    return {'FINISHED'}

