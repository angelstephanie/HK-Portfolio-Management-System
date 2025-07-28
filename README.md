# Getting Started

## Download required package
```bash
pip install -r requirements.txt
```

## Running the Frontend Application

To run the frontend application locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/angelstephanie/HK-Portfolio-Management-System.git
cd HK-Portfolio-Management-System
```

### 2. Navigate to the frontend Directory
```bash
cd frontend
```

### 3. Install Dependencies
```bash
npm install
```

### 4. Start the Development Server
```bash
npm start
```

## Fetch Pricing data from Yahoo and save into database
To fetch pricing data from Yahoo and save data into asset table, follow these steps:

### 1.Create table in your local server
Make sure the script in **backend\database\Hong Kong Hackathon.sql** is run and tables are created.

### 2.Update asset_info.json
Add ticket name into **\backend\asset_info.json** if you have.

### 3.Run YahooFetcher
```python3
# example of using fetcher
asset_config = "asset_info.json"
username = "root" # your username
password = "n3u3da!" # your password
schema = "HongKongHackathon" # schema name
    
fetcher = YahooFetcher(asset_config,username,password,password,schema)
fetcher.run()
```

