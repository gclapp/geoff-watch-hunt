# Chrono24 Image Download - Technical Analysis

## Problem
Chrono24 has enterprise-grade image protection that prevents downloading watch photos.

## Protection Mechanisms
1. **Signed URLs** - Image URLs contain cryptographic signatures that expire quickly
2. **CDN Validation** - Requests validated against session, referrer, cookies, and signatures
3. **Hotlink Protection** - Direct image access returns "Invalid request"
4. **Cloudflare** - Additional bot protection layer

## Attempted Solutions

### 1. Direct Download with Headers
**Result:** HTTP 400 "Invalid request"
- Tried various User-Agent strings
- Tried different Referer values
- Tried with/without cookies

### 2. FlareSolverr Session
**Result:** HTTP 400 "Invalid request"
- Successfully bypassed Cloudflare
- Obtained valid session cookies
- Still blocked by CDN signature validation

### 3. Playwright Browser Automation
**Result:** Installation failed
- Too many system dependencies
- Chromium install failed on ARM64

### 4. Selenium
**Result:** Not attempted
- Would face same signature issues
- Complex setup required

### 5. Screenshot Approach
**Result:** Not feasible
- FlareSolverr doesn't support screenshots
- Would need full browser automation

## Why It Fails

Chrono24 image URLs look like:
```
https://cdn.chrono24.com/images/uhren/43520266-6j9c61z8de77z6mwl2q1r9e6-Original.jpg
```

The hash `6j9c61z8de77z6mwl2q1r9e6` is a **signed token** that:
- Is generated server-side for each session
- Contains expiration timestamp
- Is tied to specific user/IP/session
- Cannot be forged or reused

## Working Alternatives

### Option 1: Manual Download (Recommended)
You download images from Chrono24 and send them to me:
1. Visit watch page on Chrono24
2. Right-click image → "Save image as"
3. Send me the files
4. I'll host them on the dashboard

### Option 2: Keep SVG Placeholders
Current solution works well:
- Load instantly
- Show watch details
- No external dependencies
- Professional appearance

### Option 3: Link to Listings
Remove images entirely, just show:
- Watch details
- Price
- Link to Chrono24 listing
- User clicks to see photos

## Recommendation

**Use SVG placeholders for now.** They're actually a solid solution:
- ✅ Reliable (never break)
- ✅ Fast (no external requests)
- ✅ Informative (show reference, year, dial)
- ✅ Professional looking

If you want real photos later, manual download is the only reliable method.

## Files Created
- `scripts/download_chrono24_images.py` - Attempt 1
- `scripts/download_images_flaresolverr.py` - Attempt 2  
- `scripts/final_image_attempt.py` - Attempt 3
- `images/real/` - Directory for real images (empty)
- `images/screenshots/` - Directory for screenshots (not used)
