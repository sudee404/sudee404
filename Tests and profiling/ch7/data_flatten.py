nested={
    'fullname':'Alexander',
    'age':'21',
    'phone-numbers': ['+447421234567', '+447423456789'],
    'residence':{
        'address':{
            'first-line':'Alexander Rd',
            'second-line':'',
        },
        'zip':'N8 0PP',
        'city':'Nairobi',
        'country':'Kenya',
    }
}



flat={
    'fullname':'Alexander',
    'age': '21',
    'phone-numbers': ['+447421234567', '+447423456789'],
    'residence.address.first-line': 'Alexander Rd',
    'residence.address.second-line': '',
    'residence.zip':'N8 0PP',
    'residence.city': 'Nairobi',
    'residence.country':'Kenya',
}

def flatten(data, prefix='', separator='.'):
    """Flattens a nested dict structure. """
    if not isinstance(data, dict):
        return {prefix: data} if prefix else data

    result = {}
    for (key, value) in data.items():
        result.update(
            flatten(
                value,
                _get_new_prefix(prefix, key, separator),
                separator=separator))

    return result

def _get_new_prefix(prefix, key, separator):
    return (separator.join((prefix, str(key)))
    if prefix else str(key))

print(flatten(nested))
print(nested)
print(flat)