#non primitive types are collection of primitive types

#list
print("List")
marksOfStudents =[ 23,45,16,2,5 ,5.67]
print(marksOfStudents[-3])
marksOfStudents.insert(1,94);
print("Before Sorting ",marksOfStudents)
marksOfStudents.sort();
print("After Sorting ",marksOfStudents)
marksOfStudents[0]=100;
print(marksOfStudents)

#Dictionary
print("\nDictionary")
marksOfStudents ={ "Surendra":48,"sonu":56,"Suri":90,"varun":89}
print(marksOfStudents)
print(marksOfStudents["varun"])

#Tuple
print("\nTuple")
monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May",
"Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# cannot modify. tuples are immutable
#monthsOfYear[0] = "Jan"
print(monthsOfYear)
date =input("Please enter the date to know month")
dateMonthYearInfo= date.split("/");
currentMonth=int(dateMonthYearInfo[1]);
print(" Month for your date is  ",monthsOfYear[currentMonth-1]);

