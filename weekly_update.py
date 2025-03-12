from datetime import datetime
from tools.set_schedule import lords_date
import groups
from scheduler import get_prophesying_group_order, get_cleaning_group_order#, get_ushering_order

# Weekly updates
subject = "Church in Tucson Weekly Announcements"
hwmr_week = 2 # update weekly
HWMR = """Living a Christian Life and Church Life Under the Government of God for the Economy of God"""
HWMR_link = "https://www.livingstream.com/en/holy-word-for-morning-revival/99999390-hwmr-living-a-christian-life-and-church-life-under-the-government-of-god-for-the-economy-of-god.html"
min_mag_link = "https://www.livingstream.com/en/ministry-of-the-word/99999388-ministry-of-the-word-periodical-the-vol-29-no-01-february-2025.html"
webcast_link = "https://www.lsmwebcast.com/ArchivesDtl.cfm?cat=C&subj=425"
ushers = "Isaac/Craig"

# Meeting topics to be updated weekly
thursday_meeting = "Life-study of Matthew"
friday_meeting = "Life-study of Hebrews"
saturday_meeting = "Life-study of Titus"

announcements = f"""
Hi saints,
<br><br>

This coming weekend is the Tucson Book Festival! There will be no meetings this weekend since we will all be at the BFA table. 
We will send out more information on the book fair later this week. <br><br>
Next week we will repeat week 2 of the HWMR.

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

        <h2 style="color: #0056b3; margin-top: 40px;">Meeting Schedule</h2>
        <p>
            Tuesday: 7:30 PM Prayer Meeting <br>
            Thursday: {thursday_meeting} <br>
            Friday: {friday_meeting} <br>
            Lord's Day Morning: No Meeting <br>
        </p>

        <h2 style="color: #0056b3; margin-top: 40px;">Upcoming Events</h2>
        <h4>Tucson Festival of Books | March 15-16, 2025</h4>
        <ul>
            <li><a href="https://tucsonfestivalofbooks.org/" style="color: #0056b3; text-decoration: none;">tucsonfestivalofbooks.org</a>
        </ul>

        <h4>International Memorial Day Conference | May 23-26, 2025</h4>
        <ul>
            <li>Phoenix, Arizona
        </ul>
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