
import csv
import ollama
from openpyxl import load_workbook

MODEL = "llama3.2"

# Load Nora's system prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    system = f.read()

# Load test cases from Excel
workbook = load_workbook("owasp_test_cases.xlsx", read_only=True, data_only=True)
sheet = workbook.active

rows = sheet.iter_rows(values_only=True)
headers = [str(value).strip() for value in next(rows)]

with open("results.csv", "w", newline="", encoding="utf-8-sig") as f_out:
    writer = csv.writer(f_out)

    writer.writerow([
        "id",
        "category",
        "risk_id",
        "prompt",
        "expected_behaviour",
        "response",
        "result",
        "notes",
    ])

    for values in rows:
        row = dict(zip(headers, values))

        try:
            reply = ollama.chat(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": str(row["prompt"])},
                ],
            )

            response = reply["message"]["content"]
            result = ""
            notes = ""

        except Exception as error:
            response = ""
            result = "ERROR"
            notes = str(error)

        writer.writerow([
            row["id"],
            row["category"],
            row["risk_id"],
            row["prompt"],
            row["expected_behaviour"],
            response,
            result,
            notes,
        ])

        print("Done:", row["id"])

workbook.close()
print("All tests processed. Results saved to results.csv")
