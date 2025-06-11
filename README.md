Login Flooder Tool
A Python-based tool designed to simulate multiple login attempts on a phishing page for penetration testing and security research purposes. This tool helps in assessing the resilience of phishing pages against brute-force or flooding attacks.

Features
Multi-threaded Requests: Sends multiple login requests simultaneously to test the target's capacity.
Random Credentials Generation: Generates random usernames and passwords for each request.
Tor Integration: Optionally routes requests through the Tor network to mask the origin IP.
User-Agent Rotation: Uses a list of random User-Agent strings to mimic real browsers.
GUI Interface: Built with tkinter for ease of use.
Logging: Displays real-time logs of successful and failed attempts.
Screenshot
(You can add a screenshot of the GUI here.)

Prerequisites
Before running the tool, ensure you have the following installed:

Python 3.6 or later
Required Python libraries:
bash

Copy
pip install requests pillow stem tkinter
Tor (optional, for IP masking):
Install Tor on your system.
Configure the Tor control port (default: 9051) and set a password in torrc.
Setup
Clone the repository:

bash

Copy
git clone https://github.com/yourusername/login-flooder.git
cd login-flooder
Install dependencies:

bash

Copy
pip install -r requirements.txt
Configure Tor (optional):

Edit the torrc file to enable the control port and set a password:

Copy
ControlPort 9051
HashedControlPassword <your-hashed-password>
Replace TOR_PASSWORD in the script with your actual Tor password.
Run the tool:

bash

Copy
python login_flooder.py
Usage
Enter the Target URL:

Provide the URL of the phishing page (e.g., http://example.com/login).
Set the Number of Requests:

Specify how many login attempts you want to simulate.
Enable Tor (Optional):

Check the "Use Tor to change IP" box to route requests through Tor.
Start the Attack:

Click the "Start Attack" button to begin sending requests.
Monitor Logs:

The GUI displays real-time logs of successful and failed attempts.
Stop the Attack:

Click the "Stop" button to halt the process at any time.
Ethical Considerations
Legal Use: This tool is intended for authorized penetration testing and security research only. Unauthorized use against systems you do not own or have permission to test is illegal.
Responsibility: The user assumes all responsibility for ensuring compliance with local laws and regulations.
Disclosure: Always obtain explicit permission before testing any system.
Code Structure
send_request(): Handles individual HTTP requests, logs results, and rotates Tor IPs if enabled.
generate_random_credentials(): Creates random email and password combinations.
change_tor_ip(): Communicates with the Tor control port to request a new IP.
GUI Components: Built using tkinter, including input fields, buttons, and a logging area.
Example Output

Copy
[✓] {'email': 'abc123@gmail.com', 'pass': 'xyz456'} → 200
[×] {'email': 'def456@gmail.com', 'pass': 'uvw789'} → ConnectionError
Troubleshooting
Tor Connection Issues:

Ensure Tor is running and the control port is correctly configured.
Verify the TOR_PASSWORD in the script matches your Tor configuration.
Request Failures:

Check the target URL for typos.
Ensure the server is reachable and not blocking your IP.
Contributing
Feel free to fork this repository and submit pull requests for improvements. For major changes, open an issue first to discuss the proposed changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
