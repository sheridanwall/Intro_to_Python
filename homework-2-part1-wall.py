# Sheridan Wall
# Nov. 1, 2020
# Homework 2, Part 1


# Part One : Lists
numbers = [22 , 90 , 0 , -10 , 3 , 22 , 48]

# Number of elements
print(len(numbers)) 
    # 7 
# 4th element
print(numbers[3])
    # -10
# Sum of 2nd and 4th element
print(numbers[1] + numbers[3])
    #80
# 2nd largest value
print(sorted(numbers))
print(numbers[5])
    #22
# Last element
print(numbers[6])
    #48 unsorted & sorted
# Sum of all numbers / 2
print(sum(numbers)/2)
    #87.5
# Print if median or mean is higher --> Google searched for function
median_nums = print(len(numbers) // 2) #3
mean_nums = print(sum(numbers) / len(numbers)) #25
print("The mean is higher than the median")

# Part One : Dictionaries
movie = {
    'title' : 'Pretty Woman' ,
    'year' : '1990' ,
    'director' : 'Gary Marshall'
}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

# Add keys and find difference
movie['budget'] = 14000000
movie['revenue'] = 465000000

profit = movie['revenue'] - movie['budget']
print(profit)
# profit = 451,000,000

# Investment
if profit < movie['budget']:
    print("That was a bad investment")
if profit > (movie['budget'] * 5):
    print("That was a good investment")
else:
    print("That was on okay investment")

# NYC borough populations
borough_pops = {
    'manhattan' : 1600000 , 
    'brooklyn' : 2600000 , 
    'bronx' : 1400000 ,
    'queens' : 2300000 , 
    'staten' : 470000
}

print(borough_pops['brooklyn'])
# 2,600,000
total_pop = (sum(borough_pops.values()))
print(total_pop)
# Sum = 8,370,000
manhattan_pop = (borough_pops['manhattan'] / total_pop) * 100
print(round(manhattan_pop))
# 19 percent


