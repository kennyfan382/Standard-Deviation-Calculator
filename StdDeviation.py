import math

def getData():
    dataStr = input("Please enter your numbers below (seperate each number with a space): ").split() #Needs to be a str for the split method to turn the vals into an array
    if(dataStr == ["exit"]):
        exit()
    else: 
        data = [] #We will take the splits of the dataStr, convert them to ints, and put them here
        for num in dataStr:
            try:
                data.append(int(num))
            except ValueError as ValErr: #Incase the data isnt all ints
                print(ValErr)
                getData()
        method(data)

def mean(data): #Add all the data and divide it by its length
    sum = 0
    for num in data:
        sum += num
    mean = sum / len(data)
    return mean

def method(data):
    print(data)
    print(f"Mean: {mean(data)}")
    squares = [] #For holding the squared results of data - mean
    for num in data: #Subtract the mean and square that result
        subMean = num - mean(data)
        square = subMean * subMean #Square the result of the data being subtracted by the mean 
        squares.append(square)
    print(f"Your standard deviation for this data set is: {math.sqrt(mean(squares))}\n\n\n") #Find the mean of the square numbers, then the square root of that result

while True:
    getData() #type exit to leave