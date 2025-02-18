from datetime import datetime
from tools.set_schedule import lords_date
import groups
from scheduler import get_prophesying_group_order, get_cleaning_group_order#, get_ushering_order

# Weekly updates
subject = "Church in Tucson Weekly Announcements"
hwmr_week = 6 # update weekly
HWMR = """The Christian Life"""
HWMR_link = "https://www.livingstream.com/en/holy-word-for-morning-revival/99999347-hwmr-the-christian-life.html"
min_mag_link = "https://www.livingstream.com/en/ministry-of-the-word/99999346-ministry-of-the-word-periodical-the-vol-28-no-06-august-2024.html"
webcast_link = "https://www.lsmwebcast.com/ArchivesDtl.cfm?cat=C&subj=420"
ushers = "Jaime/Craig"

# Meeting topics to be updated weekly
monday_meeting = "Life-study of First Thessalonians"
thursday_meeting = "Life-study of Matthew"
friday_meeting = "Life-study of Hebrews"
saturday_meeting = "Life-study of Titus"

announcements = f"""
Hi saints,
<br><br>

This coming weekend we have the conference with brother Ron Kangas in Phoenix. There will be no Table Meeting or other meetings in 
Tucson this weekend, since hopefully many if not all of us will be able to attend the conference. Reminder to account for traffic
on Friday for the first meeting.<br><br>

We are on week 6 of the HWMR and will repeat week 6 next week for us to speak on after the conference.

<br><br>
In Him.
"""

current_date = datetime.today() 
lords_day_date = lords_date(send_date=current_date).strftime('%m/%d/%Y')
prophesying_order = get_prophesying_group_order(groups.prophesying_groups, current_date)
cleaning_team = get_cleaning_group_order(groups.cleaning_groups, current_date)
# ushers = get_ushering_order(groups.ushering_groups, current_date)

# Format the group orders for display
def format_group_order(group_order):
    formatted_order = ""
    day = 0
    # Check if the input is a dictionary
    if isinstance(group_order, dict):
        for group, members in group_order.items():
            day += 1
            members_str = ", ".join(members)  # Convert list of members to a string
            formatted_order += f'<li style="padding: 5px 0;"><b>Day {day}</b>: {group} - {members_str}</li>'
    return formatted_order

prophesying_formatted = format_group_order(prophesying_order)

# Since cleaning_order now returns a dictionary with just one team, extract that team for email content
first_cleaning_team_name, first_cleaning_team_members = list(cleaning_team.items())[0]
cleaning_formatted = f"<b>{first_cleaning_team_name}</b>: {', '.join(first_cleaning_team_members)}"

# Update the HTML message to include formatted group orders
message_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Weekly Announcements</title>
</head>
<body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">
    <div style="max-width: 600px; margin: auto; border: 10px solid #eee; padding: 20px;">

        <p style="font-size: 16px;">{announcements}</p>

        <h2 style="color: #0056b3;">Lord's Day, {lords_day_date}</h2>
        
        <p>This Lord's day, we will be in Phoenix for the conference, but here is the morning revival info for the week:<br><br>
        <i>{HWMR}, week {hwmr_week}.</i><br>
        <ul>
            <li> <a href="{HWMR_link}" style="color: #0056b3; text-decoration: none;">HWMR</a>
            <li> <a href="{min_mag_link}" style="color: #0056b3; text-decoration: none;">Ministry Magazine</a>
            <li> <a href="{webcast_link}" style="color: #0056b3; text-decoration: none;">Audio Messages</a>
        </ul>

        <h2 style="color: #0056b3; margin-top: 40px;">Upcoming Events</h2>
        <h4>Phoenix Blending Conference | February 21-23, 2025</h4>
            Meetings will be at the Phoenix meeting hall:<br>
<a href="https://www.google.com/maps?q=17803+North+27th+Avenue,+Phoenix,+Arizona+85053,+United+States" style="color: #0056b3 target="_blank">17803 North 27th Avenue, Phoenix, Arizona 85053</a>

            <ul style="list-style-type: none;">
                <li> Meeting 1: Friday, 7:30 PM
                <li> Meeting 2: Saturday, 10:00 AM
                <li> Meeting 3: Saturday, 7:00 PM
                <li> Meeting 4: Lord's Day, 10:00 AM
            </ul>

        <h4>Tucson Festival of Books | March 15-16, 2025</h4>
            <p>Please sign up in the hall for time slot(s) to be at the table. We will also need some to help set up and break down 
            before and after the festival.</p>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
	# Define the filename for the output HTML file
	filename = "./email_temp.html"

	# Writing the HTML content to a file
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(message_html)

	print(f"HTML email saved to {filename}")