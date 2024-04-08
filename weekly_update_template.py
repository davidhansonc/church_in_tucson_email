import datetime
from tools.set_schedule import get_schedule, lords_date

'''UPDATE THE FOLLOWING'''
# update weekly
subject = "Weekly Announcements"
announcements = f"""
Hi saints, <br><br>

This coming weekend will be the Spring International Training for Elders and Responsible Ones (ITERO). There are 9 messages to listen to over 
the weekend, so the brothers who are attending will be preoccupied. This may affect the meeting schedule, so later this week we will send out 
clarification on meetings that may be canceled.
<br><br>
A reminder that we are starting week 1 of the new morning revival this week! If you still need a copy, you can get one at the link below. 

Enjoy Him!
"""

hwmr_week = 1 # update weekly (ascending)
group_seed = 6 # update weekly (DEscending 6-->1)

HWMR = "The Enjoyment of Christ and Our Growth in Life unto Maturity"
HWMR_LSM = "https://www.livingstream.com/en/holy-word-for-morning-revival/99999300-hwmr-the-enjoyment-of-christ-and-our-growth-in-life-unto-maturity.html"


monday_meeting = f"Life-study of First Thessalonians (message 1)" # update weekly (ascending)
thursday_meeting = f"Life-study of First Peter (message 28)" # update weekly (ascending)
friday_meeting = f"Life-study of Hebrews (message 39)" # update weekly (ascending)    
saturday_meeting = f"Life-study of John (message 49)" #update weekly (ascending)

schedule = get_schedule(group_seed)


message_html = f""" <html>
  <head></head>
  <body>
    <p> {announcements} </p>

    <h2>Next Lord's Day ({lords_date(send_date=datetime.date.today())})</h2>
        <h3>Prophesying Schedule:</h3>
        <p>
        <ul>
            <li>Day 1:  Group {schedule[0]}
            <li>Day 2:  Group {schedule[1]}
            <li>Day 3:  Group {schedule[2]}
            <li>Day 4:  Group {schedule[3]}
            <li>Day 5:  Group {schedule[4]}
            <li>Day 6:  Group {schedule[5]}
        </ul>
        <i>{HWMR}, week {hwmr_week}.</i><br>
        If still you need a physical or electronic copy of the HWMR book
		    see the <a href="{HWMR_LSM}">LSM Bookstore</a>.
        <br><br>

        For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
        <a href="https://drive.google.com/file/d/1byQPJ73KjIZqgHkgW_U-4MS6fbE5eRQU/view?usp=drive_link">this link</a>.
        </p>

    <h2>Meeting Schedule</h2>
        <p>
        Monday: 7:00 PM {monday_meeting} <br><br>
        Tuesday: 7:30 PM prayer meeting <br><br>
        Thursday: {thursday_meeting} <br><br>
        Friday: {friday_meeting} <br><br>
        Saturday: {saturday_meeting} <br><br>
        Lord's Day Morning: 10:00 AM Table meeting and 11:00 AM prophesying meeting <br><br>
        </p>
  </body>
</html>
"""

message_text = f"""
If you see this, please reply and ask for a direct email with the schedule and announcements.
"""