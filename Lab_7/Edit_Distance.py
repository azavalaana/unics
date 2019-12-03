# Method that returns the number of changes needed to change one word for another
def edit_distance(str1, str2):

    # 2D array with the length of both strings
    table = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]

    # First fill the first line and column
    for i in range(len(str1) + 1):
        table[0][i] = i

    for i in range(len(str2) + 1):
        table[i][0] = i

    # Loops to check how many changes are needed
    for i in range(len(str2)):
        for j in range(len(str1)):
            # If char are equal, use the diagonal value
            if str1[j] == str2[i]:
                table[i + 1][j + 1] = table[i][j]
            # If char are different, we get the smallest value from the surrounding 3 and add 1 to it.
            else:
                table[i+1][j+1] = min(table[i][j], table[i][j+1], table[i+1][j]) + 1

    # Return the total number of changes needed which is the bottom right value
    num_changes = table[len(str2)][len(str1)]

    return num_changes


