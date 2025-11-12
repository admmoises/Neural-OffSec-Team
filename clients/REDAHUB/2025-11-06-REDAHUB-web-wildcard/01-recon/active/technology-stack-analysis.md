# Technology Stack Analysis - REDAHUB

---
**Timestamp:** 2025-11-11 10:29:00 -03
**Engagement:** 2025-11-06-REDAHUB-web-wildcard
**Target:** https://redahub.cloud/
---

## Frontend Stack

### React Single Page Application (SPA)
- **Framework:** React.js (production build)
- **Build Tool:** Likely Webpack/Vite (chunked JS bundles)
- **Language:** Portuguese (Brazil)
- **Theme:** Dark mode enabled by default
- **Assets:**
  - `/static/js/main.023e6df6.js` - Main JS bundle (hash: 023e6df6)
  - `/static/css/main.3e386794.css` - Main CSS bundle (hash: 3e386794)
  - `/manifest.json` - PWA manifest
  - `/favicon.ico` - Favicon
  - `/logo192.png` - App icon

### robots.txt Configuration
```
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:
```
**Analysis:** No crawling restrictions - all paths indexable by search engines

### PWA (Progressive Web App)
- Manifest present at `/manifest.json`
- Theme color: `#0a0e27` (dark blue)
- Apple touch icon available
- Likely supports offline functionality

## Backend Stack

### Web Server
- **Server:** nginx/1.29.3
- **Backend:** Golang net/http server
- **Reverse Proxy:** nginx → Golang backend

### HTTP Headers Analysis
```
HTTP/2 200
accept-ranges: bytes
cache-control: no-cache, no-store, must-revalidate
content-type: text/html
date: Tue, 11 Nov 2025 13:24:01 GMT
etag: "690a5c0d-2bf"
expires: 0
last-modified: Tue, 04 Nov 2025 20:03:25 GMT
pragma: no-cache
server: nginx/1.29.3
content-length: 703
```

### Security Headers Assessment

| Header | Status | Risk |
|--------|--------|------|
| **Strict-Transport-Security (HSTS)** | ❌ Missing | 🟡 Medium |
| **Content-Security-Policy (CSP)** | ❌ Missing | 🔴 High |
| **X-Frame-Options** | ❌ Missing | 🟡 Medium |
| **X-Content-Type-Options** | ❌ Missing | 🟢 Low |
| **Referrer-Policy** | ❌ Missing | 🟢 Low |
| **Permissions-Policy** | ❌ Missing | 🟢 Low |

**Finding:** Application lacks critical security headers, particularly CSP and HSTS.

### Cache Configuration
- **Cache-Control:** `no-cache, no-store, must-revalidate`
- **Pragma:** `no-cache`
- **Expires:** `0`

**Analysis:** Aggressive no-caching policy applied to HTML (good for SPA updates, but no caching for static assets detected yet)

## Infrastructure

### Hosting
- **Provider:** HSTGR.cloud (Hostinger)
- **Hostname:** srv1065673.hstgr.cloud
- **IP:** 82.29.59.28
- **Location:** Likely Europe (Hostinger datacenter)
- **Domain Registrar:** ARUBA PEC S.p.A. (Italy)

### Operating System
- **OS:** Ubuntu Linux
- **SSH:** OpenSSH 9.6p1 Ubuntu 3ubuntu13.13

### Open Services
| Port | Service | Version | Risk |
|------|---------|---------|------|
| 22 | SSH | OpenSSH 9.6p1 | 🟢 Low (if hardened) |
| 80 | HTTP | Golang | 🟢 Low (redirects to HTTPS) |
| 443 | HTTPS | Golang + nginx/1.29.3 | 🟢 Low |
| 3000 | HTTP | **Easypanel Management** | 🔴 **CRITICAL** |

## Application Architecture

### Deployment Platform
- **Management:** Easypanel (exposed on port 3000)
- **Container:** Likely Docker-based (Easypanel is a Docker management platform)
- **Orchestration:** Easypanel manages container deployments

### Application Description
**Title:** REDAHUB Sistema Editorial
**Description:** Gerenciamento de conteúdo multi-canal
**Purpose:** Editorial content management system
**Market:** Brazilian/Portuguese-speaking markets

### Technology Summary

```
┌─────────────────────────────────────┐
│          Client Browser             │
│         (React SPA UI)              │
└─────────────┬───────────────────────┘
              │ HTTPS (443)
              ▼
┌─────────────────────────────────────┐
│       nginx/1.29.3 (Reverse Proxy)  │
└─────────────┬───────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│    Golang Backend API Server        │
│    (net/http framework)             │
└─────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│         Database (TBD)              │
│    (PostgreSQL/MySQL/MongoDB?)      │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│      Easypanel (Port 3000)          │
│   Container Management Platform     │
│          🔴 EXPOSED!                │
└─────────────────────────────────────┘
```

## Potential Attack Vectors

### 🔴 Critical
1. **Easypanel Exposure (Port 3000)** - Direct access to deployment platform
2. **Missing CSP** - XSS attacks not mitigated by headers

### 🟡 Medium
3. **Missing HSTS** - SSL stripping attacks possible
4. **Missing X-Frame-Options** - Clickjacking possible
5. **SSH Exposed** - Brute force potential (if weak credentials)

### 🟢 Low
6. **React SPA** - Client-side routing may expose API endpoints
7. **No sitemap.xml** - Manual discovery of routes required
8. **Aggressive no-cache** - Performance impact (minor security benefit)

## Recommendations

### Immediate (Critical)
1. **Close Port 3000** or restrict to internal IPs only
2. **Implement CSP** headers to prevent XSS
3. **Enable HSTS** with `max-age=31536000; includeSubDomains; preload`

### Short-term (7 days)
4. Implement X-Frame-Options: DENY or SAMEORIGIN
5. Add X-Content-Type-Options: nosniff
6. Configure Referrer-Policy: strict-origin-when-cross-origin
7. Review SSH access controls (key-only auth, fail2ban)

### Medium-term (30 days)
8. Implement rate limiting on API endpoints
9. Add security monitoring/logging
10. Regular security scanning and pentesting
11. Implement WAF (Web Application Firewall)

## Technology Versions

| Component | Version | Latest | Status |
|-----------|---------|--------|--------|
| nginx | 1.29.3 | 1.25.x (stable) | ⚠️ Needs verification |
| OpenSSH | 9.6p1 | 9.6p1 | ✅ Current |
| Ubuntu | 3ubuntu13.13 | Latest LTS | ✅ Current |
| Golang | Unknown | TBD | ⏳ Needs detection |
| React | Unknown | TBD | ⏳ Needs detection |

---

**Next Steps:**
- [ ] Analyze React bundle for API endpoints
- [ ] Test discovered API endpoints
- [ ] Verify Golang version via headers or error messages
- [ ] Complete nmap full scan for additional services
- [ ] SSL/TLS cipher suite analysis
- [ ] Manual testing of Easypanel authentication
