
def build_profile(fname,lname,**user_info):
    """Building dictionary which has evrything we know about the user"""
    profile = {}
    profile['first_name'] = fname
    profile['last_name'] = lname

    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('kamoche', 'jackson',
                            location= 'Emba',
                            field = "programmer")

print(user_profile)
