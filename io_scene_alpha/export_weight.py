# unlicense

# alpha world Weight Exporter

import os
import bpy
import bmesh

# // blendWeightsX blendWeightsY blendWeightsZ blendWeightsW blendIndicesX blendIndicesY blendIndicesZ blendIndicesW 

def export(filepath):
    file = open( filepath, 'w' )
    fscanf = file.write
	
    objList = [object for object in bpy.data.objects if object.type == 'MESH']
    for obj in objList:
        mesh = obj.data
    
        bm = bmesh.new()
        bm.from_mesh(mesh)
        bmesh.ops.triangulate(bm, faces=bm.faces)
        bm.to_mesh(mesh)
        mesh.calc_loop_triangles()
        bm.free()
        
        fscanf('blendWeightsX blendWeightsY blendWeightsZ blendWeightsW ')
        fscanf('blendIndicesX blendIndicesY blendIndicesZ blendIndicesW ')
        fscanf('\n')
        
        fscanf(' \n')
        
        vert = mesh.vertices

        for face in mesh.polygons:
            t = obj.data.loop_triangles
            
            t_1 = vert[face.vertices[0]]
            count_1 = 0
            for g in t_1.groups:
                fscanf('%.3f ' % g.weight)
                count_1 = count_1 + 1
            while count_1 < 4:
                fscanf('%.3f ' % 0.0)
                count_1 = count_1 + 1
                
            count_1 = 0
            for g in t_1.groups:
                fscanf('%d ' % g.group)
                count_1 = count_1 + 1
            while count_1 < 4:
                fscanf('%d ' % -1)
                count_1 = count_1 + 1
                
            fscanf('\n')
            
#==========================================================
            
            t_2 = vert[face.vertices[2]]
            count_2 = 0
            for g in t_2.groups:
                fscanf('%.3f ' % g.weight)
                count_2 = count_2 + 1
            while count_2 < 4:
                fscanf('%.3f ' % 0.0)
                count_2 = count_2 + 1
                
            count_2 = 0
            for g in t_2.groups:
                fscanf('%d ' % g.group)
                count_2 = count_2 + 1
            while count_2 < 4:
                fscanf('%d ' % -1)
                count_2 = count_2 + 1
                
            fscanf('\n')
            
#==========================================================
            
            t_3 = vert[face.vertices[1]]
            count_3 = 0
            for g in t_3.groups:
                fscanf('%.3f ' % g.weight)
                count_3 = count_3 + 1
            while count_3 < 4:
                fscanf('%.3f ' % 0.0)
                count_3 = count_3 + 1
                
            count_3 = 0
            for g in t_3.groups:
                fscanf('%d ' % g.group)
                count_3 = count_3 + 1
            while count_3 < 4:
                fscanf('%d ' % -1)
                count_3 = count_3 + 1
                
            fscanf('\n')
                    
    file.close()

    return {'FINISHED'}
		 
