import json
import pandas as pd

# Leggi file JSON
with open("ntp_results.json") as f:
    data = [json.loads(line) for line in f]

# Crea DataFrame
df = pd.DataFrame(data)

# Salva in Excel
df.to_excel("report_ntp.xlsx", index=False)

print("✅ File report_ntp.xlsx creato con successo!")
