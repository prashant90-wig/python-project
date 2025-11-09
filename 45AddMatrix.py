def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must be same size")
    
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result

def print_matrix(mat):
    for row in mat:
        print(row)

def main():
    A = [[1, 2],
         [3, 4]]
    
    B = [[5, 6],
         [7, 8]]
    
    print("Matrix A:")
    print_matrix(A)
    
    print("\nMatrix B:")
    print_matrix(B)
    
    print("\nA + B:")
    print_matrix(add_matrices(A, B))

if __name__ == "__main__":
    main()