# Module created for matrix operations for the 3D renderer

def matMult(mat1, mat2):
	# Check for the sizes if they match (nxm) X (mxp) = nxp
	mat3 = []
	if (len(mat1[0]) == len(mat2)):
		for i in range(len(mat1)):
			temp = []
			total = 0
			for j in range(len(mat1[0])):
				total += mat2[j][0] * mat1[i][j]

			temp.append(total)
			mat3.append(temp)
	else:
		print("Invalid Matrix size")
		return None
	return mat3

def rotateMult(mat1, mat2):
	mat3 = []
	if (len(mat1[0]) == len(mat2)):
		for i in range(len(mat1)):
			temp = []
			total = 0
			for j in range(len(mat1[0])):
				total += mat2[j] * mat1[i][j]

			temp.append(total)
			mat3.append(temp)
	else:
		print("Invalid Matrix size")
		return None
	return mat3