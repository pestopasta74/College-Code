#Generate a formatted full name
#use file name as name_function.py
# save it in a folder
def formatted_name(first_name, last_name, middle_names = ''):
    if middle_names == '':
        full_name = first_name + ' '+ last_name
        return full_name.title()
    else:
        full_name = first_name + ' '+ middle_names + ' ' + last_name
        return full_name.title()