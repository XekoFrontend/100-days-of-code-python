def is_leap_year(year):
  """ Checking if the input year is the leap year"""
  divisible_4 = int(year) % 4
  divisible_100 = int(year) % 100
  divisible_400 = int(year) % 400
  if divisible_4 == 0:
    if divisible_100 == 0:
      if divisible_400 == 0:
        return True
      else:
        return False
    return True
  else:
    return False  

def year_from(star_year, end_year):
  """ Loop all year from range of input """
  empty_list = []
  for year in range(star_year, end_year + 1):
    check_year = is_leap_year(year)  
    if check_year == True:
      empty_list.append(str(year))
  return empty_list

leap_year = year_from(star_year=2000, end_year=2024)
print(f"Leap year are: {', '.join(leap_year)}")