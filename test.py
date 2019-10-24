flight_details = ["A1890:BAN:MUM:1400", "B1820:MUM:DEL:730", "C1923:DEL:AND:1100"]
pass_details = {"LW101" : ["Amanda", "A1890", "C7", 25]}

def find_flights(flight_time):
    fnl = []
    flight_time = int(flight_time)
    for x in flight_details:
        lst = x.split(":")
        if int(lst[3]) <= flight_time + 200 and int(lst[3]) >= flight_time:
            fnl.append(x)
    return x

def sort_flight_list(flight_list):
    fnl = []
    for x in flight_list:
        fnl.append(x.split(":"))

    for x in range(len(fnl)):
        for y in range(x, len(fnl)-1):
            if int(fnl[y][3]) > int(fnl[y+1][3]):
                fnl[y], fnl[y+1]= fnl[y+1], fnl[y]
    print(fnl)

    fnl2 = []
    for x in fnl:
        fnl2.append(":".join(x))

    return fnl2

def get_passenger_details(flight_detail):
    lst = []
    flight_detail = flight_detail.split(":")
    for x in pass_details:
        if pass_details[x][1] == flight_detail[0]:
            lst.append(x)
    return lst

print(find_flights("0700"))
print(sort_flight_list(flight_details))
print(get_passenger_details("A1890:BAN:MUM:1400"))
