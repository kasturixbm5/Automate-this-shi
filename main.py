import nvdlib
import os
import ast
import sys
from colorama import Fore, Style, init
init(autoreset=True)

# Check if user wants to force-refresh online fetch
force_refresh = '--force-refresh' in sys.argv

def summarize_cve(cve_id):
    try:
        log_path = f"logs/{cve_id}"
        os.makedirs("logs", exist_ok=True)

        # Step 1: Use cached log if it exists and not forcing refresh
        if os.path.exists(log_path) and not force_refresh:
            print(Fore.GREEN + f"{cve_id} exists in logs")
            with open(log_path, "r") as f:
                raw_data = f.read()
            r = ast.literal_eval(raw_data)
            from_log = True
            is_dict = True
        else:
            # Step 2: Fetch from online and cache it
            r_obj = nvdlib.searchCVE(cveId=cve_id)[0]
            print(Fore.CYAN + f"Querying {cve_id} from the Internet")
            with open(log_path, "w") as f:
                f.write(str(vars(r_obj)))  # Logging only
            r = r_obj
            from_log = False
            is_dict = False

        # Step 3: Extract fields depending on data type
        if is_dict:
            description = r['descriptions'][0]['value']
            v31vector = r.get('v31vector')
            v3vector = r.get('v3vector')
            v2vector = r.get('v2vector')
            v31score = r.get('v31score')
            v3score = r.get('v3score')
            v2score = r.get('v2score')
            v31severity = r.get('v31severity')
            v3severity = r.get('v3severity')
            v2severity = r.get('v2severity')
        else:
            description = r.descriptions[0].value
            v31vector = getattr(r, 'v31vector', None)
            v3vector  = getattr(r, 'v3vector', None)
            v2vector  = getattr(r, 'v2vector', None)
            v31score  = getattr(r, 'v31score', None)
            v3score   = getattr(r, 'v3score', None)
            v2score   = getattr(r, 'v2score', None)
            v31severity = getattr(r, 'v31severity', None)
            v3severity  = getattr(r, 'v3severity', None)
            v2severity  = getattr(r, 'v2severity', None)

        # Step 4: Determine CVSS version, score, severity
        if v31vector:
            cvss_version = v31vector.split(':')[1].split('/')[0]
            cvss_score = v31score
            cvss_severity = v31severity
        elif v3vector:
            cvss_version = v3vector.split(':')[1].split('/')[0]
            cvss_score = v3score
            cvss_severity = v3severity
        elif v2vector:
            cvss_version = v2vector.split(':')[1].split('/')[0]
            cvss_score = v2score
            cvss_severity = v2severity
        else:
            cvss_version = 'CVSS'
            cvss_score = 'N/A'
            cvss_severity = 'Unknown'

        # Determine severity color
        if isinstance(cvss_score, (int, float)):
            score_val = float(cvss_score)
            if score_val <= 3.9:
                score_color = Fore.YELLOW       # Low
            elif score_val <= 6.9:
                score_color = Fore.LIGHTYELLOW_EX  # Medium
            elif score_val <= 8.9:
                score_color = Fore.RED          # High
            elif score_val <= 10.0:
                score_color = Fore.LIGHTRED_EX  # Critical
            else:
                score_color = Fore.RESET
        else:
            score_color = Fore.RESET

        # Final output
        print(f"{description}")
        print(f"{cve_id} | CVSS{cvss_version}: {score_color}{cvss_score} ({cvss_severity}){Style.RESET_ALL}\n")

    except Exception as e:
        print(Fore.RED + f"{cve_id} | Error: {e}\n")

def main():
    with open("cve_list", "r") as file:
        cve_ids = [line.strip() for line in file if line.strip()]

    for cve_id in cve_ids:
        summarize_cve(cve_id)

if __name__ == "__main__":
    main()
