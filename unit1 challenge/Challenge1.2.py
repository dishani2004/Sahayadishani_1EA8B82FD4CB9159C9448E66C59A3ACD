
def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False
    
year = 2014

if isLeapYear(year):
  print('{}is a loop year year.'.format(year))
else:
  print('{}is a not a leap year.'.format(year))