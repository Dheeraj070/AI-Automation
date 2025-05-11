import subprocess

print("\n--- Running amazon_scraper.py ---")
try:
    result = subprocess.run(['python', 'amazon_scraper.py'], check=True, capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error while running amazon_scraper.py:\n{e.stderr}")
    exit(1)  # Exit if the first script fails

print("\n--- Running data_analysis.py ---")
try:
    result = subprocess.run(['python', 'data_analysis.py'], check=True, capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error while running data_analysis.py:\n{e.stderr}")
    exit(1)  # Exit if the second script fails

print("\n--- Running report_generator.py ---")
try:
    result = subprocess.run(['python', 'report_generator.py'], check=True, capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error while running report_generator.py:\n{e.stderr}")
    exit(1)  # Exit if the third script fails


print("\n✅ All scripts executed successfully.")
