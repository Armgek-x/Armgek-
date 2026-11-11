def convert_size(value, direction, unit_from, unit_to):
    result = 0
    
    if direction == "to_larger":
        if unit_from == "bits" and unit_to == "bytes":
            result = value / 8
        elif unit_from == "bytes" and unit_to == "kb":
            result = value / 1024
        elif unit_from == "kb" and unit_to == "mb":
            result = value / 1024
        elif unit_from == "mb" and unit_to == "gb":
            result = value / 1024
        else:
            pass
    elif direction == "to_smaller":
        if unit_from == "gb" and unit_to == "mb":
            result = value * 1024
        elif unit_from == "mb" and unit_to == "kb":
            result = value * 1024
        elif unit_from == "kb" and unit_to == "bytes":
            result = value * 1024
        elif unit_from == "bytes" and unit_to == "bits":
            result = value * 8
            
    return result

def convert_time(value, mode):
    if mode == "hours_to_mins":
        return value * 60
    elif mode == "mins_to_secs":
        return value * 60
    elif mode == "secs_to_mins":
        return value / 60
    elif mode == "mins_to_hours":
        return value / 60
    else:
        return 0