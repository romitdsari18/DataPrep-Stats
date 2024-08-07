# -*- coding: utf-8 -*-


#Importing necessary libraries
import pandas as pd 

#Loading the data into a pandas dataframe
df = pd.read_csv("cps.csv")

#Extracting the lowest and highest grades offered from the "Grades_Offered_All" column
df['Lowest Grade Offered'] = df['Grades_Offered_All'].apply(lambda x: str(x).split(",")[0])
df['Highest Grade Offered'] = df['Grades_Offered_All'].apply(lambda x: str(x).split(",")[-1])

#Defining a function to extract the starting hour from the 'School_Hours' column
def school_start_hours(data):
    result = str(data['School_Hours'])
    if result == 'nan':
        return result
    for i in range(len(result)):
        if result[i].isdigit():
            if i+1 < len(result) and result[i+1] == ':':
                return result[i]
            elif i+1 < len(result) and result[i+1].lower() == 'a':
                return result[i]
            elif i+1 < len(result) and result[i+1].lower() == 'p':
                return str(int(result[i]) + 12)
    return result

#Applying the 'school_start_hours' function to each row in the DataFrame to create a new column called 'Starting Hour'
df['Starting Hour'] = df.apply(lambda data: school_start_hours(data), axis=1)

#Replacing the missing values in the "College_Enrollment_Rate_School" column with the mean value of the column
college_enrollment_rate_mean = df['College_Enrollment_Rate_School'].mean()
df['College_Enrollment_Rate_School'] = df['College_Enrollment_Rate_School'].fillna(college_enrollment_rate_mean)

#Displaying the first 10 rows in the requried format
pd.options.display.max_columns = None
df_updated = df[["School_ID", "Short_Name", "Is_High_School", "Zip", "Student_Count_Total", "College_Enrollment_Rate_School", "Lowest Grade Offered", "Highest Grade Offered", "Starting Hour"]]
df_updated.index = pd.RangeIndex(start=0, stop=len(df_updated), step=1)
print(df_updated.head(10).to_string())
print("\n")

#Calculating the mean and standard deviation of college enrollment rates for high schools
high_schools_cer = df_updated.loc[df_updated['Is_High_School'], 'College_Enrollment_Rate_School']
mean_of_cer = high_schools_cer.mean()
std_of_cer = high_schools_cer.std()
print(f"College Enrollment Rate for High Schools = {mean_of_cer:.2f}, (sd = {std_of_cer:.2f})\n")

#Calculating the mean and standard deviation of total student count for non-high schools
non_high_schools_tsc = df_updated.loc[~df_updated['Is_High_School'], 'Student_Count_Total']
mean_of_tsc = non_high_schools_tsc.mean()
std_of_tsc = non_high_schools_tsc.std()
print(f"Total Student Count for Non-High schools = {mean_of_tsc:.2f}, (sd = {std_of_tsc:.2f})\n")

#Printing the distribution of starting hours for schools
print("Distribution of Starting Hours:")
dist_of_hours = [8,7, 9]
for hour in dist_of_hours:
    count = len(df_updated[df_updated['Starting Hour'].str.contains(str(hour))])
    print(f"{hour} am: {count}")

#Calculating the number of schools outside of the Loop area (specified by a list of zip codes)
loop_zips = [60601, 60602, 60603, 60604, 60605, 60606, 60607, 60616]
outside_loop = df_updated[~df_updated['Zip'].isin(loop_zips)]
out_of_loop = len(outside_loop)
print("\nNumber of schools outside Loop:", out_of_loop)



