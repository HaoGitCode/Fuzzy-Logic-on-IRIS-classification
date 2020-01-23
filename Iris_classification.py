from sklearn.datasets import load_iris
import numpy as np
import statistics

# load the iris data
iris = load_iris()
features = iris.data.T  #   (4,150)

# load iris features
sepal_length = features[0]
sepal_width = features[1]
pedal_length = features[2]
pedal_width = features[3]

# find the boundary of each feature
slmax = [0] * 3;
slmin = [10] * 3;
swmax = [0] * 3;
plmax = [0] * 3;
pwmax = [0] * 3;
swmin = [10] * 3;
plmin = [10] * 3;
pwmin = [10] * 3;
for i in range(0,150):
    for j in range(0,3):
        if (iris.target[i] == j):
            if sepal_length[i] > slmax[j]:
                slmax[j] = sepal_length[i];
            if sepal_length[i] < slmin[j]:
                slmin[j] = sepal_length[i];

            if sepal_width[i] > swmax[j]:
                swmax[j] = sepal_width[i];
            if sepal_width[i] < swmin[j]:
                swmin[j] = sepal_width[i];

            if pedal_length[i] > plmax[j]:
                plmax[j] = pedal_length[i];
            if pedal_length[i] < plmin[j]:
                plmin[j] = pedal_length[i];

            if pedal_width[i] > pwmax[j]:
                pwmax[j] = pedal_width[i];
            if pedal_width[i] < pwmin[j]:
                pwmin[j] = pedal_width[i];

# find medium value for features
verginica_medw_temp = sepal_width[100:150]
verginica_medw = statistics.median(verginica_medw_temp)

versicolor_medl_temp = sepal_length[50:100]
versicolor_medl = statistics.median(versicolor_medl_temp)  # the sepal length medium of versicolor

# Membership for Pedal width
# width is narrow
def pw_narrow(x):
    if (x <= pwmax[0]) and (x >= pwmin[0]):
        return 1
    else:
        return 0
# width is medium
def pw_med(x):
    if (x >= pwmin[1]) and (x <= 1.3):
        return 1
    elif (x > 1.3) and (x <= pwmax[1]):
        return - 2 * float(x) + 3.6
    else:
        return 0
# width is wide
def pw_wide(x):
    if (x >= pwmin[2]) and (x <= 1.9): # 7.1 is the first number belong to verginica
        return 2 * float(x) - 2.8
    elif (x > 1.9) and (x <= pwmax[2]):
        return 1
    else:
        return 0

# Membership for Pedal length
# Length if low
def pl_low(x):
    if (x <= plmax[0]) and (x >= plmin[0]):
        return 1
    else:
        return 0
# Length is medium
def pl_med(x):
    if (x >= plmin[1]) and (x <= 4.4):
        return  1
    elif (x > 4.4) and (x <= plmax[1]):
        return  51 / 7 - float(x) * (10 / 7)
    else:
        return 0
# Length is long
def pl_long(x):
    if (x >= plmin[2]) and (x <= 5.2): # 7.1 is the first number belong to verginica
        return (float(x)*10)/7 - 45/7
    elif (x > 5.2) and (x <= plmax[2]):
        return 1
    else:
        return 0

# Membership for Sepal width
# width is narrow
def sw_narrow(x):
    if (x <= 2.1) and (x >= swmin[1]):
        return 1
    elif (x > 2.1) and (x <= swmax[1]):
        return - float(x) * (10 / 13) + 34 / 13
    else:
        return 0
# width is medium
def sw_med(x):
    if (x >= swmin[2]) and (x <= verginica_medw):
        return 1.25 * float(x) - 2.75
    elif (x > verginica_medw) and (x <= swmax[2]):
        return - 1.25 * float(x) + 4.75
    else:
        return 0
# width is wide
def sw_wide(x):
    if (x >= swmin[0]) and (x <= 3.9): # 7.1 is the first number belong to verginica
        return 0.625 * float(x) - 1.4375
    elif (x > 3.9) and (x <= swmax[0]):
        return 1
    else:
        return 0

# Membership for Sepal length
# Length if low
def sl_low(x):
    if (x <= 4.8) and (x >= slmin[0]):
        return 1
    elif (x > 4.8) and (x <= slmax[0]):
        return - float(x) + 5.8
    else:
        return 0
# Length is medium
def sl_med(x):
    if (x >= slmin[1]) and (x <= versicolor_medl):
        return  float(x) -4.9
    elif (x > versicolor_medl) and (x <= slmax[1]):
        return  70 / 11 - float(x) * (10 / 11)
    else:
        return 0
# Length is long
def sl_long(x):
    if (x >= slmin[2]) and (x <= 7.1): # 7.1 is the first number belong to verginica
        return (float(x)*5)/11 - 49/22
    elif (x > 7.1) and (x <= slmax[2]):
        return 1
    else:
        return 0

# Consequent Membership
def Setosa(x):
    if (x <= 1) and (x >= 0.5):
        return 2 * float(x) - 1
    elif (x <= 1.5) and (x >= 1):
        return - 2 * float(x) + 3
    else:
        return 0
def Versicolor(x):
    if (x <= 2) and (x >= 1.5):
        return 2 * float(x) - 3
    elif (x <= 2.5) and (x >= 2):
        return - 2 * float(x) + 5
    else:
        return 0
def Verginica(x):
    if (x <= 3) and (x >= 2.5):
        return 2 * float(x) - 5
    elif (x <= 3.5) and (x >= 3):
        return - 2 * float(x) + 7
    else:
        return 0

