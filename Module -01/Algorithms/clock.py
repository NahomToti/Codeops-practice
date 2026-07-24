def digitalClock(seconds):
    
    seconds = seconds % 86400

    
    hours = seconds // 3600
    seconds = seconds % 3600

    
    minutes = seconds // 60

    
    seconds = seconds % 60

    
    return f"{hours:02}:{minutes:02}:{seconds:02}"


# Test cases
print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))