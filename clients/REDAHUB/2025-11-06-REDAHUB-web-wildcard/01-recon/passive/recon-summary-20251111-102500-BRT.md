# FASE 1 - Reconnaissance Passivo - Results

## Timestamp: 2025-11-11 10:25:00 -03

### DNS & WHOIS
- Domain: redahub.cloud
- Primary IP: 82.29.59.28
- Hostname: srv1065673.hstgr.cloud
- Registrar: ARUBA PEC S.p.A. (Italy)

### Open Ports (Nmap Quick Scan)
- Port 22/tcp: SSH (OpenSSH 9.6p1 Ubuntu 3ubuntu13.13)
- Port 80/tcp: HTTP (Golang net/http server)
- Port 443/tcp: HTTPS (Golang net/http + nginx/1.29.3)
- Port 3000/tcp: HTTP (Easypanel - 🔴 CRITICAL FINDING)

### Technology Stack
- OS: Ubuntu Linux
- Web Server: nginx/1.29.3
- Backend: Golang net/http
- Frontend: React SPA
- Management: Easypanel (port 3000)

### Application Details
- Main App: REDAHUB Sistema Editorial
- Description: Gerenciamento de conteúdo multi-canal
- Language: Portuguese (Brazil)
- Dark mode: Enabled

### OSINT Results
- theHarvester: Executed (awaiting final results)
- amass: Running in background (subdomain enumeration)

### Critical Findings
🔴 FINDING-001: Easypanel Management Panel Exposed on Port 3000
   - Severity: CRITICAL (CVSS 9.1)
   - Status: Documented
   - Next: Manual authentication testing required
