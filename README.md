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
  
  The values for a-f are based on existing columns in the data. For g-i, you will need to generate new columns which derives information from existing ones. Replace the missing numeric values    with the mean for that column. Display the first 10 rows of this dataframe.

3. Displays the following information:
   
  3.1 Mean and standard deviation of College Enrollment Rate for High Schools 
  
  3.2 Mean and standard deviation of Student_Count_Total for non-High Schools 
  
  3.3 Distribution of starting hours for all schools d. Number of schools outside of the Loop Neighborhood (i.e., outside of zip codes 60601,60602, 60603, 60604, 60605, 60606, 60607, and 60616)
