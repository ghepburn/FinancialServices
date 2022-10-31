# FinancesAnalysis
Automated analysis and presentation of personal financial data

# ToDo
Data Storage
- Setup DB tables
	- Transaction Table
	- Mappings table
	- logs table
Data Import Service
- Create an import script which calls and connects to an "import transactions" API endpoint
	- Understands where data files are
	- Transforms CSV data into JSON
	- Sends JSON to API
	- Sends logs to API
API
- Import endpoint
	- Accepts JSON transactional data and loads it into DB
- Mapping endpoint
	- CRUD endpoint for different "maps" of transactions files. Ex: BMO credit card, TD chequings. 
- Logging endpoint
	- GET and POST logs created from imports
- Transaction endpoint
	- For frontend to GET transaction data
	- Support "before" and "after" parameters for date filtering
# Setup


# How It Works
