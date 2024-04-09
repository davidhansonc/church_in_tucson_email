from datetime import datetime
from tools.set_schedule import lords_date
import groups
from scheduler import get_prophesying_group_order, get_cleaning_group_order, get_ushering_order

# Weekly updates
subject = "Church in Tucson Weekly Announcements"
hwmr_week = 1  # update weekly
HWMR = "The Enjoyment of Christ and Our Growth in Life unto Maturity"
HWMR_LSM = "https://www.livingstream.com/en/holy-word-for-morning-revival/99999300-hwmr-the-enjoyment-of-christ-and-our-growth-in-life-unto-maturity.html"

# Meeting topics to be updated weekly
monday_meeting = "Life-study of First Thessalonians (message 1)"
thursday_meeting = "Life-study of First Peter (message 28)"
friday_meeting = "Life-study of Hebrews (message 39)"
saturday_meeting = "Life-study of John (message 49)"

announcements = """
Hi saints, <br><br>

This coming weekend will be the Spring International Training for Elders and Responsible Ones (ITERO). There are 9 messages to listen to over 
the weekend, so the brothers who are attending will be preoccupied. This may affect the meeting schedule, so later this week we will send out 
clarification on meetings that may be canceled.
<br><br>
A reminder that we are starting week {hwmr_week} of the new morning revival this week! If you still need a copy, you can get one at the link below. 

Enjoy Him!
""".format(hwmr_week=hwmr_week)

current_date = datetime.today()
lords_day_date = lords_date(send_date=current_date)
prophesying_order = get_prophesying_group_order(groups.prophesying_groups, current_date)
cleaning_order = get_cleaning_group_order(groups.cleaning_groups, current_date)
ushering_order = get_ushering_order(groups.ushering_groups, current_date)

# Update the HTML message to include cleaning and ushering schedules
message_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Weekly Announcements</title>
</head>
<body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">
    <div style="max-width: 600px; margin: auto; border: 10px solid #eee; padding: 20px;">

        <p style="font-size: 16px;">{announcements}</p>

        <h2 style="color: #0056b3;">Next Lord's Day ({lords_day_date})</h2>
        
        <h3 style="color: #0056b3;">Prophesying Schedule:</h3>
        <ul style="list-style-type: none; padding: 0;">
            {''.join(f'<li style="padding: 5px 0;">{group}</li>' for group in prophesying_order)}
        </ul>
        
        <h3 style="color: #0056b3;">Cleaning Team Schedule:</h3>
        <ul style="list-style-type: none; padding: 0;">
            {''.join(f'<li style="padding: 5px 0;">{team}</li>' for team in cleaning_order)}
        </ul>
        
        <h3 style="color: #0056b3;">Ushering Schedule:</h3>
        <p style="margin-bottom: 20px;">This week's ushers: {ushering_order}</p>
        
        <p><i>{HWMR}, week {hwmr_week}.</i><br>
        If you still need a physical or electronic copy of the HWMR book, see the <a href="{HWMR_LSM}" style="color: #0056b3; text-decoration: none;">LSM Bookstore</a>.</p>

        <p>For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
        <a href="https://drive.google.com/file/d/1byQPJ73KjIZqgHkgW_U-4MS6fbE5eRQU/view?usp=drive_link" style="color: #0056b3; text-decoration: none;">this link</a>.</p>

        <h2 style="color: #0056b3; margin-top: 40px;">Meeting Schedule</h2>
        <p>
            Monday: 7:00 PM {monday_meeting} <br>
            Tuesday: 7:30 PM prayer meeting <br>
            Thursday: {thursday_meeting} <br>
            Friday: {friday_meeting} <br>
            Saturday: {saturday_meeting} <br>
            Lord's Day Morning: 10:00 AM Table meeting and 11:00 AM prophesying meeting <br>
        </p>
    </div>
</body>
</html>
"""

message_text = """
If you see this message, please reply and ask for a direct email with the schedule and announcements.
"""

if __name__ == "__main__":
	# Define the filename for the output HTML file
	filename = "./email.html"

	# Writing the HTML content to a file
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(message_html)

	print(f"HTML email saved to {filename}")
