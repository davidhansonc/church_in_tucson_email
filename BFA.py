full_map = "https://tucsonfestivalofbooks.org/?mid=313"
partial_maps = "https://tucsonfestivalofbooks.org/?mid=312"
BFA_guide = "https://biblesforamerica.org/guide/distribution-guide-2020-01-08.pdf"
exhibitor_handbook = "https://tucsonfestivalofbooks.org/?mid=305"
tfb_webpage = "https://tucsonfestivalofbooks.org/"
schedule = """
<h4>Saturday, March 15</h4>
<table>
    <tr>
        <th>Time</th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
    </tr>
    <tr><td>9:30 AM - 10:00 AM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>10:00 AM - 10:30 AM</td><td>Craig</td><td>David H.</td><td>Jaime T.</td><td>Joel C.</td></tr>
    <tr><td>10:30 AM - 11:00 AM</td><td>Craig</td><td>David H.</td><td>Jaime T.</td><td>Joel C.</td></tr>
    <tr><td>11:00 AM - 11:30 AM</td><td>Craig</td><td>David H.</td><td>Joel C.</td><td>DC</td></tr>
    <tr><td>11:30 AM - 12:00 PM</td><td>Craig</td><td>David H.</td><td>Joel C.</td><td>DC</td></tr>
    <tr><td>12:00 PM - 12:30 PM</td><td></td><td>Joel C.</td><td>DC</td><td></td></tr>
    <tr><td>12:30 PM - 1:00 PM</td><td>Joel C.</td><td>DC</td><td></td><td></td></tr>
    <tr><td>1:00 PM - 1:30 PM</td><td>DC</td><td>Jonathan</td><td></td><td></td></tr>
    <tr><td>1:30 PM - 2:00 PM</td><td>DC</td><td>Jonathan</td><td></td><td></td></tr>
    <tr><td>2:00 PM - 2:30 PM</td><td>Jaime T.</td><td>Judy</td><td></td><td></td></tr>
    <tr><td>2:30 PM - 3:00 PM</td><td>Jaime T.</td><td>Judy</td><td></td><td></td></tr>
    <tr><td>3:00 PM - 3:30 PM</td><td>Craig</td><td>Judy</td><td></td><td></td></tr>
    <tr><td>3:30 PM - 4:00 PM</td><td>Craig</td><td>Judy</td><td></td><td></td></tr>
    <tr><td>4:00 PM - 4:30 PM</td><td>Craig</td><td>Judy</td><td></td><td></td></tr>
    <tr><td>4:30 PM - 5:00 PM</td><td>Craig</td><td>Judy</td><td></td><td></td></tr>
    <tr><td>5:00 PM - 5:30 PM</td><td>Craig</td><td>Judy</td><td></td><td></td></tr>
</table>

<h4>Lord's Day, March 16</h4>
<table>
    <tr>
        <th>Time</th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
    </tr>
    <tr><td>9:30 AM - 10:00 AM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>10:00 AM - 10:30 AM</td><td>Isaac/Esther</td><td>Joel C.</td><td></td><td></td></tr>
    <tr><td>10:30 AM - 11:00 AM</td><td>Isaac/Esther</td><td>Joel C.</td><td></td><td></td></tr>
    <tr><td>11:00 AM - 11:30 AM</td><td>Isaac/Esther</td><td>Joel C.</td><td></td><td></td></tr>
    <tr><td>11:30 AM - 12:00 PM</td><td>Isaac/Esther</td><td>Joel C.</td><td></td><td></td></tr>
    <tr><td>12:00 PM - 12:30 PM</td><td>Isaac/Esther</td><td>Joel C.</td><td></td><td></td></tr>
    <tr><td>12:30 PM - 1:00 PM</td><td>Isaac/Esther</td><td>Joel C.</td><td></td><td></td></tr>
    <tr><td>1:00 PM - 1:30 PM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>1:30 PM - 2:00 PM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>2:00 PM - 2:30 PM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>2:30 PM - 3:00 PM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>3:00 PM - 3:30 PM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>3:30 PM - 4:00 PM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>4:00 PM - 4:30 PM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>4:30 PM - 5:00 PM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
    <tr><td>5:00 PM - 5:30 PM</td><td>Craig</td><td>David H.</td><td></td><td></td></tr>
</table>
"""

# Update the HTML message to include formatted group orders
message_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Tucson Festival of Books Information</title>
</head>
<body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; color: #333;">
    <div style="max-width: 600px; margin: auto; border: 10px solid #eee; padding: 20px;">
        <p>
		Hi saints,
		<br><br>
		Below is the key information for this weekend's book festival and our Bibles for America booth.

        <h4 style="color: #0056b3; margin-top: 40px;">Booth Location</h4>
		We are <strong>Booth 180</strong> on the southwest side of the book festival. Two map types are provided. The first 
		is a 
        <a href="{full_map}" style="color: #0056b3; text-decoration: none;">full map</a>
        of the entire book festival, and a 
		<a href="{partial_maps}" style="color: #0056b3; text-decoration: none;">version broken up</a> into smaller sections.

        <h4 style="color: #0056b3; margin-top: 40px;">BFA</h4>
        Here is the BFA distribution guide that we referenced last Lord's day. It would be great if everyone could read through 
		the relevant parts is possible <a href="{BFA_guide}" style="color: #0056b3; text-decoration: none;">BFA Distribution Guide</a>
		Etc.

        <h4 style="color: #0056b3; margin-top: 40px;">Parking</h4>
        I believe the Highland Garage, Park Avenue Garage and campus surface lots will have free parking this weekend. 
		There should be street parking available too. 
		Other garages will be paid and the 2nd street garage will not be available over this weekend.
		
        <h4 style="color: #0056b3; margin-top: 40px;">Serving Schedule</h4>
		The hours of the festival are from 9:30 AM to 5:30 PM. Here is the schedule for the saints who signed up to serve:
		{schedule}
        <br>
		Again, if you didn't get a chance to sign up, you are still welcome.

		<br><br><br>
        The weather may bring a mix of rain or sun, so dress appropriately. 
		There are plenty of places to buy food and water nearby.
		
		<br><br>
		Praise the Lord for this opportunity!
		</p>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
	# Define the filename for the output HTML file
	filename = "./email.html"

	# Writing the HTML content to a file
	with open(filename, 'w', encoding='utf-8') as file:
		file.write(message_html)

	print(f"HTML email saved to {filename}")