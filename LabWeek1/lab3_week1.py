def calculation(value):
    a,b,c,d = value.split()
    time_in_hour = int(a)
    time_in_minute = int(b)

    time_out_hour = int(c)
    time_out_minute = int(d)

    if time_in_hour < 7 or time_out_hour > 23 or (time_out_hour < time_in_hour):
        return "Invalid"
    elif time_in_minute < 0 or time_out_minute < 0:
        return "Invalid"
    elif time_in_minute >= 60 or time_out_minute >= 60:
        return "Invalid"


    time_in_min = (time_in_hour*60)+time_in_minute
    time_out_min = (time_out_hour*60)+time_out_minute

    duration_minute = time_out_min-time_in_min

    duration_hour = duration_minute//60
    remain_minute = duration_minute%60

    if duration_minute<= 15:
        fee = 0

    elif duration_hour < 3 or (duration_hour == 3 and remain_minute == 0):
        fee = (duration_hour + (1 if remain_minute > 0 else 0)) * 10

    elif duration_hour >= 4 and duration_hour <= 6:
        fee = 3*10
        additional_hours = duration_hour - 3 + (1 if remain_minute > 0 else 0)
        fee += additional_hours * 20
    else:
        fee = 200
        
    return fee


value = input()
output = calculation(value)
print(output)