import datetime
from tools.set_schedule import get_schedule, lords_date

'''UPDATE THE FOLLOWING'''
# update weekly
subject = "Weekly Announcements"
announcements = f"""
Hi saints, <br><br>

We have the normal schedule this week. We are beginning week 1 of the new HWMR from the recent ITERO. 
See the links below if you still need to get a copy.

<br><br>
Jesus is Lord!
"""

hwmr_week = 1  # update weekly (ascending)
group_seed = 2 # update weekly (DEscending 6-->1)


monday_meeting = f"Life-study of First John (message 20)" # update weekly (ascending)
thursday_meeting = f"Life-study of First Peter (message 1)" # update weekly (ascending)
friday_meeting = f"Life-study of Hebrews (message 12)" # update weekly (ascending)    
saturday_meeting = f"Life-study of John (message 23)" #update weekly (ascending)


HWMR = f"""
HWMR: 
Knowing, Experiencing, and Living the All-inclusive Christ for the Genuine Church Life
Making Ourselves Ready for the Lord's Coming
, week {hwmr_week}
"""
HWMR_LSM = """
https://www.livingstream.com/en/holy-word-for-morning-revival/99999246-hwmr-knowing-experiencing-and-living-the-all-inclusive-christ-for-the-genuine-church-life.html
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
        <i>{HWMR}</i><br>
        If you need a physical copy of the upcoming HWMR book, see the <a href="{HWMR_LSM}">LSM Bookstore</a>.<br>
        For electronic versions, see the following links: <a href="{HWMR_kindle}">Kindle</a> | 
        <a href="{HWMR_google}">Google Play</a> | 
        <a href="{HWMR_apple}">iBook</a>
        <br><br>

        For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
        <a href="https://drive.google.com/file/d/1byQPJ73KjIZqgHkgW_U-4MS6fbE5eRQU/view?usp=drive_link">this link</a>.
        <br><br>
        
        See <a href="https://book.passkey.com/event/50571223/owner/3004/home">this link</a> to reserve a hotel with 
        the LSM discount for the upcoming Dallas Thanksgiving conference.
        <br><br>

        <a href="https://sites.google.com/view/elimsprings/english/events/gospel-trips-2023">Here</a> 
        is the link for info and to sign up for the October Germany gospel trips. 
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