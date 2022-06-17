import sys
import re

if len(sys.argv) == 2:
    growthfactor = 1.0
elif len(sys.argv) == 3:
    growthfactor = float(sys.argv[2])
else:
    print('usage: python obj2mc.py myobject.obj [growthfactor]')
    sys.exit(1)

obj = open(sys.argv[1])
json = open('./model/male.json', 'w')

#start with dummy coordinates because obj is one-indexed
coordinates = ['0.0,0.0,0.0']
normals =['0.0,0.0,0.0']
firstline = True #used to make sure the final face has no comma at the end
offset = 0.5 #makes the center of the block the origin, not the corner

json.write('''{
\t"vertexPositions": [
''')

for line in obj:
    # every vertex
    splitline = line.strip().split()
    if splitline and splitline[0] == 'v':
        coords = [float(splitline[1]), float(splitline[2]),
                  float(splitline[3])]
        for i in range(3):
            coords[i] = (coords[i] * growthfactor) + offset
            coords[i] = round(coords[i], 10)
        
        # ',x1,y1,z1'
        coord_string = ','.join(str(coord) for coord in coords)
        # coordinates = [0,0,0,x1,y1,z1,...]
        coordinates.append(coord_string)
    if splitline and splitline[0] == 'vn':
        v_normal = [float(splitline[1]), float(splitline[2]), float(splitline[3])]
        v_normal_string = ','.join(str(v) for v in v_normal)
        normals.append(v_normal_string)
    if splitline and splitline[0] == 'f':
        # each face has 4 vertices
        if(len(splitline)==5):
            for i in range(1, 5):
                # splitline[1] = '1/2/3' ---> [v1, vt1, vn1]
                splitline[i] = splitline[i].split('/')
            coord_ids = (int(splitline[1][0]), int(splitline[2][0]),
                        int(splitline[3][0]), int(splitline[4][0]))
            
            if firstline:
                firstline = False
            else:
                json.write(',')
            json.write(coordinates[coord_ids[0]])
            json.write(',')
            json.write(coordinates[coord_ids[1]])
            json.write(',')
            json.write(coordinates[coord_ids[2]])
            json.write(',')
            json.write(coordinates[coord_ids[0]])
            json.write(',')
            json.write(coordinates[coord_ids[2]])
            json.write(',')
            json.write(coordinates[coord_ids[3]])
        else:
            for i in range(1, 4):
                # splitline[1] = '1/2/3' ---> [v1, vt1, vn1]
                splitline[i] = splitline[i].split('/')
            coord_ids = (int(splitline[1][0]), int(splitline[2][0]),
                        int(splitline[3][0]))
            if firstline:
                firstline = False
            else:
                json.write(',')
            json.write(coordinates[coord_ids[0]])
            json.write(',')
            json.write(coordinates[coord_ids[1]])
            json.write(',')
            json.write(coordinates[coord_ids[2]])
json.write('''
\t],''')
json.write('''
\t"vertexNormals": [''')
#### write surface normals
obj.close()
obj = open(sys.argv[1])
firstline = True
for line in obj:
    splitline = line.strip().split()
    if splitline and splitline[0] == 'f':
        if (len(splitline)==5):
            for i in range(1, 5):
                # splitline[1] = '1/2/3' ---> [v1, vt1, vn1]
                splitline[i] = splitline[i].split('/')
            normal_ids = (int(splitline[1][2]), int(splitline[2][2]),
                        int(splitline[3][2]), int(splitline[4][2]))
            
            if firstline:
                firstline = False
            else:
                json.write(',')
            json.write(normals[normal_ids[0]])
            json.write(',')
            json.write(normals[normal_ids[1]])
            json.write(',')
            json.write(normals[normal_ids[2]])
            json.write(',')
            json.write(normals[normal_ids[0]])
            json.write(',')
            json.write(normals[normal_ids[2]])
            json.write(',')
            json.write(normals[normal_ids[3]])
        else:
            for i in range(1, 4):
                # splitline[1] = '1/2/3' ---> [v1, vt1, vn1]
                splitline[i] = splitline[i].split('/')
            normal_ids = (int(splitline[1][2]), int(splitline[2][2]),
                        int(splitline[3][2]))
            if firstline:
                firstline = False
            else:
                json.write(',')
            json.write(normals[normal_ids[0]])
            json.write(',')
            json.write(normals[normal_ids[1]])
            json.write(',')
            json.write(normals[normal_ids[2]])
json.write('''
\t],''')
json.write('''
\t"vertexFrontcolors": [''')
#### write surface normals
obj.close()
obj = open(sys.argv[1])
firstline = True
for line in obj:
    splitline = line.strip().split()
    if splitline and splitline[0] == 'f':
        if (len(splitline)==5):
            if firstline:
                firstline = False
            else:
                json.write(',')
            json.write('0.6784313725490196,0.6784313725490196,0.6901960784313725')
            json.write(',')
            json.write('0.6784313725490196,0.6784313725490196,0.6901960784313725')
            json.write(',')
            json.write('0.6784313725490196,0.6784313725490196,0.6901960784313725')
            json.write(',')
            json.write('0.6784313725490196,0.6784313725490196,0.6901960784313725')
            json.write(',')
            json.write('0.6784313725490196,0.6784313725490196,0.6901960784313725')
            json.write(',')
            json.write('0.6784313725490196,0.6784313725490196,0.6901960784313725')
        else:
            if firstline:
                firstline = False
            else:
                json.write(',')
            json.write('0.6784313725490196,0.6784313725490196,0.6901960784313725')
            json.write(',')
            json.write('0.6784313725490196,0.6784313725490196,0.6901960784313725')
            json.write(',')
            json.write('0.6784313725490196,0.6784313725490196,0.6901960784313725')
json.write('''
\t]
}''')

obj.close()
json.close()