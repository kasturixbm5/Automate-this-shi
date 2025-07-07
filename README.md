
# ATS - Automate This Shi

Sick and tired of sending out Advisories tickets?

Boss says to add some AI into "cybersecurity"?

Or having a lazy day to review some CVEs?

Automate This Shi (ATS) is your go-to tool to quickly automate CVE and advisory review workflows. Just feed in a list of CVEs, and it’ll handle the heavy lifting — summarizing severity, description, vectors, and even generating advisory-ready output.


## 🔍 tf does it do
1. Input CVEs

- You provide a plain .txt or .csv file with a list of CVE IDs (e.g., CVE-2024-12345).

- Optionally, pass command-line arguments to define your output format or advisory style.

2. CVE Fetching & Caching

- ATS queries the NVD (National Vulnerability Database) via the nvdlib API.

- Fetched results are cached in logs/ to avoid unnecessary API calls.

- You can force-refresh the data if needed.

3. Data Extraction

- For each CVE, it extracts:

- CVSS score, version, and vector

- Affected components/products

- Short and long descriptions

- Vulnerability type and attack vector (e.g., network, physical)

- References (links, patches, vendor advisories)

4. AI-Powered Advisory Generation

- Uses a lightweight local LLM or an OpenAI-compatible API (configurable) to:

- Translate CVE descriptions into plain English

- Suggest potential impact to organization assets

- Draft a full advisory (e.g., summary, technical analysis, mitigation steps)

- Make it sound professional, technical, or chill — depending on the selected mode (--tone=pro, --tone=casual, etc.)




## Installation

Clone, and install the dependencies

```bash
  git clone https://github.com/kasturixbm5/Automate-this-shi.git
  cd Automate-this-shi
  pip install -r requirements.txt
```
    

## Usage/Examples

By default, the repo contains a few sample CVEs to test. The tool will first check if the CVEs has already been logged in ```/logs/{cve-id}```. If so, any interactions with the requested CVEs will be done locally directly from the log file for faster response. Whenever a new CVE that hasn't been logged, it will query it directly to NIST API platform. Then, it will log it into /logs folder.

## Usage

```javascript
python main.py
```


### Sample Output
```bash
CVE-2025-7102 exists in logs
A vulnerability was found in BoyunCMS up to 1.4.20. It has been declared as critical. This vulnerability affects unknown code of the file application/update/controller/Server.php. The manipulation of the argument phone leads to sql injection. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used.
CVE-2025-7102 | CVSS3.1: 6.3 (MEDIUM)

CVE-2025-7098 exists in logs
A vulnerability, which was classified as critical, was found in Comodo Internet Security Premium 12.3.4.8162. Affected is an unknown function of the component File Name Handler. The manipulation of the argument name/folder leads to path traversal. It is possible to launch the attack remotely. The complexity of an attack is rather high. The exploitability is told to be difficult. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.
CVE-2025-7098 | CVSS3.1: 5.6 (MEDIUM)

CVE-2025-7097 exists in logs
A vulnerability, which was classified as critical, has been found in Comodo Internet Security Premium 12.3.4.8162. This issue affects some unknown processing of the file cis_update_x64.xml of the component Manifest File Handler. The manipulation of the argument binary/params leads to os command injection. The attack may be initiated remotely. The complexity of an attack is rather high. The exploitation is known to be difficult. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.
CVE-2025-7097 | CVSS3.1: 8.1 (HIGH)

CVE-2025-3108 exists in logs
A critical deserialization vulnerability exists in the run-llama/llama_index library's JsonPickleSerializer component, affecting versions v0.12.27 through v0.12.40. This vulnerability allows remote code execution due to an insecure fallback to Python's pickle module. JsonPickleSerializer prioritizes deserialization using pickle.loads(), which can execute arbitrary code when processing untrusted data. Attackers can exploit this by crafting malicious payloads to achieve full system compromise. The root cause includes an insecure fallback mechanism, lack of validation or safeguards, misleading design, and violation of Python security guidelines.
CVE-2025-3108 | CVSSCVSS: N/A (Unknown)
```



## Fetch new data

```javascript
python main.py --force-refresh
```

### Sample Output
```bash
Querying CVE-2025-7102 from the __Internet__
A vulnerability was found in BoyunCMS up to 1.4.20. It has been declared as critical. This vulnerability affects unknown code of the file application/update/controller/Server.php. The manipulation of the argument phone leads to sql injection. The attack can be initiated remotely. The exploit has been disclosed to the public and may be used.
CVE-2025-7102 | CVSS3.1: 6.3 (MEDIUM)

Querying CVE-2025-7098 from the __Internet__
A vulnerability, which was classified as critical, was found in Comodo Internet Security Premium 12.3.4.8162. Affected is an unknown function of the component File Name Handler. The manipulation of the argument name/folder leads to path traversal. It is possible to launch the attack remotely. The complexity of an attack is rather high. The exploitability is told to be difficult. The exploit has been disclosed to the public and may be used. The vendor was contacted early about this disclosure but did not respond in any way.
CVE-2025-7098 | CVSS3.1: 5.6 (MEDIUM)

Querying CVE-2025-7097 from the Internet
CVE-2025-7097 | CVSS3.1: 8.1 (HIGH)

Querying CVE-2025-3108 from the __Internet__
A critical deserialization vulnerability exists in the run-llama/llama_index library's JsonPickleSerializer component, affecting versions v0.12.27 through v0.12.40. This vulnerability allows remote code execution due to an insecure fallback to Python's pickle module. JsonPickleSerializer prioritizes deserialization using pickle.loads(), which can execute arbitrary code when processing untrusted data. Attackers can exploit this by crafting malicious payloads to achieve full system compromise. The root cause includes an insecure fallback mechanism, lack of validation or safeguards, misleading design, and violation of Python security guidelines.
CVE-2025-3108 | CVSSCVSS: N/A (Unknown)
```
