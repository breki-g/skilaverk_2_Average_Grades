totalWeightedGrades = 0
totalWeights = 0
maxGrade = 0
count = 0
weight = None
flag = False    #breyting
while True:
    grade = float(input())
    if grade == -1:
        break
    
    flag = True     #breyting

    weight = float(input())
    if weight !=0:
        totalWeightedGrades += grade * weight
    totalWeights += weight

    if grade > maxGrade:
        maxGrade = grade

    count += 1


if flag:    #breyting

    if count > 0:
        if totalWeights > 0:
            weightedAverage = totalWeightedGrades / totalWeights
            roundedWeightedAverage = round(weightedAverage, 2)
            print("Weighted average grade:", roundedWeightedAverage)
            print("Highest grade:", maxGrade)
        else:
            weightedAverage = 0

    if weight == 0:
        print("Highest grade:", maxGrade)
            
            #breyting endar

    
    