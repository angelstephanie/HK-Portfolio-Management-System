from backend.YahooFetcher import YahooFetcher
from backend.repository.Asset_repo import Asset_repo

def setup():
    # Create an instance of AssetService
    yahooFetcher = YahooFetcher()
    asset_repo = Asset_repo()
    
    # Fetch and update assets
    assets = yahooFetcher.fetchByAssetType()
    for asset in assets:
        print(f"Adding asset: {asset}")
        asset_repo.add_asset(asset)
    
if __name__ == "__main__":
    setup()
    print("Assets have been set up successfully.")