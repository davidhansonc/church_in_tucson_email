# Define the groups
prophesying_groups = {
    "Group 1": ["Jay", "Pauline", "DC"],
    "Group 2": ["David", "Denny", "Teresa"],
    "Group 3": ["Craig", "Esther", "Tien Min"],
    "Group 4": ["Isaac", "Judy", "Jessica"],
    "Group 5": ["Joel", "Sam", "Grace"],
    "Group 6": ["Jaime", "Osvin", "Carol"],
}

cleaning_groups = {
    "Team 1": ["Jay", "Denny", "David", "Jessica"],
    "Team 2": ["Isaac", "Esther", "Osvin", "Pauline"],
    "Team 3": ["Craig", "Jaime", "Teresa"],
    "Team 4": ["Sam", "Judy", "Tien Min", "Joel", "Carol"],
}

ushering_groups = [
    "Sam/David",
    "David/Jaime",
    "Jaime/Craig",
    "Isaac/DC",
    "DC/Craig",
    "Isaac, Craig",
    "Craig/Sam",
]


if __name__ == "__main__":
    print(f"prophesying groups: {prophesying_groups}")
    print(f"cleaning groups: {cleaning_groups}")
    print(f"ushering groups: {ushering_groups}")