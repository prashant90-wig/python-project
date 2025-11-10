def print_matrix(mat):
    for row in mat:
        print(row)

def transpose_matrix(mat):
    if len(mat)==0:
        raise ValueError("Matrix cannot be made empty!")
    result = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            row.append(mat[j][i])
        result.append(row)
    return result

def main():
    A = [[1,2],
        [3, 4]]
    
    B = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    
    print("Matrix A: ")
    print_matrix(A)

    print("Transpose of A: ")
    print_matrix(transpose_matrix(A))

    print("Matrix B: ")
    print_matrix(B)

    print("Transpose of B: ")
    print_matrix(transpose_matrix(B))

    
if __name__ == "__main__":
    main()

