# unlicense

# alpha world Skeleton Exporter

import os
import bpy
	
def export(filepath):
    file = open( filepath, 'w' )
    fscanf = file.write
    armature = [object for object in bpy.data.objects if object.type == 'ARMATURE']

    if armature:
        for arm in armature:
            root = arm.data.bones
            fscanf('bone ')
            fscanf('%i \n' % len(root))
            fscanf('\n')
          
            for bone in root:
                id = root.find(bone.name)
                fscanf('boneid %d\n' % id)
                fscanf('name %s\n' % bone.name)
                
                if bone.parent:
                    parentId = root.find(bone.parent.name)
                    fscanf('parent %d\n' % parentId)
                else:
                    fscanf('parent -1\n')
                    
                fscanf('head %.3f %.3f %.3f \n' % ( (bone.head_local[0]), (bone.head_local[2]), (bone.head_local[1]) ))
                fscanf('tail %.3f %.3f %.3f \n' % ( (bone.tail_local[0]), (bone.tail_local[2]), (bone.tail_local[1]) ))

                fscanf('\n')

    file.close()

    return {'FINISHED'}

