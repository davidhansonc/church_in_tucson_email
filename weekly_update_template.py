import datetime
from tools.set_schedule import get_schedule, lords_date

'''UPDATE THE FOLLOWING'''
# update weekly
subject = "Weekly Announcements"
announcements = f"""
Hi saints, <br><br>

We have the normal schedule this week. Remember to sign up for the December training! <br><br>

This week is our last week in the current morning revival book. Next week we will begin the book from 
the July training. If you're not on the order list and need a physical or electronic copy, the link 
is updated below.<br><br>

Phoebe Zhang will be sending out email updates from her experience in the training. For those who would like 
to receive the emails, you can sign up at this link: 
https://docs.google.com/forms/d/1Ed-BmnlDra8cwegQTrMLWZGr0DqOkqsJxQ6ARn093nk/edit

<br><br>
Jesus is Lord!
"""

hwmr_week = 8  # update weekly (ascending)
group_seed = 1 # update weekly (DEscending 6-->1)


monday_meeting = f"Life-study of First John (message 27)" # update weekly (ascending)
thursday_meeting = f"Life-study of First Peter (message 7)" # update weekly (ascending)
friday_meeting = f"Life-study of Hebrews (message 18)" # update weekly (ascending)    
saturday_meeting = f"Life-study of John (message 28)" #update weekly (ascending)


HWMR = f"""
HWMR: 
Knowing, Experiencing, and Living the All-inclusive Christ for the Genuine Church Life
Making Ourselves Ready for the Lord's Coming
, week {hwmr_week}
"""
HWMR_LSM = """
https://www.livingstream.com/en/holy-word-for-morning-revival/99999261-hwmr-an-overview-of-the-central-burden-and-present-truth-of-the-lords-recovery-before-his-appearing-vol-1.html
"""
HWMR_apple = """
https://books.apple.com/ec/book/the-holy-word-for-morning-revival-knowing/id6447316633
"""
HWMR_google = """
https://play.google.com/store/books/details/The_Holy_Word_for_Morning_Revival_Knowing_Experien?id=E6S3EAAAQBAJ&hl=en_US&gl=US&pli=1
"""
HWMR_kindle = """
https://www.amazon.com/Holy-Word-Morning-Revival-All-inclusive-ebook/dp/B0C1L7X257
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
        <i>{HWMR}</i><br><br>
        If you need a physical or electronic copy of the upcoming HWMR book, 
		    see the <a href="{HWMR_LSM}">LSM Bookstore</a>.<br>
        <br><br>

        For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
        <a href="https://drive.google.com/file/d/1byQPJ73KjIZqgHkgW_U-4MS6fbE5eRQU/view?usp=drive_link">this link</a>.
        <br><br>
        </p>

    <h2>Meeting Schedule</h2>
        <p>
        Monday: 7:00 PM {monday_meeting} <br><br>
        Tuesday: 7:30 PM prayer meeting <br><br>
        Thursday: 7:30 PM {thursday_meeting} <br><br>
        Friday: 7:30 PM {friday_meeting} <br><br>
        Saturday: 7:30 PM {saturday_meeting} <br><br>
        Lord's Day Morning: 10:00 AM - 12:00 PM Table and prophesying meetings<br><br>
  </body>
</html>
"""

message_text = f"""
If you see this, please reply and ask for a direct email with the schedule and announcements.
"""