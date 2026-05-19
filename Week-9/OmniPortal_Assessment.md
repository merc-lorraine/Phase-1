# OMNI-PORTAL ASSESSMENT REPORT
**Operator:** **Deadline:** April 5 @ 11:59 PM 

## PHASE 1: AUTH BYPASS (SQLi)
* **Payload Used:** [' OR 1=1 --]
* **Result:** Successfully bypassed login and obtained 'auth_token' cookie.

## PHASE 2: CLIENT-SIDE HIJACK (XSS)
* **Stored XSS Payload:** [<script>alert(document.cookie)</script>]
* **Secret Cookie Captured:** [SUPPORT_TIER_1_SECRET_TOKEN]

## PHASE 3: API ENUMERATION (BOLA)
* **Insecure Order ID:** [501]
* **Confidential Data Leaked:** [501: '1', '$15,000.00', 'Confidential Server Lease']

## PHASE 4: THE REMEDIATION
* **Fix for SQLi:** parameterized queries or prepared statementd which treat input strictly as data, not executable SQL code.
* **Fix for XSS:** A developer must properly encode/escape user input before rendering it in the browser. This ensures the browser treats the input as plain text instead of executable HTML or JavaScript.
* **Fix for API BOLA:** Verify the authenticated user is authorized to access the specific resource being requested. Enforce object-level authorization on every request or use role-based or ownership-based access controls and log unauthorized access attempts.
