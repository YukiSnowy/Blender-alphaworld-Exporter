# unlicense

# alpha world Mesh Exporter

import os
import bpy
import bmesh

def export(filepath, normal, texture):
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

        print('pos = ',obj.location)

        fscanf('// x y z ')
        if(normal):
            fscanf('nx ny nz ')
        if(texture):
            fscanf('u v ')
        numvert = len(mesh.vertices)
        fscanf('\n')

        fscanf(' ')
        fscanf('\n')

        vert = mesh.vertices
        
        print('polygons: ',len(mesh.polygons))

        uv_layer = obj.data.uv_layers.active
        index = 0
        for face in mesh.polygons:
            t = obj.data.loop_triangles
            fscanf('%.3f %.3f %.3f ' % ((vert[face.vertices[0]].co[0]+obj.location[0]), (vert[face.vertices[0]].co[2]+obj.location[2]), (vert[face.vertices[0]].co[1]+obj.location[1])))
            if(normal):
                fscanf('%.3f %.3f %.3f ' % ((vert[face.vertices[0]].normal[0]), (vert[face.vertices[0]].normal[2]), (vert[face.vertices[0]].normal[1])))
            if(texture):
                fscanf("%.3f %.3f " % (uv_layer.data[0+index].uv[0], 1-uv_layer.data[0+index].uv[1]))
            fscanf('\n')
            
            fscanf('%.3f %.3f %.3f ' % ((vert[face.vertices[2]].co[0]+obj.location[0]), (vert[face.vertices[2]].co[2]+obj.location[2]), (vert[face.vertices[2]].co[1]+obj.location[1])))
            if(normal):
                fscanf('%.3f %.3f %.3f ' % ((vert[face.vertices[2]].normal[0]), (vert[face.vertices[2]].normal[2]), (vert[face.vertices[2]].normal[1])))
            if(texture):
                fscanf("%.3f %.3f " % (uv_layer.data[2+index].uv[0], 1-uv_layer.data[2+index].uv[1]))
            fscanf('\n')
            
            fscanf('%.3f %.3f %.3f ' % ((vert[face.vertices[1]].co[0]+obj.location[0]), (vert[face.vertices[1]].co[2]+obj.location[2]), (vert[face.vertices[1]].co[1]+obj.location[1])))
            if(normal):
                fscanf('%.3f %.3f %.3f ' % ((vert[face.vertices[1]].normal[0]), (vert[face.vertices[1]].normal[2]), (vert[face.vertices[1]].normal[1])))
            if(texture):
                fscanf("%.3f %.3f " % (uv_layer.data[1+index].uv[0], 1-uv_layer.data[1+index].uv[1]))
            fscanf('\n')
            
            index = index+3

    file.close()

    return {'FINISHED'}
		 
