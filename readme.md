### Inventory Records

This program allows the user to choose an unlimited number of items to be 
recorded. It outputs the most expensive item, average cost per item, total 
expenses and total tax deductible.


### To run the program under Shell

1. A "shebang" line is already included on the first line of the program 
which indicates the location of the Python interpreter on the hard drive.

 #!/usr/bin/env python3
 
2. You must then make the script executable, using the following command:

 chmod +x exp.py

3. You can run the program by invoking the Python interpreter manually 
as follows:

 python exp.py


### Program instructions

1. The program will ask you how many items you would like to record. Please
input a non-negative integer otherwise a ValueError will be triggered.

2. Item 1: log will then appear and you will be asked to enter the cost for
the item. Accepted input are only non-negative decimal numbers otherwise a 
ValueError will be triggered.

3. Then enter how many items used. Accepted input are only non-negative 
integers otherwise a ValueError will be triggered.

4. Next there is a Yes or No option if the item is tax deductible. Please 
input only a Yes or No starting letter in either lowercase or uppercase.

5. The whole process will be repeated until the number of items reaches your 
specified count.

6. A summary will be shown once all items has been logged in. You will see
information on: most expensive item, average cost per item, total expenses
and total tax deductible.
