

def get_formatted_name(first_name,last_name, middle_name = ''):
    """Display formatted name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name +  ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
geek = get_formatted_name("Jackson","kamoche")
print(geek)
geek = get_formatted_name("Jackson","kamoche", 'Githinji')
print(geek)