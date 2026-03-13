# Watch Hunt Dashboard - Image Updates

## Changes Made (March 13, 2026)

### 1. Dashboard HTML Updated (`dashboard/index.html`)

**Smart Image Selection Logic:**
- First checks for local downloaded images (`localImagePath`)
- Falls back to remote image URLs (`imageUrl`) if they are valid HTTP/HTTPS URLs
- Ignores SVG placeholders and data URIs
- Shows clickable placeholder when no image is available

**Image Display Improvements:**
- Uses `referrerpolicy="no-referrer"` for remote images (helps with hotlink protection)
- Better error handling - shows "View on [Source]" message if image fails to load
- Clickable placeholder cards that open the listing page directly
- Maintains vendor badge overlay on all cards

### 2. New Scripts Created

**`scripts/watch_image_downloader.py`**
- Downloads images from remote URLs in watch-data.json
- Saves to `dashboard/images/{source}/` directory
- Tracks which watches have local images vs remote
- Updates watch-data.json with `localImagePath` entries

**`scripts/watch_image_scraper.py`**
- Uses browser automation (Scrapling) to scrape images from listing pages
- Handles Chrono24 and Bob's Watches specifically
- Extracts high-resolution images from listing pages
- Downloads and saves locally

### 3. Current Image Status

| Watch ID | Source | Image Status |
|----------|--------|--------------|
| 1-8 | Various | SVG placeholders (need scraping) |
| 9-13 | Chrono24 | Local images downloaded |
| 14 | Chrono24 | Remote URL (working) |
| 15-20 | Chrono24 | Local images downloaded |

### 4. Next Steps to Get More Images

**Option A: Run the image scraper (recommended)**
```bash
cd /home/ubuntu/.openclaw/workspace
python3 scripts/watch_image_scraper.py
```
This will visit each listing page and extract the actual watch images.

**Option B: Manual image URL updates**
For watches 1-8, you can manually find the image URLs on the listing pages and update `watch-data.json`.

### 5. Dashboard Features

- ✅ Shows actual watch images when available
- ✅ Falls back gracefully when no image exists
- ✅ Click-through to listing page from placeholder
- ✅ Vendor badges on all cards
- ✅ Responsive image loading with lazy loading
- ✅ Error handling for broken image links

### 6. Files Modified

- `dashboard/index.html` - Updated createWatchCard function
- `scripts/watch_image_downloader.py` - New (downloads existing remote URLs)
- `scripts/watch_image_scraper.py` - New (scrapes images from listing pages)

---

The dashboard is now ready to display actual watch images from websites. Run the scraper to populate more images.
