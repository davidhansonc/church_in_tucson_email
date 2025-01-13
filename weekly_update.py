from datetime import datetime
from tools.set_schedule import lords_date
import groups
from scheduler import get_prophesying_group_order, get_cleaning_group_order#, get_ushering_order

# Weekly updates
subject = "Church in Tucson Weekly Announcements"
hwmr_week = 1 # update weekly
HWMR = """The Christian Life"""
HWMR_link = "https://www.livingstream.com/en/holy-word-for-morning-revival/99999347-hwmr-the-christian-life.html"
min_mag_link = "https://www.livingstream.com/en/ministry-of-the-word/99999346-ministry-of-the-word-periodical-the-vol-28-no-06-august-2024.html"
webcast_link = "https://www.lsmwebcast.com/ArchivesDtl.cfm?cat=C&subj=420"
ushers = "Isaac/DC"

# Meeting topics to be updated weekly
monday_meeting = "Life-study of First Thessalonians"
thursday_meeting = "Life-study of Matthew"
friday_meeting = "Life-study of Hebrews"
saturday_meeting = "Life-study of Second Timothy"

announcements = f"""
Hi saints,
<br><br>

This week we have the normal church meeting schedule. We are beginning week 1 of the new morning revival 
book, "{HWMR}". See the links below if you need an electronic copy. Unfortunately the physical copies 
are currently out of stock.
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
        
        <p><i>{HWMR}, week {hwmr_week}.</i><br><br>
        For the Holy Word for Morning Revival book and associated the written and/or audio 
        messages from the conference, see the following links:</p>
        <ul>
            <li> <a href="{HWMR_link}" style="color: #0056b3; text-decoration: none;">HWMR</a>
            <li> <a href="{min_mag_link}" style="color: #0056b3; text-decoration: none;">Ministry Magazine</a>
            <li> <a href="{webcast_link}" style="color: #0056b3; text-decoration: none;">Audio Messages</a>
        </ul>

        <p>For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
        <a href="https://drive.google.com/file/d/15seb5EfFD93_XuVOP4qi5fTzn4wLio8V/view?usp=drive_link" 
        style="color: #0056b3; text-decoration: none;">this link</a>.</p>
        
        <h3 style="color: #0056b3;">Prophesying Schedule:</h3>
        <ul style="list-style-type: none; padding: 0;">
            {prophesying_formatted}
        </ul>
        
		<h3 style="color: #0056b3;">Cleaning Team and Ushers:</h3>
        <p style="margin-bottom: 20px;">{cleaning_formatted}</p>
        <p style="margin-bottom: 20px;"><b>Ushers</b>: {ushers}</p>
        <p style="margin-bottom: 20px;">Please meet at the hall about a half hour before the Table meeting starts 
        for cleaning and preparing the elements.</p>

        <h2 style="color: #0056b3; margin-top: 40px;">Meeting Schedule</h2>
        <p>
            Monday: 7:30 PM {monday_meeting} <br>
            Tuesday: 7:30 PM Prayer Meeting <br>
            Thursday: 7:30 PM {thursday_meeting} <br>
            Friday: 7:30 PM {friday_meeting} <br>
            Saturday: 7:30 PM {saturday_meeting} <br>
            Lord's Day Morning: 10:00 AM Table meeting and 11:00 AM prophesying meeting <br>
        </p>

        <h2 style="color: #0056b3; margin-top: 40px;">Upcoming Events</h2>
        <h4>Phoenix Blending Conference | February 21-23, 2025</h4>
            <p>Brother Ron will be coming to Phoenix for a Southwest blending conference. 
            Sign up on the sign-up sheets in the hall for hospitality and/or childcare during 
            the conference.</p>

        <h4>Tucson Festival of Books | March 15-16, 2025</h4>
            <p>We will be tabling for Bibles for America again. 
            More info to come...</p>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
	# Define the filename for the output HTML file
	filename = "./email.html"

	# Writing the HTML content to a file
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(message_html)

	print(f"HTML email saved to {filename}")