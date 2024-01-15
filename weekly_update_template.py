import datetime
from tools.set_schedule import get_schedule, lords_date

'''UPDATE THE FOLLOWING'''
# update weekly
subject = "Weekly Announcements"
announcements = f"""
Hi saints, <br><br>

We have the normal meeting schedule this week.

<br><br>
Praise the Lord.
"""

hwmr_week = 11 # update weekly (ascending)
group_seed = 6 # update weekly (DEscending 6-->1)


monday_meeting = f"Life-study of First John (message 38)" # update weekly (ascending)
thursday_meeting = f"Life-study of First Peter (message 17)" # update weekly (ascending)
friday_meeting = f"Life-study of Hebrews (message 28)" # update weekly (ascending)    
saturday_meeting = f"Life-study of John (message 38)" #update weekly (ascending)


HWMR = f"""
HWMR: 
An Overview of the Central Burden and Present Truth of the Lord’s Recovery before His Appearing, vol. 2
, week {hwmr_week}
"""
HWMR_LSM = """
https://www.livingstream.com/en/holy-word-for-morning-revival/99999270-hwmr-an-overview-of-the-central-burden-and-present-truth-of-the-lords-recovery-before-his-appearing-vol-2.html
"""
HWMR_apple = """
https://books.apple.com/us/book/the-holy-word-for-morning-revival-an-overview/id6451326887
"""
HWMR_google = """
https://play.google.com/store/books/details/The_Holy_Word_for_Morning_Revival_An_Overview_of_t?id=9XzLEAAAQBAJ&hl=en_US&gl=US
"""
HWMR_kindle = """
https://www.amazon.com/Holy-Word-Morning-Revival-Appearing-ebook/dp/B0CBWBPTHX
"""


schedule = get_schedule(group_seed)
lords_day = lords_date(datetime.date.today())


message_html = f""" <html>
  <head></head>
  <body>
    <p> {announcements} </p>

    <h2>Next Lord's Day ({lords_day})</h2>
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
        <i>{HWMR}</i><br>
        If you need a physical or electronic copy of the upcoming HWMR book, 
		    see the <a href="{HWMR_LSM}">LSM Bookstore</a>.
        <br><br>

        For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
        <a href="https://drive.google.com/file/d/1byQPJ73KjIZqgHkgW_U-4MS6fbE5eRQU/view?usp=drive_link">this link</a>.
        </p>

    <h2>Meeting Schedule</h2>
        <p>
        Monday: 7:00 PM {monday_meeting} <br><br>
        Tuesday: 7:30 PM prayer meeting <br><br>
        Thursday: 7:30 PM {thursday_meeting} <br><br>
        Friday: 7:30 AM {friday_meeting} <br><br>
        Saturday: 7:30 AM {saturday_meeting} <br><br>
        Lord's Day Morning: 10:00 AM Table and prophesying meetings <br><br>
        </p>
  </body>
</html>
"""

message_text = f"""
If you see this, please reply and ask for a direct email with the schedule and announcements.
"""