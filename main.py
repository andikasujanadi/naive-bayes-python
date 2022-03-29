import os
import csv
from collections import Counter

#clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

def csv_to_array(file_loc):
    #print table 
    print_table = False
    label = None
    ar = []
    column_count = 0
    with open(file_loc) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                label = row
                column_count = len(row)
                if print_table:
                    print(f'{", ".join(row)}\n')
                line_count += 1
            else:
                ar.append(row)
                if print_table:
                    print(f'{", ".join(row)}')
                line_count += 1
        if print_table:
            print(f'\nProcessed {line_count} lines.\n')
    return label,ar,line_count-1,column_count

def transpose(ar,col, properties = False):
    val = []
    for row in ar:
        val.append(row[col])
    if properties:
        return list(dict.fromkeys(val))
    return val

#how many value in a goal
def value_in_goal(label_index,label,goal,data):
    value = 0
    for i in range(len(data)):
        goals = data[i][len(data[i])-1]
        property = data[i][label_index]
        if goals == goal and property == label:
            # print(f'{property} - {goals}')
            value += 1

    return value


def main():
    #read csv
    label,data,row,col = csv_to_array('data.csv')
    data_transpose = []

    #get properties (long,short,small, medium, etc)
    properties = []
    for i in range(col):
        data_transpose.append(transpose(data,i))
        properties.append(transpose(data,i,True))
    
    #get goal property
    goal = properties[len(properties)-1]
    
    #get count number for each property
    values = []
    for i in range(col):
        values.append(dict(Counter(data_transpose[i])))

    #print available data 
    print_data = False
    if print_data:
        print()
        print(f'raw array : {data}\n')
        print(f'row       : {row}\n')
        print(f'col       : {col}\n')
        print(f'properties: {properties}\n')
        print(f'label     : {label}\n')
        print(f'values    : {values}\n')
        print(f'goal      : {goal}\n')
        print()

    #get input user for prediction
    choices = []
    print('Naïve Bayes Algoritm\n'
        'Author: Andika Sujanadi\n\n'
        f'determine {label[len(label)-1]}\n'
        )
    print("PLEASE INPUT THE INDEX EACH CATEGORY\n")

    for i in range(len(label)-1):
        print(f'{label[i]} ',end='[')

        for j in range(len(properties[i])):
            
            if j != 0:
                print(end=', ')

            print(f'{properties[i][j]}({j})',end='')

        print(end=']')
        choices.append(int(input(" = ")))
        print()

    print()
    
    #starting fact
    print('fact:\n')
    for i in range(len(goal)):
        print(f'P({label[len(label)-1]}={goal[i]}) = {values[len(values)-1][goal[i]]}/{row}')
    print()

    #variable for result HMAP
    result = []

    #colecting more fact
    print('fact:\n')
    i=1
    for i in range(len(goal)):
        temp_result = 1
        for j in range(col-1):
            data_in_goal = value_in_goal(j,properties[j][choices[j]],goal[i],data)
            total_goal = values[len(values)-1][goal[i]]
            temp_result = temp_result * data_in_goal / total_goal
            print(f'P({label[j]} = {properties[j][choices[j]]} | '
                f'{label[len(label)-1]} = {goal[i]}) = '
                f'{data_in_goal}/{total_goal}')
        print()
        temp_result = temp_result * values[len(values)-1][goal[i]] / row
        result.append(round(temp_result,2))

    #HMAP
    print('HMAP: \n')
    for i in range(len(goal)):
        print('P(',end='')
        for j in range(col-1):
            if j != 0:
                print(end=', ')
            print(f'{label[j]} = {properties[j][choices[j]]}',end='')
        print(f' | {label[len(label)-1]} = {goal[i]}',end='')
        print(f') = {result[i]}')
    print()
    
    #answer
    max_value = max(result)
    index_max_value = result.index(max_value)
    print(f'{label[len(label)-1]} = {goal[index_max_value]}')

if __name__ == '__main__':
   main()
