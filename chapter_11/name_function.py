def get_formatted_name(fname,lname,middle=''):
    """Generate a neatly formatted full name"""
    if middle:
        full_name = fname + ' ' + middle + ' ' +lname
    else:
        full_name = fname + ' ' + lname
    return full_name.title()