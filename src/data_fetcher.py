import aiohttp
import asyncio
import os
from dotenv import load_dotenv

class DataFCFetcher:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('DATAFC_API_KEY')
        self.base_url = 'https://api.datafc.com/v1'
        
    async def fetch_data(self, endpoint: str, params: dict = None):
        """
        Belirtilen endpoint'ten veri çeker
        
        Args:
            endpoint (str): API endpoint'i
            params (dict): Sorgu parametreleri
            
        Returns:
            dict: API yanıtı
        """
        if not self.api_key:
            raise ValueError("API anahtarı bulunamadı. Lütfen .env dosyasını kontrol edin.")
            
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/{endpoint}"
            async with session.get(url, headers=headers, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise Exception(f"API hatası: {response.status} - {await response.text()}")
                    
    async def get_matches(self, league_id: str = None, date: str = None):
        """
        Maç verilerini çeker
        
        Args:
            league_id (str): Lig ID'si
            date (str): Tarih (YYYY-MM-DD formatında)
            
        Returns:
            dict: Maç verileri
        """
        params = {}
        if league_id:
            params['league'] = league_id
        if date:
            params['date'] = date
            
        return await self.fetch_data('matches', params)
        
    async def get_team_stats(self, team_id: str):
        """
        Takım istatistiklerini çeker
        
        Args:
            team_id (str): Takım ID'si
            
        Returns:
            dict: Takım istatistikleri
        """
        return await self.fetch_data(f'teams/{team_id}/stats')

# Örnek kullanım
async def main():
    fetcher = DataFCFetcher()
    try:
        # Belirli bir ligin maçlarını çek
        matches = await fetcher.get_matches(league_id="TR1")
        print("Maçlar:", matches)
        
        # Belirli bir takımın istatistiklerini çek
        team_stats = await fetcher.get_team_stats("TEAM_ID")
        print("Takım İstatistikleri:", team_stats)
        
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    asyncio.run(main())