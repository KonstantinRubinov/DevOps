import csv
import sys

file_name=sys.argv[1] # prints var1
column_num=sys.argv[2] # prints var2
column_num=int(column_num)-1

line_count=0
mysum=0
col_name=""

in_range=True
has_data=False

with open(file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
       try:
           my_col=row[column_num]
           if line_count == 0:
               try:
                   col_name=my_col
               except ValueError:
                   pass
           else:
               try:
                   mysum += float(my_col)
                   has_data=True
               except ValueError:
                   pass
           line_count += 1
       except IndexError:
           col_data = (column_num+1)
           col_format_string = "there is no column %s"
           print(col_format_string % col_data)
           in_range=False
           break




        
if in_range:
    after_point = mysum - int(mysum)
    if has_data:
        if after_point == 0:
            mysum = int(mysum)
        data = (col_name, mysum)
        format_string = "The total %s is %s"
        print(format_string % data)
    else:
        data = (col_name)
        format_string = "The column %s has no numeric data"
        print(format_string % data)


            











  
