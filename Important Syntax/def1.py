def build_profile(first, last, **other_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in other_info.items():
        profile[key] = value
    return profile 

print(build_profile('Tanvir ', 'Hasan', Location = 'Rajshahi'))