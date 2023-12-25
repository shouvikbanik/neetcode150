def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    linear_matrix = []
    for row in range(len(matrix)):
        linear_matrix.extend(matrix[row])
    if target in linear_matrix:
        return True
    else:
        return False
