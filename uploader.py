import csv
import json

# Replace with your API key
API_KEY = "API KEY"
URL = f"URL"

# Initialize lists for storing the JSON bodies and curl commands
json_bodies = []
curl_commands = []

# Open the CSV file
with open("your_csv_file.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    # Iterate over each row in the CSV file
    for row in reader:
        # Set up the data for the request
        data = {
            "tags": row["Tags"].split(","),
            "name": row["Cohort Name"],
            "description": row["Description"],
            "query": {
                QUERY HERE
            }
        }

        # Append the JSON body to the list
        json_bodies.append(data)

        # Build the curl command
        headers = ["Content-Type: application/json"]
        curl_command = f"curl -X POST '{URL}'"
        for header in headers:
            curl_command += f" -H '{header}'"
        curl_command += f" -d '{json.dumps(data)}'"
        #curl_command += " \\\n  --silent --output /dev/null"

        # Append the curl command to the list
        curl_commands.append(curl_command)

# Write the JSON array to a file
with open("post_bodies-1.json", "w") as outfile:
    json.dump(json_bodies, outfile)

# Write the curl commands to a .sh file
with open("curl_commands.sh", "w") as outfile:
    for command in curl_commands:
        outfile.write(command + "\n")
