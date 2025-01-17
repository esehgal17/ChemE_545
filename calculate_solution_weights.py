#the dictionary the function will work with
molecular_weights = {
'NaCl': 58.44,
'H2SO4': 98.079,
'NaOH': 40.00,
'KMnO4': 158.034,
'CH3COOH': 60.052
}
#the list of solutions needed that the function will work with
solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']

def calculate_solution_weights(molecular_weights, solutions_needed): #define the function name and the 2 inputs it will take in
    
    output_list = [] #initalize an empty list so you can append strings to it later in the code
    
    for solution in solutions_needed: #looping through each string in the list "solutions_needed"
        chemical_name = solution.split('-')[0] #grabbing just the chemical name (NaCl) from the list by splitting the list by the "-" character and take the first part (the 0th index)
        concentration_full_name = solution.split('-')[1] #grabbing just the concentration name (including 'M') by splitting the list by the "-" character and take the second part (the 1st index)
        concentration = float(concentration_full_name.replace('M', '')) #get rid of the 'M' in the variable "concentration_full_name" and replace with nothing AND turn it into a float so you can perform mathematical functions
    
        if chemical_name in molecular_weights: #checking to see if the chemical_name is avaiable in the dictionary 
            mol_weight = molecular_weights[chemical_name] #if it is, continue with this line and get the value from the key (chemical_name)
            weight = mol_weight*concentration #calculate the weight by multiplying mol_weight by concentration
            outputs = f'{chemical_name}-{concentration_full_name}-{weight:.2f}g' #format the outputs with an f-string and the variable names in {}. the ":.2f" in the weight variable means round to 2 decimal places. I also need to add the "g" at the end to denote grams.
        else: #if the chemical_name is NOT avaiable in the dictionary
            outputs = 'unknown' #set the outputs variable to "unknown"
    
        output_list.append(outputs)#append the outputs from the for loop into this list (initialized earlier)
    
    return(output_list) #come out of the loop, and return the full list of everything that went through the loop.
