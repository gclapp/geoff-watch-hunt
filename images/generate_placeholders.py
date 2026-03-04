#!/usr/bin/env python3
"""Generate SVG placeholder images for watches"""

import os

watches = [
    {
        "id": 1,
        "ref": "16013",
        "year": "1978",
        "dial": "Blue",
        "case": "Two-tone",
        "source": "Bob's Watches"
    },
    {
        "id": 2,
        "ref": "16013",
        "year": "1979",
        "dial": "Blue faded",
        "case": "Two-tone",
        "source": "Bulang & Sons"
    },
    {
        "id": 3,
        "ref": "1601",
        "year": "1973",
        "dial": "Blue Sigma",
        "case": "Steel",
        "source": "Chrono24"
    },
    {
        "id": 4,
        "ref": "1601",
        "year": "1973",
        "dial": "Deep Blue",
        "case": "Steel",
        "source": "Chrono24"
    },
    {
        "id": 5,
        "ref": "1601",
        "year": "1973",
        "dial": "Black",
        "case": "Unknown",
        "source": "Chrono24"
    },
    {
        "id": 6,
        "ref": "1601",
        "year": "1973",
        "dial": "Blue",
        "case": "Steel",
        "source": "Chrono24"
    },
    {
        "id": 7,
        "ref": "1603",
        "year": "1973",
        "dial": "Silver",
        "case": "Steel",
        "source": "Chrono24"
    },
    {
        "id": 8,
        "ref": "1803",
        "year": "1973",
        "dial": "Day-Date",
        "case": "Gold",
        "source": "Chrono24"
    }
]

for watch in watches:
    # Determine colors based on dial
    if "blue" in watch["dial"].lower():
        bg_color = "#1E3A5F"
        dial_color = "#2563EB"
    elif "black" in watch["dial"].lower():
        bg_color = "#1A1A1A"
        dial_color = "#333333"
    elif "silver" in watch["dial"].lower():
        bg_color = "#4A5568"
        dial_color = "#A0AEC0"
    else:
        bg_color = "#2D3748"
        dial_color = "#4A5568"
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{bg_color};stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1A1A1A;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#F4E4BC;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#C9A961;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#8B7355;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="400" height="280" fill="url(#bg)"/>
  
  <!-- Watch case -->
  <circle cx="200" cy="140" r="90" fill="none" stroke="url(#gold)" stroke-width="8"/>
  <circle cx="200" cy="140" r="82" fill="#0A0A0A"/>
  
  <!-- Dial -->
  <circle cx="200" cy="140" r="75" fill="{dial_color}"/>
  
  <!-- Hour markers -->
  <g fill="url(#gold)">
    <rect x="196" y="75" width="8" height="12" rx="1"/>
    <rect x="196" y="193" width="8" height="12" rx="1"/>
    <rect x="135" y="136" width="12" height="8" rx="1"/>
    <rect x="253" y="136" width="12" height="8" rx="1"/>
  </g>
  
  <!-- Hands -->
  <line x1="200" y1="140" x2="200" y2="100" stroke="url(#gold)" stroke-width="3" stroke-linecap="round"/>
  <line x1="200" y1="140" x2="230" y2="140" stroke="url(#gold)" stroke-width="2" stroke-linecap="round"/>
  
  <!-- Date window -->
  <rect x="230" y="125" width="20" height="16" fill="#F5F5F5"/>
  <text x="240" y="137" font-family="Arial" font-size="10" fill="#1A1A1A" text-anchor="middle">23</text>
  
  <!-- Text info -->
  <text x="200" y="245" font-family="Georgia, serif" font-size="16" fill="#C9A961" text-anchor="middle" font-weight="bold">Rolex Datejust {watch["ref"]}</text>
  <text x="200" y="262" font-family="Arial" font-size="11" fill="#9CA3AF" text-anchor="middle">{watch["year"]} • {watch["dial"]} • {watch["case"]}</text>
  
  <!-- Crown -->
  <rect x="292" y="132" width="6" height="16" fill="url(#gold)" rx="1"/>
</svg>'''
    
    filename = f'watch_{watch["id"]}.svg'
    with open(filename, 'w') as f:
        f.write(svg)
    print(f'Generated: {filename}')

print(f'\\nGenerated {len(watches)} placeholder images')
