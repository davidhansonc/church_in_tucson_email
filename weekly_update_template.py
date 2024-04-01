import datetime
from tools.set_schedule import get_schedule, lords_date

'''UPDATE THE FOLLOWING'''
# update weekly
subject = "Weekly Announcements"
announcements = f"""
Hi saints, <br><br>

The sign-up sheet for the semiannual training (in-person and video) is available on the table in the hall. Please sign up if 
you are burdened to. 
<br><br>
This week is the last week of the current Holy Word for Morning Revival. Next week we will start week one of 
"The Enjoyment of Christ and Our Growth in Life unto Maturity". The link below is updated if you need to order a physical or electronic 
copy. 
<br><br>

We have the normal schedule this week.
<br><br>

Enjoy Him!
"""

hwmr_week = 9 # update weekly (ascending)
group_seed = 1 # update weekly (DEscending 6-->1)

HWMR = "Living and Serving according to God’s Economy concerning the Church"
HWMR_LSM = "https://www.livingstream.com/en/holy-word-for-morning-revival/99999300-hwmr-the-enjoyment-of-christ-and-our-growth-in-life-unto-maturity.html"


monday_meeting = f"Life-study of Jude (message 5)" # update weekly (ascending)
thursday_meeting = f"Life-study of First Peter (message 27)" # update weekly (ascending)
friday_meeting = f"Life-study of Hebrews (message 38)" # update weekly (ascending)    
saturday_meeting = f"Life-study of John (message 48)" #update weekly (ascending)

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
        If you need a physical or electronic copy of the upcoming HWMR book
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