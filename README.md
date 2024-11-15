def student_health_list(filename: str, health_value: int):
    """
    Returns a list of dictionaries, each representing a student's data 
    with the specified health value. Excludes the 'Health' attribute from 
    each dictionary. Returns an empty list if no students match.
    """
    file = open(filename, "r")
    students = []
    line_number = 1
    for line in file:
        if line_number == 1:
            headers = line.strip().split(',')
            for header in headers:
                if header == 'Health':
                    health_index = headers.index('Health')
                    headers.pop(health_index)
        else:
            values = line.strip().split(',')
            if len(values) <= health_index:
                continue            
            if int(values[health_index]) == num_health:
                values.pop(health_index)
                student_dict = dict(zip(headers, values))
                students.append(student_dict)
        line_number += 1
    file.close()
    return students
