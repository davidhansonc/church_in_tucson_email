import datetime
from tools.set_schedule import get_schedule, lords_date

'''UPDATE THE FOLLOWING'''
# update weekly
subject = "Weekly Announcements"
announcements = f"""
Hi saints, <br><br>

This week, due to the semiannual training, there will be no scheduled church meetings except for the prayer meeting on Tuesday night. 
The first video training meeting will be at 7:30 PM on Thursday night. Please arrive by 7:20! See the calendar on our church website for 
the full schedule at churchintucson.org/calendar. 
<br><br>
The subject of the training is "The Divine and Mystical Realm". Living Stream Ministry has uploaded the video recordings of Witness Lee's 
conference on this subject from 1996 (about a year before he died). The saints are encouraged to watch these as a prepartion for the upcoming training. You can find them at https://www.youtube.com/playlist?list=PL_ztWyfQDVVagWfXveRqOKKBbs0bov4_O. 
<br><br>
For the Holy Word for Morning Revival (HWMR) book, we will move on to week 11. In the prophesying meeting next week, saints can share from both the HWMR and from the training. We will then repeat week 11 the following week.

<br><br>
Praise the Lord!
"""

hwmr_week = 11  # update weekly (ascending)
group_seed = 4 # update weekly (DEscending 6-->1)


monday_meeting = f"Life-study of First John (message 15)" # update weekly (ascending)
thursday_meeting = f"Life-study of Acts (message 68)" # update weekly (ascending)
friday_meeting = f"Life-study of Hebrews (message 5)" # update weekly (ascending)    
saturday_meeting = f"Life-study of John (message 17)" # update weekly (ascending)


HWMR = f"""  
HWMR: 
1 & 2 Chronicles, Esra, Nehemiah, and Esther
, week {hwmr_week}
"""
HWMR_LSM = """
https://www.livingstream.com/en/holy-word-for-morning-revival/99999176-hwmr-crystallization-study-of-1-2-chronicles-ezra-nehemiah-and-esther-vol-2.html
"""
HWMR_apple = """
"""
HWMR_google = """
"""
HWMR_kindle = """
"""


schedule = get_schedule(group_seed)
lords_day = lords_date(datetime.date.today())


message_html = f''' <html>
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
        Buy a physical or electronic copy of the HWMR <a href="{HWMR_LSM}">here</a>, 
        <br>
        <br>

        For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
        <a href="https://drive.google.com/file/d/19njXktu271Hx_19Le8r9abYlztqbz3t8/view?usp=sharing">this link</a>.<br>
        </p>

    <h2>Meeting Schedule</h2>
        <p>
        Tuesday: 7:30 PM - Prayer Meeting <br><br>
        Lord's Day Morning: 10:00 AM - 12:00 PM Table and prophesying <br><br>
  </body>
</html>
'''

"""
message_html = f''' <html>
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
        Buy a physical or electronic copy of the HWMR <a href="{HWMR_LSM}">here</a>, 
        <br>
        <br>

        For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
        <a href="https://drive.google.com/file/d/19njXktu271Hx_19Le8r9abYlztqbz3t8/view?usp=sharing">this link</a>.<br>
        </p>

    <h2>Meeting Schedule</h2>
        <p>
        Monday: 7:00 PM - {monday_meeting} <br><br>
        Tuesday: 7:30 PM - Prayer Meeting <br><br>
        Wednesday: No Meeting <br><br>
        Thursday: 7:30 PM - {thursday_meeting} <br><br>
        Friday: 7:30 PM - {friday_meeting} <br><br>
        Saturday: 7:30 PM - {saturday_meeting} <br><br>
        Lord's Day Morning: 10:00 AM - 12:00 PM Table and prophesying <br><br>
  </body>
</html>
'''
"""

message_text = f"""
If you see this, please reply and ask for a direct email with the schedule and announcements.
"""