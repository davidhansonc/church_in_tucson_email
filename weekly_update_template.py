import datetime
from set_schedule import get_schedule, lords_date

'''UPDATE THE FOLLOWING'''
# update weekly
subject = "Weekly Announcements"
announcements = f"""
Hi saints, <br><br>

For those signed up for the summer video training, here are a few announcements. The dates of the video training will 
be July 6th to July 18th every evening at 7:00 PM except for Wednesday the 12th. We'll have testing from 7:00 to 7:30 
and the message will start at 7:30. There are up to two excused absences allowed, but these 
need to be reported before the start of the video training, otherwise they will be counted as unexcused. 
<br><br>
Normal schedule this week.

<br><br>
Jesus is Lord!
"""

hwmr_week = 2  # update weekly (ascending)
group_seed = 1 # update weekly (DEscending 6-->1)


monday_meeting = f"Life-study of 1 John (message 8)" # update weekly (ascending)
thursday_meeting = f"Life-study of Acts (message 60)" # update weekly (ascending)
friday_meeting = f"Life-study of First Corinthians (message 67)" # update weekly (ascending)    
saturday_meeting = f"Life-study of John (message 9)" # update weekly (ascending)


HWMR = f"""  
HWMR: 
The Divine Dispensing of the Divine Trinity for the Divine Economy
, week {hwmr_week}
"""
HWMR_LSM = """
https://www.livingstream.com/en/holy-word-for-morning-revival/99999169-hwmr-crystallization-study-of-1-2-chronicles-ezra-nehemiah-and-esther-vol-1.html
"""
HWMR_apple = """
https://books.apple.com/us/book/the-holy-word-for-morning-revival-crystallization/id6445311211
"""
HWMR_google = """
https://play.google.com/store/books/details/Witness_Lee_The_Holy_Word_for_Morning_Revival_Crys?id=-telEAAAQBAJ
"""
HWMR_kindle = """
https://www.amazon.com/Holy-Word-Morning-Revival-Crystallization-study-ebook/dp/B0BRQV3DD5/ref=sr_1_1?crid=XQ85WC25BH1U&keywords=volume+01+chronicles+morning+revival&qid=1682390586&s=digital-text&sprefix=volume+01+chronicles+morning+revival%2Cdigital-text%2C150&sr=1-1
"""


schedule = get_schedule(group_seed)
lords_day = lords_date(datetime.date.today())


message_html = f"""
<html>
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
        Order a physical copy of the HWMR <a href="{HWMR_LSM}">here</a>, 
        <br>
        Electronic copies are here:
        <ul>
          <li> <a href="{HWMR_kindle}">Kindle</a>
          <li> <a href="{HWMR_google}">Google Play</a>
          <li> <a href="{HWMR_apple}">Apple</a>
        </ul><br>

        For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
        <a href="https://drive.google.com/file/d/19njXktu271Hx_19Le8r9abYlztqbz3t8/view?usp=sharing">this link</a>.<br>
        </p>

    <h2>Meeting Schedule</h2>
        <p>
        Monday: 7:00 PM {monday_meeting} <br><br>
        Tuesday: 7:30 PM - Prayer Meeting <br><br>
        Wednesday: No Meeting <br><br>
        Thursday: 7:30 PM {thursday_meeting} <br><br>
        Friday: 7:30 PM {friday_meeting} <br><br>
        Saturday: 7:30 PM {saturday_meeting} <br><br>
        Lord's Day Morning: 10:00 AM - 12:00 PM Table and prophesying <br><br>
  </body>
</html>
"""

message_text = f"""
If you see this, please reply and ask for a direct email with the schedule and announcements.
"""