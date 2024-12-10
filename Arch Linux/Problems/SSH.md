OBJECTIVE: Create a scalable, manageable reverse SSH tunnel system allowing machines behind restrictive networks to be accessed remotely.

CORE COMPONENTS:
1. Jump Server:
	- Central server accessible from internet
	- Manages reverse tunnel connections
	- Tracks assigned ports and machine status
	- Configuration in /opt/tunnel-manager/config.json
	- Email notifications for tunnel status

2. Machine Registration Process:
	- User runs setup script on their machine
	- Script generates SSH key and collects:
	    - Machine name
	    - Contact email
	    - Purpose/location
	- User sends info to admin
	- Admin reviews and adds to system
	- User gets assigned port and activates tunnel

3. Connection Management:
	- Each machine gets unique port (starting 2222+)
	- Autossh ensures tunnel stability
	- Systemd service keeps tunnel running across reboots
	- Monitoring script checks tunnel status
	- Email alerts for dropped connections

4. Control Features:
	- Enable/disable specific tunnels
	- List all active tunnels
	- Remove machines from system
	- View connection history

5. Security:
	- Dedicated tunnel user on jump server
	- Each machine has unique SSH key
	- Restricted shell access
	- Clear port assignment tracking

6. Client Access:
	- Simple SSH command to connect through jump server
	- Standard SSH clients work (no special software)

Implementation Order:
1. Basic jump server setup
2. Machine registration script
3. Monitoring system
4. Control features