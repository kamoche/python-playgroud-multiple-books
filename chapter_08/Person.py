

def build_person(first_name, last_name, age = ''):
    """Display dictionary about person information"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

programmer = build_person('Jackson', 'Kamoche', '27')
print(programmer)
