import pygal
from Rolling.die import Die

die1 = Die()
die2 = Die(10)
results = []

for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequenics = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    '''用于统计在results中,每个点数各出现了多少次'''
    frequency = results.count(value)
    frequenics.append(frequency)

hist = pygal.Bar()

hist.title = "Result of rolling D6%D10 dice 50000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10', frequenics)
hist.render_to_file('Die_Visual.svg')
