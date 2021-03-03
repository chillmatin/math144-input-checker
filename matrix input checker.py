#   THIS SCRIPT IS WRITTEN BY MATIN HUSEYNZADE AND FAKHRI JAFAROV. ALL RIGHTS RESERVED.




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
        if i[0] != ' ' or i[-1]==' ' or i.count(" ") > 1:
            result = False

    return result

def matrix(user_input):
    result = True
    for k in user_input:
        if k.count(" ") > 1:
            result = False
            return result
    paranthesis_check = (user_input.count('[') == user_input.count(']') and user_input.count('(') == user_input.count(')'))
    if user_input[-2]!=' ':
        result = False
        return result
    else:
        if paranthesis_check:
            
            if user_input[:3]=='[ (':
                new_List = user_input.strip('[ ').strip(' ]')
                new_list2 = new_List.split('), ')
                
                for i in new_list2:
                    if i[-1]!=')':
                        i+=')'
                    result = row_vector(i)
                    if result==False:
                        return result
                return result


            elif user_input[:3]=='( [':
                new_List = user_input.strip('( ').strip(' )')
                new_list2 = new_List.split('], ')
               
                for i in new_list2:
                    
                    if i[-1]!=']':
                        i+=']'
                        
                    result = column_vector(i)
                    if result==False:
                        return result
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
        input_type = 4        # Augmented Matrixp
        print('\n'+str(augmented_matrix(user_input)))



    elif user_input[:3]=='( [' or user_input[:3] == '[ (':
        input_type = 3        # Matrix 
        print('\n'+str(matrix(user_input)))
        

    elif user_input[0] == '[':
        input_type = 2        # Column Vector
        print('\n'+str(column_vector(user_input)))


    elif user_input[0] == '(':
        input_type = 1        # Row Vector
        print('\n'+str(row_vector(user_input)))
        

    print(50 * '-' + '\n')