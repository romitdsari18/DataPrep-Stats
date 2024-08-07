# DataPrep-Stats
To create a program in Python that performs the following: 
1. Loads the cps.csv file (assume it's in the current directory) and create a DataFrame object fromit.
   
2. Based on the data contained in the cps.csv file, generates a dataframe with the following information:

     2.1 School_ID 
  
     2.2 Short_Name 
  
     2.3 Is_High_School
  
     2.4 Zip
  
     2.5 Student_Count_Total 
  
     2.6 College_Enrollment_Rate_School
  
     2.7 Lowest Grade Offered (derived from Grades_Offered_All column)
  
     2.8 Highest Grade Offered (derived from Grades_Offered_All column) 
  
     2.9 Starting Hour (derived from School_Hours column) 
  
     The values for a-f are based on existing columns in the data. For g-i, you will need to generate new columns which derives information from existing ones. Replace the missing numeric           values with the mean for that column. Display the first 10 rows of this dataframe.

3. Displays the following information:
   
     3.1 Mean and standard deviation of College Enrollment Rate for High Schools 
  
     3.2 Mean and standard deviation of Student_Count_Total for non-High Schools 
  
     3.3 Distribution of starting hours for all schools d. Number of schools outside of the Loop Neighborhood (i.e., outside of zip codes 60601,60602, 60603, 60604, 60605, 60606, 60607, and 60616)

# Explaination

1.The code starts by importing the pandas library, which will be used to work with data in a tabular format. 

2. Then we used the pandas data frame to load the "cps.csv" file.

3. We have used the "Grades_Offered_All" column to extract the lowest and highest grades offered by each school and adds them as new columns in the data frame. 

4. Then we have defined a function called "school_start_hours" that extracts the starting hour from the "School_Hours" column for each row in the data frame. The function is applied to each row using the apply() method, and the resulting values are added to a new column called "Starting Hour".

5. Then we have replaced the missing values in the "College_Enrollment_Rate_School" column with the mean value of the column. 

6. It creates a new data frame containing only the columns required for output and displays the first 10 rows in the required format. 

7. We have calculated the mean and standard deviation of college enrollment rates for high schools, using Boolean indexing to select only the high schools from the data frame. 

8. In the similar way we have calculated the mean and standard deviation of total student count for non-high schools, using Boolean indexing to select only the non-high schools from the data frame. 

9. We have prints out a distribution of starting hours for schools, using a list of hours to count the number of schools starting at each hour. 

10. Finally, calculated the number of schools outside of the Loop area (specified by a list of zip codes), using Boolean indexing to select only the schools with zip codes outside of the Loop.

11. The number of such schools is printed to the console.
