# 🏠 Fake Address Generator

> Generate realistic, localized fake addresses for testing, development, and demo data — safely and at scale.

![License](https://img.shields.io/github/license/yourusername/fake-address-generator)
![Build](https://img.shields.io/github/actions/workflow/status/yourusername/fake-address-generator/ci.yml?branch=main)
![Version](https://img.shields.io/github/package-json/v/yourusername/fake-address-generator)

---

## ✨ Overview

The **Fake Address Generator** provides realistic, country-specific postal addresses for use in software testing, UI mockups, QA environments, and safe data anonymization. It produces fictional (non-deliverable) addresses while mimicking real-world formatting, structure, and naming conventions.

**Key benefits:**
- Avoid using real addresses during development
- Prevent accidental exposure of user data
- Support for multiple countries and locales
- CLI and REST API interfaces

---

## ⚙️ Features

✅ Multi-country address format support  
✅ Realistic city, state, and postal code generation  
✅ Localized templates (🇺🇸 US, 🇬🇧 UK, 🇩🇪 DE, 🇫🇷 FR, more...)  
✅ Batch export (CSV, JSON, SQL)  
✅ Optional fake geo-coordinates (lat/lng)  
✅ Deterministic seed support for reproducible results  
✅ REST API for automation & test frameworks  
✅ Lightweight, dependency-free CLI

---

## 📦 Installation

### Clone & install

```bash
git clone https://github.com/yourusername/fake-address-generator.git
cd fake-address-generator
npm install          # Node.js version
# or
pip install -r requirements.txt  # Python version
🚀 Usage
CLI (Command Line)
Generate a single fake address:

bash
Copy code
node cli/generate.js
Generate 100 fake addresses (US only) and export to CSV:

bash
Copy code
node cli/generate.js --count 100 --locale us --format csv --output addresses.csv
CLI Options:

Flag	Description	Default
--count	Number of addresses to generate	1
--locale	Locale to use (us, uk, de, etc.)	us
--format	Output format (json, csv, sql)	json
--seed	Optional seed for deterministic results	null
--output	File path to save output	stdout

API (Optional REST Server)
Start the API server:

bash
Copy code
npm run api
POST /api/v1/generate

Request:

json
Copy code
{
  "count": 5,
  "locale": "us",
  "includeGeo": true
}
Response:

json
Copy code
[
  {
    "street": "1944 Maple Drive",
    "city": "San Mateo",
    "state": "CA",
    "postalCode": "94403",
    "country": "United States",
    "latitude": 37.5345,
    "longitude": -122.3041
  },
  ...
]
🗂 Supported Locales
Code	Country	Example Format
us	United States	123 Main St, Chicago, IL 60601
uk	United Kingdom	42 High Street, London, SW1A 1AA
de	Germany	Musterstraße 12, 10115 Berlin
fr	France	18 Rue des Lilas, 75000 Paris
in	India	202 MG Road, Mumbai, MH 400001

Want to contribute a new locale? See the /locales folder and open a PR!

🛡️ Privacy & Ethical Use
This tool does not generate real addresses.

All addresses are fictional and randomly assembled from public datasets, synthetic templates, and generic components.

Do not use these addresses for fraud, impersonation, or anything deceptive.

This is for development, QA, education, and demo purposes only.

Example use cases:

Populate test environments

Create fake user profiles

Anonymize production data dumps

Build UI/UX prototypes with realistic mock data

📁 Example Outputs
JSON:
json
Copy code
{
  "street": "487 Pine Hill Rd",
  "city": "Springfield",
  "state": "IL",
  "postalCode": "62704",
  "country": "United States"
}
CSV:
csv
Copy code
street,city,state,postalCode,country
487 Pine Hill Rd,Springfield,IL,62704,United States
🧪 Tests
Run tests:

bash
Copy code
npm run test
Coverage is tracked and reported using jest (Node) or pytest (Python). All address formats and locale rules are covered by unit tests and snapshot checks.

🤝 Contributing
Want to improve fake data realism or add your country’s format? Contributions are welcome!

Fork the repo

Create a branch: git checkout -b feat/new-locale-in

Add/edit templates under /locales

Write tests

Open a pull request 🚀

📄 License
MIT License © [Your Name or Organization]
See LICENSE for full text.

💬 Contact
For bug reports, feature requests, or support:
📧 Email: xoxoakarsh@gmail.com
🐙 GitHub: @akarshxs

Stay safe, test smart, and build better tools — without risking real data. 🔐

yaml
Copy code

---

Let me know if you'd like:

- A **live demo link** section
- `Dockerfile` or deployment instructions
- Screenshots of the tool
- A badge for `npm` or `PyPI` if you’re publishing it as a package

Also happy to tailor it if you're using a specific stack (e.g. Python + Flask or Node + Express).




Attach

Search

Study

Voice

ChatGPT can make mistakes. Check important info. See Cookie Preferences.
