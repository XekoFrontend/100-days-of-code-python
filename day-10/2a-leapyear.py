def is_leap_year(year):
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
  empty_list = []
  for year in range(star_year, end_year):
    check_year = is_leap_year(year)  
    if check_year == True:
      empty_list.append(year)
  return empty_list

leap_year = year_from(star_year=1992, end_year=2013)
print(f"Leap year are: {leap_year}")
