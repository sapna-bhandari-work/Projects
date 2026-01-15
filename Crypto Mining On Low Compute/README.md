```markdown
# MineCryptoOnWifiRouter

## Description

This project demonstrates how a **low-power Wi-Fi router** can be used to mine cryptocurrency using its built-in CPU. The miner runs directly on an **OpenWRT-based router** and connects to the **Duino-Coin** network, a lightweight cryptocurrency designed for constrained devices such as routers, microcontrollers, and embedded systems.

The project is intended **strictly for educational purposes** and showcases how blockchain mining concepts can be applied to **resource-constrained hardware**.

---

## Key Features

- Cryptocurrency mining on low-power Wi-Fi routers  
- Compatible with OpenWRT-based devices  
- Lightweight CPU-based mining using SHA-1 hashing  
- Automatic mining pool selection  
- LED indicators for accepted and rejected shares  
- Continuous mining with automatic fault recovery  
- Minimal dependencies and low memory usage  

---

## Technologies Used

- Python 3  
- Socket Programming  
- Cryptographic Hashing (SHA-1)  
- OpenWRT (Embedded Linux)  
- Duino-Coin Mining Protocol  

---

## Project Structure

```

Project Folder
├── miner.py
├── README.md
└── LICENSE

````

---

## Requirements

### Hardware
- Wi-Fi router compatible with **OpenWRT**
- Stable internet connection

### Software
- OpenWRT installed on the router  
- Python 3  
- Required packages:
  - `requests`
  - `coreutils-nohup`

---

## Installation

### Step 1: Flash OpenWRT
Flash your router with **OpenWRT**.  
⚠️ Flashing OpenWRT may void your router warranty.

Refer to the official OpenWRT documentation for your router model.

---

### Step 2: SSH into the Router

**Linux / macOS**
```bash
ssh root@<router-ip>
````

**Windows**

* Use **PuTTY**
* Default SSH port: `22`

---

### Step 3: Install Dependencies

```bash
opkg update
opkg install python3
opkg install coreutils-nohup
```

---

### Step 4: Configure the Miner

Open `miner.py` and update:

```python
username = "sapna"
mining_key = "None"
```

(Optional)
Enable LED indicators by setting:

```python
leds = True
```

LED names can be found at:

```
OpenWRT Web Interface → System → LED Configuration
```

---

### Step 5: Upload the Script

Use a tool like **WinSCP**:

* Protocol: `SCP`
* Upload `miner.py` to the router

---

## Usage

Run the miner:

```bash
python3 miner.py
```

To keep mining in the background:

```bash
nohup python3 miner.py &
```

Stop the miner using:

```bash
Ctrl + C
```

---

## Output

The miner displays:

* Connection status
* Accepted / rejected shares
* Hashrate (kH/s)
* Mining difficulty
* Timestamped logs

Example output:

```
12:45:10 : Accepted share 83421 Hashrate 87 kH/s Difficulty 2400
```

---

## Tested Routers

| Model              | Hashrate  | Difficulty | Estimated Output |
| ------------------ | --------- | ---------- | ---------------- |
| AVM Fritz!Box 4040 | ~100 kH/s | 2400       | ~10–15 DUCO/day  |
| TP-LINK WR841N     | ~5 kH/s   | 5000       | Very low         |

⚠️ Profitability is extremely low. This project is **not intended for financial gain**.

---

## Working Explanation

1. The miner connects to a Duino-Coin pool server
2. A mining job is requested from the server
3. The router performs SHA-1 hashing on the CPU
4. A valid nonce is searched within difficulty limits
5. The result is submitted back to the pool
6. Accepted or rejected shares are logged
7. LED indicators reflect mining status
8. The miner runs continuously and auto-recovers on failure

---

## Limitations

* Extremely low mining profitability
* Router CPU constraints
* No GPU or ASIC support
* Increased router CPU usage and heat
* Not suitable for production mining

---

## Ethical & Legal Disclaimer

This project is developed **strictly for educational and learning purposes**.

* Do **NOT** mine on routers you do not own
* Do **NOT** deploy on institutional or ISP-provided networks
* Always inform users before running mining software

The author is **not responsible for any misuse** of this software.

---

## Author

**Sapna Bhandari**
Third Year B.Sc. Computer Engineering Student

```
```
