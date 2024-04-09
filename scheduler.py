from datetime import datetime, timedelta
import groups

date_seed = datetime(2024, 4, 7)


def get_prophesying_group_order(groups, current_date):
    start_date = datetime(2024, 4, 7)
    # Calculate the next Sunday or use the current date if it's already Sunday
    if current_date.weekday() != 6:
        next_sunday = current_date + timedelta(days=(6-current_date.weekday()))
    else:
        next_sunday = current_date

    weeks_since_start = (next_sunday - start_date).days // 7
    # Determine the shift for the group order
    shift = -weeks_since_start % len(groups)
    
    # Create a new ordered list of group names based on the shift
    ordered_group_names = list(groups.keys())[shift:] + list(groups.keys())[:shift]
    
    # Build the ordered dict with group names and their members
    ordered_groups = {group: groups[group] for group in ordered_group_names}
    
    return ordered_groups


def get_cleaning_group_order(groups, current_date):
    # Calculate the next Sunday or use the current date if it's already Sunday
    if current_date.weekday() != 6:
        next_sunday = current_date + timedelta(days=(6 - current_date.weekday()))
    else:
        next_sunday = current_date

    weeks_since_start = (next_sunday - date_seed).days // 7
    # Determine the shift for the group order, adapted for the number of cleaning groups
    shift = -weeks_since_start % len(groups)
    
    # Generate the group order based on the shift
    group_order = list(groups.keys())
    ordered_group_order = group_order[shift:] + group_order[:shift]
    
    # Select the first team from the ordered list and retrieve its members
    first_team_name = ordered_group_order[0]
    first_team_members = groups[first_team_name]
    
    # Return both the team name and its members
    return {first_team_name: first_team_members}



def get_ushering_order(groups, current_date):
    # This simply cycles through the list without considering Sundays
    days_since_start = (current_date - date_seed).days
    # Shift for the ushering order
    shift = days_since_start % len(groups)
    
    # Return the usher for the current day
    return groups[shift]


if __name__ == "__main__":
    current_date = datetime.now()
    print("Prophesying Groups:", get_prophesying_group_order(groups.prophesying_groups, current_date))
    print("Cleaning Groups:", get_cleaning_group_order(groups.cleaning_groups, current_date))
    print("Ushering Order:", get_ushering_order(groups.ushering_groups, current_date))
