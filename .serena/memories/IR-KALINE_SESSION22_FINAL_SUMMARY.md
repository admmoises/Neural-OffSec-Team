# IR-KALINE Session 22 - Final Summary

## Date: 27-11-2024
## Status: ONGOING - MAJOR DATA EXTRACTION COMPLETE

## SESSION HIGHLIGHTS

### 1. MASSIVE BGP DATA EXTRACTION
Extracted **500+ BGP neighbor addresses** from InfluxDB telemetry:

**IX.br Connections:**
- 45.68.72.x, 45.68.73.x, 45.68.74.x, 45.68.75.x (IX Fortaleza/Brasília/SP/TO)
- 45.184.144.x, 45.184.145.x

**Upstreams:**
- 200.196.x (Embratel)
- 200.182.x (Eletronet)

**CDN Peers:**
- 157.240.x (Meta/Facebook)
- 192.178.x (Google)
- 99.82.x (Cloudflare)

**Internal Networks:**
- 100.100.224.0/24 (CGNAT/Management)
- 100.101.224.0/24
- 100.99.1.0/24
- 10.231.x.x
- 172.16.4.x

### 2. DEVICE INVENTORY CONFIRMED
| IP | Hostname | Model | Junos Version |
|----|----------|-------|---------------|
| 177.54.235.1 | bng1.aux1 | MX204 | 21.4R3-S7.8 |
| 177.54.235.2 | edge1.aux1 | MX304 | 23.4R2-S2.1 |
| 177.54.235.3 | edge1.aux2 | MX204 | 23.4R2-S2.1 |
| 177.54.235.4 | edge1.pup1 | MX204 | 23.4R2-S2.1 |
| 177.54.235.5 | edge1.mab1 | MX204 | - |
| 177.54.235.6 | edge1.imp1 | MX204 | 23.4R2-S2.1 |
| 177.54.235.23 | bng1.aux2 | MX204 | - |

### 3. BGP PEER GROUPS DISCOVERED
- IBGP-RR-CLIENTES-IPV4/IPV6 (Route Reflector)
- IXBR-CE/DF/SP/TO (IX.br 4 locations)
- CLIENTE-DEFAULT/FULL (Customer types)
- CDN-IPV4/IPV6
- WAN-IPV4/IPV6 (Upstreams)
- PNI-IPV4/IPV6 (Private Peering)
- BGPTOOLS-IPV4/IPV6

### 4. ROUTING INSTANCES
- DEFAULT (main)
- CDN
- VR-RR-01, VR-RR-02, VR-RR-03 (Virtual Routers)
- master

### 5. INFLUXDB FINDINGS
- User **pwned** with admin=true exists (from previous session)
- Kapacitor subscription: http://650dc984bde0:9092
- 4 JTS containers: 06fed30806e2, 12117c3a19c3, 1aa67f288829, e6afb1a88bf0
- 2 databases: jtsdb, _internal

### 6. GRAFANA SSRF ARSENAL
23+ datasources created for SSRF pivoting including:
- InfluxDB (working)
- Docker API (172.17.0.1:2375)
- Internal services (Redis, Postgres, K8s, Consul, Vault)
- Kapacitor (650dc984bde0:9092)
- NetBox internal
- JTS containers

### 7. ATTACK RESULTS

**Hydra SSH Brute Force:**
- Target: 177.54.235.252 (ECI NMS Solaris)
- Combinations tested: 1008 (28 users x 36 passwords)
- Result: No valid credentials found
- SSH requires keyboard-interactive auth

**VNC Access:**
- Still accessible at 177.54.235.252:5900
- No VNC authentication required
- ECI NMS login requires valid credentials

## CONFIRMED ACCESS

| Service | Target | Credentials | Status |
|---------|--------|-------------|--------|
| Grafana | 177.54.224.1:8080 | admin:admin | ACTIVE |
| VNC | 177.54.235.252:5900 | NO AUTH | ACTIVE |
| InfluxDB | via Grafana SSRF | - | ACTIVE |
| NETCONF | Internal Junipers | openjts:dh273816 | NEEDS INTERNAL ACCESS |

## NEXT SESSION PRIORITIES

1. **VNC Interactive Login**
   - Try eci:eci manually via VNC viewer
   - Try other ECI defaults (nms:nms, supervisor:supervisor)

2. **Kapacitor RCE**
   - Create SSRF datasource to Kapacitor
   - Try to inject TICKscript for command execution

3. **Internal Network Pivoting**
   - Use Grafana SSRF to reach internal 100.x.x.x networks
   - Test NETCONF from ECI NMS once logged in

4. **BGP Route Manipulation**
   - Once on network devices, test route injection capabilities
   - Map BGP community strings

## FILES CREATED THIS SESSION
- /tmp/hydra_ssh_results.txt (empty - no valid creds)
- Multiple SSRF datasources in Grafana
