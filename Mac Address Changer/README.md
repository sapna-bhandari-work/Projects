````markdown
# MAC Address Changer

## Description

This project is a Python-based MAC address changer developed to modify the Media Access Control (MAC) address of a specified network interface on a Linux system. The tool allows users to spoof or change the MAC address temporarily by bringing the interface down, applying a new MAC address, and bringing it back up.

The project is designed for educational purposes and demonstrates core concepts such as command-line argument parsing, system command execution, regular expressions, and basic network interface manipulation.

---

## Key Features

- Change MAC address of a specified network interface  
- Command-line argument support using options  
- Validates MAC address format before applying  
- Displays current and updated MAC address  
- Uses system-level commands via Python  
- Console-based execution with clear status output  

---

## Technologies Used

- Python 3  
- subprocess  
- optparse  
- re (Regular Expressions)  
- Linux networking utilities (`ifconfig`)  

---

## Project Structure

Project Folder  
├── mac_changer.py  
└── README  

---

## Requirements

- Linux-based operating system  
- Python 3.x  
- Root / sudo privileges  

> ⚠️ This project will **not work on Windows** and is intended for Linux systems only.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/projects.git
````

Navigate to the project directory:

```bash
cd projects
```

Verify Python installation:

```bash
python3 --version
```

---

## Usage

Run the script with root privileges and provide the interface name and new MAC address:

```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

---

## Usage Notes

* The script must be executed with **sudo**
* The interface must exist (e.g., `eth0`, `wlan0`)
* MAC address must follow the format `XX:XX:XX:XX:XX:XX`
* The MAC address change is **temporary** and resets after reboot
* Intended only for controlled and authorized environments

---

## Output

The program prints status messages directly to the console.

Example output:

```text
[+] Current MAC address: 08:00:27:aa:bb:cc
[+] Changing MAC address for eth0 to 00:11:22:33:44:55
[+] MAC address successfully changed to 00:11:22:33:44:55
```

---

## Working Explanation

1. Command-line arguments are parsed using `optparse`.
2. The current MAC address of the interface is extracted using `ifconfig`.
3. The provided MAC address format is validated using regex.
4. The network interface is brought down.
5. A new MAC address is applied to the interface.
6. The interface is brought back up.
7. The script verifies whether the MAC address was changed successfully.

---

## Limitations

* Uses `ifconfig`, which is deprecated on some modern Linux systems
* No automatic interface detection
* No rollback mechanism if MAC change fails
* Works only on Linux

---

## Future Enhancements

* Use `ip link` instead of `ifconfig`
* Add automatic interface listing
* Implement rollback to original MAC address
* Improve error handling and logging
* Add support for random MAC generation

---

## Disclaimer

This project is intended strictly for educational and learning purposes.
Use this tool only on systems and networks where you have explicit authorization.
The author is not responsible for any misuse of this software.

---

## Author

Sapna Bhandari
Third Year B.Sc. Computer Engineering Student

```
```
