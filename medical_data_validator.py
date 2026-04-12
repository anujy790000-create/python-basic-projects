"""
Medical Records Validation System
---------------------------------

This script validates patient medical records based on predefined
data constraints.

Features:
- Ensures correct data structure
- Validates patient information fields
- Detects invalid or missing data entries
- Prints detailed validation errors

Author: Anuj Yadav
"""

import re

# -------------------------------------------------------------------
# Sample Medical Records Dataset
# -------------------------------------------------------------------
# Each record must contain:
# patient_id, age, gender, diagnosis, medications, last_visit_id

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


# -------------------------------------------------------------------
# Function: find_invalid_records
# -------------------------------------------------------------------
def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    """
    Validates individual medical record fields.

    Returns:
        list: Keys that failed validation checks.
    """

    constraints = {
        # Patient ID must start with 'P' followed by digits
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\\d+', patient_id, re.IGNORECASE),

        # Age must be integer and >= 18
        'age': isinstance(age, int) and age >= 18,

        # Gender must be male or female (case-insensitive)
        'gender': isinstance(gender, str)
        and gender.lower() in ('male', 'female'),

        # Diagnosis must be string or None
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # Medications must be list of strings
        'medications': isinstance(medications, list)
        and all(isinstance(i, str) for i in medications),

        # Visit ID must start with 'V' followed by digits
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\\d+', last_visit_id, re.IGNORECASE)
    }

    # Return all fields that failed validation
    return [key for key, value in constraints.items() if not value]


# -------------------------------------------------------------------
# Function: validate
# -------------------------------------------------------------------
def validate(data):
    """
    Validates the entire dataset.

    Parameters:
        data (list | tuple): Collection of patient records

    Returns:
        bool: True if valid, False otherwise
    """

    # Check if input is iterable sequence
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False

    is_invalid = False

    # Required keys for every record
    key_set = {
        'patient_id',
        'age',
        'gender',
        'diagnosis',
        'medications',
        'last_visit_id'
    }

    # Iterate through dataset
    for index, dictionary in enumerate(data):

        # Ensure each item is a dictionary
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        # Check for missing or extra keys
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        # Validate record fields
        invalid_records = find_invalid_records(**dictionary)

        # Print detailed errors
        for key in invalid_records:
            val = dictionary[key]
            print(f"Unexpected format '{key}: {val}' at position {index}.")
            is_invalid = True

    # Final validation result
    if is_invalid:
        return False

    print('Valid format.')
    return True


# -------------------------------------------------------------------
# Run Validation
# -------------------------------------------------------------------
validate(medical_records)
