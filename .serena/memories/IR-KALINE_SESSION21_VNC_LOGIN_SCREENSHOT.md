# IR-KALINE Session 21 - VNC Login Screenshot Analysis

## Date: 27-11-2024

## VNC ACCESS CONFIRMED - Screenshot Evidence

### Screenshot Details
- **Application**: ECI Network Management Station
- **Hostname**: z2-eciaran01
- **Login Status**: "Login incorrect; please try again" (root failed)
- **Interface**: Java-based login dialog

### Login Attempt Results
- `root` - **FAILED** (shown in screenshot)

### Next Credentials to Try
Based on VNC credential spray results:
1. **eci** (10256 bytes response - highest probability)
2. **aranet** (4300 bytes response)
3. **admin** with password Aranet123 (4300 bytes)
4. **nms** 
5. **oracle** (Solaris default)

### ECI NMS Default Credentials to Research
- eci:eci
- admin:admin
- admin:eci
- root:eci
- supervisor:supervisor

### Technical Details
- VNC Port: 5900 (display :0)
- VNC Auth: None (Security Type 1)
- OS: SunOS/Solaris (SunSSH 1.1.9)
- Resolution: 1280x1024

### Session Continuation Notes
- VNC connection is stable and responsive
- Java login dialog requires valid ECI NMS credentials
- Once logged in, should have access to network management interface
- From ECI NMS, can potentially access Juniper routers via internal network

## Full Session Context
- Grafana admin: admin:admin @ 177.54.224.1:8080
- NETCONF creds: openjts:dh273816 (active on Junipers)
- 23+ SSRF datasources created
- 7 Juniper MX routers mapped
- 2.8M InfluxDB telemetry series accessible
