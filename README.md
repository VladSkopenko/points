# Get coordinates via Google Maps API

This script gets latitude and longitude for an address using Google Maps API.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get Google Maps API key:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create new project or select existing one
   - Enable Geocoding API
   - Create API key

3. Set environment variable with API key:

**Windows (PowerShell):**
```powershell
$env:GOOGLE_MAPS_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set GOOGLE_MAPS_API_KEY=your_api_key_here
```

## Usage

Run the script:
```bash
python main.py
```

Script will automatically find coordinates for address:
`24300, Вінницька обл., Тростянецький, м. Тростянець, вул. Наконечного буд.31`

## Result

Script outputs coordinates in format: `latitude, longitude`
