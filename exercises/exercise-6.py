# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year (Jan - Dec): ')
month_cut = month[0:3].lower()
day = int(input('Enter the day of the month: '))

if month_cut in ('jan', 'feb'):
    season = "Winter"
elif month_cut in ('apr', 'may'):
    season = "Spring"
elif month_cut in ('jul', 'aug'):
    season = "Summer"
elif month_cut in ('oct', 'nov'):
    season = "Fall"
elif month_cut in ('dec') and day >= 21:
    season = "Winter"
elif month_cut in ('dec') and day < 21:
    season = "Fall"
elif month_cut in ('jun') and day >= 21:
    season = "Summer"
elif month_cut in ('jun') and day < 21:
    season = "Spring"
elif month_cut in ('sep') and day >= 22:
    season = "Fall"
elif month_cut in ('sep') and day < 22:
    season = "Summer"
elif month_cut in ('mar') and day >= 20:
    season = "Spring"
elif month_cut in ('mar') and day < 20:
    season = "Winter"
else:
    season = ""
    print('Please enter a valid month.')

if season != "":
    print(f'{month} {day} is in {season}')