from datetime import datetime, timedelta
from tools.set_schedule import lords_date
import groups
from scheduler import get_prophesying_group_order


'''UPDATE THE FOLLOWING'''
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

# Announcements content
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

# HTML message
message_html = f"""<html>
<head></head>
<body>
    <p>{announcements}</p>

    <h2>Next Lord's Day ({lords_day_date})</h2>
    <h3>Prophesying Schedule:</h3>
    <ul>
        <li>Day 1: {prophesying_order[0]}
        <li>Day 2: {prophesying_order[1]}
        <li>Day 3: {prophesying_order[2]}
        <li>Day 4: {prophesying_order[3]}
        <li>Day 5: {prophesying_order[4]}
        <li>Day 6: {prophesying_order[5]}
    </ul>
    <i>{HWMR}, week {hwmr_week}.</i><br>
    If you still need a physical or electronic copy of the HWMR book, see the <a href="{HWMR_LSM}">LSM Bookstore</a>.
    <br><br>

    For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
    <a href="https://drive.google.com/file/d/1byQPJ73KjIZqgHkgW_U-4MS6fbE5eRQU/view?usp=drive_link">this link</a>.
    </p>

    <h2>Meeting Schedule</h2>
    <p>
    Monday: 7:00 PM {monday_meeting} <br>
    Tuesday: 7:30 PM prayer meeting <br>
    Thursday: {thursday_meeting} <br>
    Friday: {friday_meeting} <br>
    Saturday: {saturday_meeting} <br>
    Lord's Day Morning: 10:00 AM Table meeting and 11:00 AM prophesying meeting <br>
    </p>
</body>
</html>
"""

# Plain text message for email clients that do not support HTML
message_text = """
If you see this message, please reply and ask for a direct email with the schedule and announcements.
"""