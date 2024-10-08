from datetime import datetime
from tools.set_schedule import lords_date
import groups
from scheduler import get_prophesying_group_order, get_cleaning_group_order#, get_ushering_order

# Weekly updates
subject = "Church in Tucson Weekly Announcements"
hwmr_week = 8  # update weekly
HWMR = """Being a Vessel unto Honor, a Fully Equipped Man of God, 
by Being Empowered in the Grace which is in Christ Jesus 
to Fully Accomplish Our Ministry in the Unique Ministry of God's Economy"""
HWMR_LSM = "https://www.livingstream.com/en/holy-word-for-morning-revival/99999332-hwmr-being-a-vessel-unto-honor-a-fully-equipped-man-of-god-by-being-empowered-in-the-grace-which-is-in-christ-jesus.htmlhttps://www.livingstream.com/en/holy-word-for-morning-revival/99999355-hwmr-experiencing-enjoying-and-expressing-christ-1-vol-1.html"
ushers = "Isaac/DC"

# Meeting topics to be updated weekly
monday_meeting = "Life-study of First Thessalonians"
thursday_meeting = "Life-study of Second Peter"
friday_meeting = "Life-study of Hebrews"
saturday_meeting = "Life-study of First Timothy"

announcements = """
Hi saints, <br><br>

The meetings on Monday night, Friday night, and Saturday night are canceled 
this week. The Tuesday night prayer meeting, Thursday night Life-study 
meeting, and the Table and prophesying meetings on the Lord's day 
remain as usual. 
<br><br>

We are on the last week of the current HWMR book and next week we will 
begin the book from the recent July training. The links below are updated for 
those not on the standing order who would like to get a copy.
<br><br>

In Him.
""".format(hwmr_week=hwmr_week)

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
        If you want to buy a physical or electronic copy of the upcoming HWMR book, see the <a href="{HWMR_LSM}" 
        style="color: #0056b3; text-decoration: none;">LSM Bookstore</a>.</p>

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
            Tuesday: 7:30 PM Prayer Meeting <br>
            Thursday: 7:30 PM {thursday_meeting} <br>
            Lord's Day Morning: 10:00 AM Table meeting and 11:00 AM prophesying meeting <br>
        </p>

        <h2 style="color: #0056b3; margin-top: 40px;">Upcoming Events</h2>
        <h4>Thanksgiving conference in Atlanta, Georgia</h3>
            <p>For conference schedule, hotel options, and other information, please see the pdf 
            document at 
            <a href=https://drive.google.com/file/d/1pEe2ikkHuHtj9qC-9oqgrmjLxnV8qGvK/view?usp=drive_link">this link</a>.
            </p>
        <h4>December Semiannual Training</h3>
            <p>The sign-up sheet for the live and video semiannual training is posted in the hall.</p>
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
