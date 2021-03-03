#   THIS SCRIPT IS WRITTEN BY MATIN HUSEYNZADE AND FAKHRI JAFAROV. ALL RIGHTS RESERVED.
# https://github.com/chillmetin/iztech
# https://github.com/faxrij/

#1. Row Vector    ex: ( 1, 2, 3)

#2. Column Vector ex: [ 1, 2, 3]

#3. Matrix ex:
#  [ ( 1, 2, 3), ( 4, 5, 6) ]
#  ( [ 1, 4], [ 2, 5], [ 3, 6] )

#4. Augmented Matrix ex:
#   [ ( 1, 1, 0| 2), ( -2, 0, 1| 0) ]
#   ( [ 1, 4], [ 2, 5]| [ 3, 6] )


def row_vector(user_input):
    result = True
    paranthesis_check = (user_input.count('(') == user_input.count(')'))

    if user_input[:2] == '( ' and user_input[-1] == ')' and paranthesis_check:
        liste = user_input[1:-1].split(',')
    else:
        result = False
        return False

    for char in liste:
        if not char[0] == ' ' or char[-1] == ' ' or char.count(" ") > 1:
            result = False

    return result


def column_vector(user_input):

    result = True
    paranthesis_check = (user_input.count('[') == user_input.count(']'))

    if user_input[:2] == '[ ' and user_input[-1] == ']' and paranthesis_check:
        splitted_list = user_input[1:-1].split(',')
    else:
        result = False
        return False

    for i in splitted_list:
        if i[0] != ' ' or i[-1] == ' ' or i.count(" ") > 1:
            result = False

    return result


def matrix(input):
    result = True
    if input[:3] == "[ (" and input[-3:] == ") ]":  #row
        raw_input = user_input[2:-2]
        row_list = raw_input.split("), ")
        index = 0
        for entry in row_list:
            if entry[-1] != ")":
                row_list[index] += ")"

        entries_per_row = []
        for row in row_list:
            if result != False: result = row_vector(row)

            if entries_per_row != []:
                if entries_per_row[-1] != row.count(',') + 1:
                    return False
            entries_per_row.append(row.count(',') + 1)
            index += 1

    elif input[:3] == '( [' and input[-3:] == "] )":  #column
        result = True
        raw_input = user_input[2:-2]
        column_list = raw_input.split("], ")
        index = 0
        for entry in column_list:
            if entry[-1] != "]":
                column_list[index] += "]"
            index += 1
        entries_per_column = []
        for column in column_list:
            if result != False: result = column_vector(column)

            if entries_per_column != []:
                if entries_per_column[-1] != column.count(',') + 1:
                    return False
            entries_per_column.append(column.count(',') + 1)

    else:
        result = False

    return result


def augmented_matrix(input):
    result = True
    paranthesis_check = (input.count('[')
                         == input.count(']')) and (input.count('(')
                                                   == input.count(')'))
    if not paranthesis_check: return False

    if input[:3] == "[ (" and input[-3:] == ") ]":  #row
        form = "row"
        raw_rows = input[2:-2].split("), ")
        rows = []
        for row in raw_rows:
            if row[-1] != ")":
                rows.append(row + ")")
            else:
                rows.append(row)

        original_rows = tuple(rows)
        entries_per_row = []
        for entry in original_rows:
            if len(entries_per_row) != 0:
                if entries_per_row[-1] != entry.count(",") + entry.count(
                        "|") + 1:
                    result = False

            entries_per_row.append(entry.count(",") + entry.count("|") + 1)

        index = 0
        for row in rows:
            augment_index = row.index("|")
            row = row.replace('|', ',')
            if result != False: result = row_vector(row)

            index += 1

    elif input[:3] == '( [' and input[-3:] == "] )":  #column
        form = "column"
        if input.count("|") > 1: return False
        replaced_raw = input.replace("|", ",")
        augment_index = input.index("|")
        column_list = replaced_raw[2:-2].split("], ")
        index = 0

        for column in column_list:
            if column[-1] != "]":
                column_list[index] += ']'
            index += 1

        if result != False:
            for column in column_list:
                result = column_vector(column)

        entries_per_column = []
        for column in column_list:
            if entries_per_column != []:
                if column.count(", ") != entries_per_column[-1]:
                    result = False

            entries_per_column.append(column.count(", "))

    else:
        form = ''
        result = False

    return result


condition = True
while condition:

    user_input = input("check:\n\n")

    if "|" in user_input:
        input_type = 4  # Augmented Matrixp
        print('\n' + str(augmented_matrix(user_input)))

    elif user_input[:3] == '( [' or user_input[:3] == '[ (':
        input_type = 3  # Matrix
        print('\n' + str(matrix(user_input)))

    elif user_input[0] == '[':
        input_type = 2  # Column Vector
        print('\n' + str(column_vector(user_input)))

    elif user_input[0] == '(':
        input_type = 1  # Row Vector
        print('\n' + str(row_vector(user_input)))

    print(50 * '-' + '\n')
