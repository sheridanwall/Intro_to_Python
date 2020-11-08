# Sheridan Wall
# October 26, 2020
# Homework 1

# Ask user their birth year using input 
# Age to integer
# Make a condition - if age is smaller than 2020, then print age by subtracting from 2020
year = input('What year were you born?')
year = int(year)
if year < 2020:
  print("You are" , 2020 - year , "years old")
# If user responds 2021 or higher, ask question again and repeat above steps
elif year > 2020:
     year = input("What year were you born?")
     year = int(year)
     print("You are" , 2020 - year , "years old")

# Human heart beat in a year = 35 million
age = 2020 - year
print("Since you were born, your heart has beaten aprroximately" , age * 35000000 , "times")
# Blue whale's heart beats 8 x a min , 525,600 mins/yr , blue whale in a yr = 4204800
print("Since you were a born, a blue whale's heart has beaten approximately" , age * 4204800 , "times")
# Rabbit's heart beats bw 140-180 a min approx. 160 per min; approx. 84096000
rabbit = age * 84096000
if rabbit > 1000000:
    print("Since you were born, a rabbit's heart has beaten approximately" , round(rabbit / 1000000) , "million times")
# Venus years = 225 days
print("You are" , round((age * 365)/225) , "years old on Venus")
# Neptune years = 165 Earth years = 60,225 days
print("You are" , round((age * 365)/60225 , 2) , "years old on Neptune")
# younger or older 
if age < 23:
    print("You are younger than me by" , 23 - age , "years")
elif age > 23:
    print("You are older than me by" , age - 23 , "years")
elif age == 23:
    print("You are the same age as me")
# Even/odd - modulo
if year % 2 == 0:
    print("You were born in an even year")
else:
    print("You were born in an odd year")
# democratic presidents - range function doesn't work, need to use statements like below 
if year > 1960 and year < 1963:
    print("There have been 5 Democratic presidents since you were born")
elif year > 1963 and year < 1977:
    print("There have been 4 Democratic presidents since you were born")
elif year > 1977 and year < 1993:
    print("There have been 3 Democratic presidents since you were born")
elif year > 1993 and year < 2009:
    print("There have been 2 Democratic presidents since you were born")
elif year > 2009 and year < 2016:
    print("There has been 1 Democratic president since you were born")
elif year > 2016: 
    print("There have been 0 Democratic presidents since you were born")
# president name - tried to make a dictionary & lists, but couldn't
if year > 1960 and year < 1963:
  print("John F. Kennedy was president when you were born")
elif year > 1963 and year < 1969:
  print("Lyndon B. Johnson was president when you were born")
elif year > 1969 and year < 1973:
  print("Richard Nixon was president when you were born")
elif year > 1973 and year < 1976:
  print("Gerald Ford was president when you were born")
elif year > 1976 and year < 1980:
  print("Jimmy Carter was president when you were born")
elif year > 1980 and year < 1988:
  print("Ronald Reagan was president when you were born")
elif year > 1988 and year < 1992:
  print("George Bush was president when you were born")
elif year > 1992 and year < 2000:
  print("Bill Clinton was president when you were born")
elif year > 2000 and year < 2008:
  print("George W. Bush was president when you were born")
elif year > 2008 and year < 2016:
  print("Barack Obama was president when you were born")
elif year > 2016:
  print("Donald Trump was president when you were born")
