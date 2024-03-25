

# Inside registration.py under the feature-voter-registration branch

def register_party(parties):
    for party in parties:
        party_name = party.get("party_name")
        member_count = party.get("member_count")
        if member_count >= 1000:
            print(f"Party {party_name} has acceptable member count and can be registered.")
        else:
            print(f"Party {party_name} does not have enough members to be registered.")

            
           # Assuming registration.py is already imported or executed
# Assuming parties_list is a list containing dictionaries of parties

# Function call to register the MK party
parties_list.append({"party_name": "MK Party", "reg_number": 10003319, "member_count": 5300})
register_party(parties_list)
 
# Create a new file named voter_info.py under a new feature branch
# Switch to the new branch before proceeding

# Inside voter_info.py

def update_voter_info(voter_info, voter_id, name, voting_district, has_voted):
    voter_info[voter_id] = {"name": name, "voting_district": voting_district, "has_voted": has_voted}

# Create a new file named voter_info.py under a new feature branch
# Switch to the new branch before proceeding
    
# Assuming parties_list contains all parties as dictionaries with keys: party_name, reg_number, member_count

# Using list comprehension
filtered_parties = [party["party_name"] for party in parties_list if party["member_count"] >= 1000]

# Using filter function
filtered_parties = list(filter(lambda party: party["member_count"] >= 1000, parties_list))
filtered_parties = [party["party_name"] for party in filtered_parties]

# Using a for loop
filtered_parties = []
for party in parties_list:
    if party["member_count"] >= 1000:
        filtered_parties.append(party["party_name"])

# Assuming voter_info contains voter records as dictionaries

registered_voters = list(filter(lambda voter: voter["registered"], voter_info.values()))
