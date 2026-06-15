def age_validator(age: int) -> str:
    if age <= 0:
        raise ValueError('Age cannot be negative or zero')
    elif age < 18:
        return 'Age not suitable for voting'
    elif age >= 18:
        return 'Age suitable for voting'
    else:
        return 'Invalid Age'
    
