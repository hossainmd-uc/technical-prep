#Dictionaries

def lineup(artists, set_times):
    
    dictionary = {}

    for i in range(len(artists)):
        if (len(set_times) >= i):
            dictionary[artists[i]] = set_times[i]

    return dictionary


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

def get_artist_info(artist, festival_schedule):
    
    result = festival_schedule.get(artist)

    if result:
        return result
    else:
        return {'message': 'Artist not found'}


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule)) 

def total_sales(ticket_sales):
    total = 0
    for each in ticket_sales:
        total += ticket_sales[each]
    
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))

def identify_conflicts(venue1_schedule, venue2_schedule):
    
    conflicts  = {}

    for each in venue1_schedule:
        v1 = venue1_schedule.get(each)
        v2 = venue2_schedule.get(each)

        if v1 and v2:
            if (v1 == v2):
                conflicts[each] = v1
    
    return conflicts


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

# print(identify_conflicts(venue1_schedule, venue2_schedule))


