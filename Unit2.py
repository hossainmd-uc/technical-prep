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


def best_set(votes):
    
    final = {}

    for each in votes:
        if votes[each] not in final:
            final[votes[each]] = 1
        else:
            final[votes[each]] += 1
    print(final)

    top = [None, 0]
    for each in final:
        if final[each] > top[1]:
            top = [each, final[each]]

    return top[0]


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

# print(best_set(votes1))
# print(best_set(votes2))


def num_popular_pairs(popularity_scores):
    
    popularity_map = {}

    for each in popularity_scores: 
        if each not in popularity_map:
            popularity_map[each] = 1
        else:
            popularity_map[each] += 1
    
    print(popularity_map)
    pairs_with_same_score = 0

    for each in popularity_map:
        if popularity_map[each] > 1:
            combinatorics_res = (popularity_map[each] * (popularity_map[each]-1))//2
            pairs_with_same_score += combinatorics_res
        
    return pairs_with_same_score

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

# print(num_popular_pairs(popularity_scores1))
# print(num_popular_pairs(popularity_scores2))
# print(num_popular_pairs(popularity_scores3)) 


def find_stage_arrangement_difference(s, t):
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """
    s1_map = {}
    t1_map = {}

    #assuming each element appears exactly once
    for i in range(len(s)):
        s1_map[s[i]] = i
    
    for i in range(len(t)):
        t1_map[t[i]] = i

    diff = 0
    for each in s1_map:
        diff += abs(s1_map[each] - t1_map[each])
    
    return diff


s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

# print(find_stage_arrangement_difference(s1, t1))
# print(find_stage_arrangement_difference(s2, t2))

#Version 1
def num_VIP_guests(vip_passes, guests):

    accepted_vip = list(vip_passes)
    current_guests = list(guests)

    total = 0
    for vip_pass in accepted_vip:
        total += current_guests.count(vip_pass)
    
    return total

#Version 2
def num_VIP_guests2(vip_passes, guests):

    vip_set = set(set(vip_passes))

    counter = 0
    for g in guests:
        if g in vip_set:
            counter+=1
    
    return counter



vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests2(vip_passes1, guests1))
print(num_VIP_guests2(vip_passes2, guests2))
