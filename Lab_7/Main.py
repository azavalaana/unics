from Edit_Distance import edit_distance


# Main program that compares two different strings
def main():
    # test case 1
    test1_str1 = "smart"
    test1_str2 = "stack"

    print("*** Test Case 1 ***")
    print("String 1: ", test1_str1)
    print("String 2: ", test1_str2)
    num_changes = edit_distance(test1_str1, test1_str2)
    print("\nTotal number of changes needed to get same strings: ", num_changes)

    # test case 2
    test2_str1 = "miners"
    test2_str2 = "market"

    print("*** Test Case 2 ***")
    print("String 1: ", test2_str1)
    print("String 2: ", test2_str2)
    num_changes = edit_distance(test2_str1, test2_str2)
    print("\nTotal number of changes needed to get same strings: ", num_changes)

    # test case 3
    test3_str1 = "frustration"
    test3_str2 = "resignation"

    print("*** Test Case 3 ***")
    print("String 1: ", test3_str1)
    print("String 2: ", test3_str2)
    num_changes = edit_distance(test3_str1, test3_str2)
    print("\nTotal number of changes needed to get same strings: ", num_changes)

main()