# Fuzzy Logic on IRIS classification

# Introduction
Iris is a flower data set which include three different species setosa, virginica andversicolor. This three species are distinguished by four features which are sepallength, sepal width, petal length and petal width. I build membership functions for this four different features. The code supports any number of rules, inputs, antecedents and implication operators. Fuzzy set-valued ouputs and corresponding defuzzified outputs would all be displayed. The best accuracy for the iris data classification is 97.33%.

# Procedure to run
  * **Input the implication operator** which are Lukasiewicz, Minimum and Product.
  * **Input any number of  antecedents.** For example, you can input "sl 1 sw 2 pl 3 pw 1". sl, sw, pl and pw represent sepal length, sepal width, pedal length and pedal width respectively. The number from 1 to 3 represent the low, medium and long in the membership function. The above input could be translated into "If sepal length is small and sepal width is large and pedal length is long and pedal width is narrow." Besides, any number of antecedents would be supported. The use could input whatever number of antecedents they want like "sl 1 pl 3".
  * **Input corresponding consequent.** The consequent is setosa, versicolor and virginica which are represented by C1, C2 and C3.
  * **Input any number of rules.** After setting the antecedents and their consequents, users could continue to input the rules until they type "!" to finish setting.
  * **Input real-valued test data.** Now, the user is able to input their own test data. The input number should be real-valued like 3.5, 1.2 and 0.2. The user could keep testing by input different data until the user type "!" to stop the program.

# Flowchart
<p align="center">
  <img width="493" height="481" src="https://github.com/HaoGitCode/Fuzzy-Logic-on-IRIS-classification/blob/master/fuzzy_flowcahrt.png">
</p>

# Suggested input rules


<table>
    <thead>
        <tr>
            <th>Species</th>
            <th>Rules  </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3> Setosa </td>
            <td>If sepal length is small and sepal width is large and pedal length is low and pedal width is narrow</td>
        </tr>
        <tr>
            <td>If sepal length is medium and sepal width is large and pedal length is low and pedal width is narrow</td>
        </tr>
        <tr>
            <td>If sepal length is low and sepal width is narrow and pedal length is low and pedal width is narrow </td>
        </tr>
        <tr>
            <td rowspan=5> Versicolor </td>
            <td>If sepal length is low and sepal width is narrow and pedal length is medium and pedal width is medium</td>
        </tr>
        <tr>
            <td>If sepal length is medium and sepal width is medium and pedal length is medium and pedal width is medium</td>
        </tr>
        <tr>
            <td>If sepal length is long and sepal width is wide and pedal length is medium and pedal width is medium </td>
        </tr>
        <tr>
            <td>If sepal length is long and sepal width is medium and pedal length is medium and pedal width is medium </td>
        </tr>
        <tr>
            <td>If sepal length is medium and sepal width is narrow and pedal length is medium and pedal width is medium </td>
        </tr>
    </tbody>
    
    
</table>
