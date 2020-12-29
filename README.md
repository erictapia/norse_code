# norse_code
Learning Nornir 3 with Cisco's Always on sandbox.

# My Environment

Python: 3.7.6

OS: OS X

# Setting up environment
```
git clone https://www.github.com/erictapia/norse_code.git
cd norse_code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Running script
```
python sandbox_devices.py
```

# Sample output
```
===============================================================================IOS-XE.Sandbox
===============================================================================
        hostname: ios-xe-mgmt.cisco.com
        serial number: 9GHT70SDYXT

===============================================================================
IOS-XR.Sandbox
===============================================================================
        hostname: sbx-iosxr-mgmt.cisco.com
        serial number: 05EFB4E4D3D

===============================================================================
NX-OS.Sandbox
===============================================================================
        hostname: sbx-nxos-mgmt.cisco.com
        serial number: 9QXOX90PJ62
```