# Allow for three implication operators
end = 0
type = 3
while end == 0:
    operator = input("Input the opertor (Lukasiewicz, Minimum, Product) :")
    if operator == "Lukasiewicz":
        type = 0
        end = 1
    elif operator == "Minimum":
        type = 1
        end = 1
    elif operator == "Product":
        type = 2
        end = 1
    else:
        print("Input opertor ERROR.")

# Allow for any number of antecedents
print("Following could be stopped by type '!' ")
end = 0
num = 1
ante = []
Rout = []
while end == 0:
    print("Input Rule" + str(num) + " :")
    count = 1
    Antecedents = input("Input the antecedents (example: sl 1 sw 2 pl 3 pw 1):")
    if Antecedents == "!":
        end = 1
        continue
    Output = input("Input the Consequent (C1, C2, C3):")
    if Output == "!":
        end = 1
        continue
    ante.append(Antecedents)
    Rout.append(Output)
    num = num + 1
print("Input rules finished. Rule number is " + str(len(ante)))

# translate the user input rules
def translate(x, y):
    if x == "sl":
        if y == "1":
            return sl_low(sl)
        if y == "2":
            return sl_med(sl)
        if y == "3":
            return sl_long(sl)
    elif x == "sw":
        if y == "1":
            return sw_narrow(sw)
        if y == "2":
            return sw_med(sw)
        if y == "3":
            return sw_wide(sw)
    elif x == "pl":
        if y == "1":
            return pl_low(pl)
        if y == "2":
            return pl_med(pl)
        if y == "3":
            return pl_long(pl)
    elif x == "pw":
        if y == "1":
            return pw_narrow(pw)
        if y == "2":
            return pw_med(pw)
        if y == "3":
            return pw_wide(pw)
    else:
        print("translate error")

# implement three implication operators
def operate(x):
    length = len(x)
    sum = 0
    product = 1
    min = 100
    if type == 0:
        for i in range(0,length):
            sum += x[i]
        sum = sum - 1
        return max(sum,0)
    elif type == 1:
        for i in range(0, length):
            if x[i] < min:
                min = x[i]
        return min
    elif type == 2:
        for i in range(0, length):
            product = product * x[i]
        return product
    else:
        print("operate error")

print("=========Setting finished, Start teseting=======")
end = 0
while end == 0:
    # Allow for any number of inputs
    print("Enter the inputs.")
    sl = (input("Enter value for sepal length:"))
    sw = (input("Enter value for sepal width:"))
    pl = (input("Enter value for petal length:"))
    pw = (input("Enter value for petal width:"))

    # method to stop the program
    if sl == "!":
        end = 1
        break

    # set the value when there is no input for some features
    if sl == "n":
        sl == 10
    if sw == "n":
        sw == 10
    if pl == "n":
        pl == 10
    if pw == "n":
        pw == 10

    if sl != "n":
        sl = float(sl)
    if sw != "n":
        sw = float(sw)
    if pl != "n":
        pl = float(pl)
    if pw != "n":
        pw = float(pw)

    # store the input of consequent membership function
    result = np.zeros((3, 30))
    # store the output of each rules
    result1 = []
    result2 = []
    result3 = []
    for i in range(0,len(ante)):
        temp = []
        if(Rout[i] == "C1"):
            temp_ante = ante[i].split()
            temp_ante_length = len(temp_ante)
            for j in range(0,int(temp_ante_length * 0.5)):
                tempvalue = float(translate(temp_ante[2*j], temp_ante[2*j+1]))      # get output of features membership function
                temp.append(tempvalue)
            result1.append(operate(temp))       # implement implication operators on the membership function features

        if (Rout[i] == "C2"):
            temp_ante = ante[i].split()
            temp_ante_length = len(temp_ante)
            for j in range(0, int(temp_ante_length * 0.5)):
                tempvalue = float(translate(temp_ante[2 * j], temp_ante[2 * j + 1]))
                temp.append(tempvalue)
            result2.append(operate(temp))

        if (Rout[i] == "C3"):
            temp_ante = ante[i].split()
            temp_ante_length = len(temp_ante)
            for j in range(0, int(temp_ante_length * 0.5)):
                tempvalue = float(translate(temp_ante[2 * j], temp_ante[2 * j + 1]))
                temp.append(tempvalue)
            result3.append(operate(temp))

    # get the maximum value among different rules
    tempsamll1 = 0
    for i in range(0, len(result1)):
        if result1[i] > tempsamll1:
            tempsamll1 = result1[i]
    tempsamll2 = 0
    for i in range(0, len(result2)):
        if result2[i] > tempsamll2:
            tempsamll2 = result2[i]
    tempsamll3 = 0
    for i in range(0, len(result3)):
        if result3[i] > tempsamll3:
            tempsamll3 = result3[i]

    # aggregate all the consequent membership function
    for m in range(0, 30):
        temp = m + 5
        temp = temp * 0.1
        result[0][m] = min(Setosa(float(temp)), tempsamll1)
        result[1][m] = min(Versicolor(float(temp)), tempsamll2)
        result[2][m] = min(Verginica(float(temp)), tempsamll3)

    # aggregate the fuzzy output
    finalresult = [0] * 30
    for i in range(0, 30):
        finalresult[i] = max(result[0][i], result[1][i], result[2][i])

    # defuzzification
    degree = 0
    n = 0
    for x in range(0, 30):
        temp = x + 5
        temp = temp * 0.1
        degree += temp * finalresult[x]
        n += finalresult[x]

    if n == 0:
        print("Unknown species")
        continue

    output = float(degree) / float(n)
    output = round(output)

    # fuzzy set outout
    print("The fuzzy output is:")
    print(finalresult)

    # defuzzied value
    if output == 1:
        print("The flower is setosa.")
    elif output == 2:
        print("The flower is versicolor.")
    elif output == 3:
        print("The flower is virginica.")
    else:
        print("Unknown species")
