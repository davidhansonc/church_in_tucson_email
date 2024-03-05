import datetime
from tools.set_schedule import get_schedule, lords_date

'''UPDATE THE FOLLOWING'''
# update weekly
subject = "Weekly Announcements"
announcements = f"""
Hi saints, <br><br>

This coming weekend is the Tucson book fair! The normal meetings on Saturday and Lord's day will 
be cancelled due to the need for saints to help out at our BFA table. Meetings on Thursday and 
Friday will be determined this week and we'll let the saints know via email or text. On Friday 
morning we need to set up our table. For those who can help, please meet at the hall at 9 AM to start 
loading up our materials. We will send out the final tabling service schedule this week, so if you are 
signed up for tabling, please come during that time. Saints are welcome to come and serve or just 
stop by any time though even if you are not scheduled. Praise the Lord! This will be a glorious week.
"""

hwmr_week = 6 # update weekly (ascending)
group_seed = 5 # update weekly (DEscending 6-->1)


monday_meeting = f"Life-study of Jude (message 1)" # update weekly (ascending)
thursday_meeting = f"Life-study of First Peter (message 23)" # update weekly (ascending)
friday_meeting = f"Life-study of Hebrews (message 34)" # update weekly (ascending)    
saturday_meeting = f"Life-study of John (message 45)" #update weekly (ascending)


HWMR = f"""
HWMR: 
Living and Serving according to God’s Economy concerning the Church
, week {hwmr_week}
"""
HWMR_LSM = """
https://www.livingstream.com/en/holy-word-for-morning-revival/99999283-hwmr-living-and-serving-according-to-gods-economy-concerning-the-church.html
"""
HWMR_apple = """
"""
HWMR_google = """
"""
HWMR_kindle = """
"""


schedule = get_schedule(group_seed)
lords_day = lords_date(datetime.date.today())

message_html = f""" <html>
  <head></head>
  <body>
    <p> {announcements} </p>
    <h2>Meeting Schedule</h2>
        <p>
        Monday: 7:00 PM {monday_meeting} <br><br>
        Tuesday: 7:30 PM prayer meeting <br><br>
        Thursday: TBD <br><br>
        Friday: TBD <br><br>
        Saturday: Tucson book fair 9:00 AM - 5:00 PM <br><br>
        Lord's day: Tucson book fair 9:00 AM - 5:00 PM <br><br>
        </p>
  </body>
</html>
"""

# message_html = f""" <html>
#   <head></head>
#   <body>
#     <p> {announcements} </p>

#     <h2>Next Lord's Day ({lords_day})</h2>
#         <h3>Prophesying Schedule:</h3>
#         <p>
#         <ul>
#             <li>Day 1:  Group {schedule[0]}
#             <li>Day 2:  Group {schedule[1]}
#             <li>Day 3:  Group {schedule[2]}
#             <li>Day 4:  Group {schedule[3]}
#             <li>Day 5:  Group {schedule[4]}
#             <li>Day 6:  Group {schedule[5]}
#         </ul>
#         <i>{HWMR}</i><br>
#         If you need a physical or electronic copy of the upcoming HWMR book, 
# 		    see the <a href="{HWMR_LSM}">LSM Bookstore</a>.
#         <br><br>

#         For the church document with the prophesying, cleaning, and ushering schedules and groups, please use 
#         <a href="https://drive.google.com/file/d/1byQPJ73KjIZqgHkgW_U-4MS6fbE5eRQU/view?usp=drive_link">this link</a>.
#         </p>

#     <h2>Meeting Schedule</h2>
#         <p>
#         Monday: 7:00 PM {monday_meeting} <br><br>
#         Tuesday: 7:30 PM prayer meeting <br><br>
#         Thursday: TBD <br><br>
#         Friday: TBD <br><br>
#         Saturday: Cancelled <br><br>
#         Lord's Day Morning: Cancelled <br><br>
#         </p>
#   </body>
# </html>
# """

message_text = f"""
If you see this, please reply and ask for a direct email with the schedule and announcements.
"""