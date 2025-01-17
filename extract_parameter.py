def extract_parameter(unit_name, parameter_name, indx): #defining the function, and that it needs 3 inputs

    #defining the dictionary that the function calls upon (note that the value is another dictionary!)
    unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
}
    #using a try and except block so that if a user give invalid arguments, the code does not crash. (handels the issue nicely).
    
    try: #have the code attempt to comply with the following 2 lines
        num = unit_operations_data[unit_name][parameter_name][indx] #variable "num" is assigned the corresponding value to the index provided by the user's argument
        return f"{unit_name}_{parameter_name}_{num}" #f-string to print the variable in the format the HW problem asked for
    except (KeyError, IndexError): #if the try block does not work, move to this section of the code ((takes in 2 arguments (does not need both), Key error means a dict key does not exists, and Index Error is if the index is out of range))
        return "Invalid input!!!" #printing "invalid input!!!" if there is invalid arugments in the input

 
