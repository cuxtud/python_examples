# Email reports

Send monthly/weekly/daily reports generated in morpheus to an email id.
This will generate the report for the last 30days. Parse the outout of the report and write to CSV. Send the CSV as an attachment in email.

## Getting Started

This script wil generate instanceCost type report. To generate other report types change the value in line 95 with the report type.

### Prerequisites

Make sure requests module is installed

```
pip install requests
```

Update the token in line 26

## Execution

Add this as a python task type. Create a job and schedule the task.