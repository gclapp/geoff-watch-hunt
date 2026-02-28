# 🏛️ 1973 Rolex Datejust Hunt Dashboard

A visual dashboard for tracking Geoff's search for the perfect 1973 Rolex Datejust.

![Dashboard Preview](preview.png)

## ✨ Features

- **📸 Watch Photos** — Each listing includes a clickable image that opens the live listing
- **🔗 Live Links** — Direct links to Bob's Watches, Chrono24, Bulang & Sons, and more
- **🎨 Color-Coded Dials** — Blue and black dials (favorites) get special highlighting
- **📊 Live Stats** — Track active listings, dial colors, and saved items
- **🎯 Preferences Panel** — Your hunt criteria displayed clearly
- **🔍 Smart Filters** — Filter by dial color, two-tone only, or pending review
- **⚡ Auto-Refresh** — Updates every 5 minutes from the JSON data

## 🚀 Deploy to GitHub Pages

### Option 1: New Repository (Recommended)

1. Create a new GitHub repo (e.g., `geoff-watch-hunt`)
2. Upload these files to the root:
   - `index.html`
   - `watch-data.json`
3. Go to **Settings → Pages**
4. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **main** → **/ (root)**
5. Your dashboard will be live at:
   ```
   https://YOURUSERNAME.github.io/geoff-watch-hunt/
   ```

### Option 2: Existing Repository

1. Create a `/docs` folder in your repo
2. Copy `index.html` and `watch-data.json` into `/docs`
3. Go to **Settings → Pages**
4. Set source to **main** branch → **/docs folder**

## 📝 Updating the Dashboard

### Adding New Watches

Edit `watch-data.json` and add a new watch object:

```json
{
  "id": 6,
  "year": 1973,
  "reference": "1601",
  "dialColor": "blue",
  "dialType": "Blue Sigma",
  "case": "Two-tone",
  "size": "36mm",
  "bracelet": "Jubilee",
  "price": "$5,500",
  "source": "Bob's Watches",
  "link": "https://www.bobswatches.com/...",
  "imageUrl": "https://images.bobswatches.com/...",
  "listingUrl": "https://www.bobswatches.com/...",
  "status": "pending_review",
  "dateAdded": "2026-02-28",
  "notes": "Your notes here",
  "geoffRating": null,
  "geoffNotes": null
}
```

### Recording Your Feedback

Update a watch's status and rating:

```json
{
  "status": "liked",     // Options: pending_review, liked, passed, sold
  "geoffRating": 8,      // Your 1-10 rating
  "geoffNotes": "Love the patina but bracelet has stretch"
}
```

### Status Options

- `pending_review` — Yellow badge, not reviewed yet
- `liked` — Green badge, you're interested
- `passed` — Red badge, not for you
- `sold` — Gray badge, no longer available

## 🎨 Dial Color Preferences

The dashboard color-codes based on your preferences:

| Color | Badge | Meaning |
|-------|-------|---------|
| 🔵 Blue | Blue badge | **Favorite** — Top priority |
| ⚫ Black | Black badge | **Favorite** — Top priority |
| 🥂 Champagne | Yellow badge | Acceptable |
| ⚪ Silver | Gray badge | Avoid |

## 📁 File Structure

```
dashboard/
├── index.html          # Main dashboard (UI & logic)
├── watch-data.json     # Watch listings data
└── README.md          # This file
```

## 🔄 Auto-Update Workflow (Optional)

To have the dashboard update automatically when I find new watches, set up a GitHub Action:

1. Go to **Actions** tab in your repo
2. Click **New workflow**
3. Use this template to auto-update from a remote JSON source:

```yaml
name: Update Watch Data

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  workflow_dispatch:  # Manual trigger

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Update watch data
        run: |
          curl -o watch-data.json https://your-data-source.com/watch-data.json
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add watch-data.json
          git commit -m "Update watch listings" || exit 0
          git push
```

## 📱 Mobile Responsive

The dashboard works great on mobile devices:
- Cards stack vertically on small screens
- Filters become scrollable
- Images scale appropriately

## 🛠️ Customization

### Change Colors

Edit the CSS variables in `index.html`:

```css
:root {
  --gold: #C9A961;        /* Your accent color */
  --blue: #2563EB;        /* Favorite dial color */
  --black: #1A1A1A;       /* Text color */
  /* ... etc */
}
```

### Add More Filters

Add filter buttons in the HTML:

```html
<button class="filter-btn" data-filter="sigma">σ Sigma Dials</button>
```

Then update the `renderWatches` function in JavaScript.

## 🐛 Troubleshooting

**Images not loading?**
- Check that `imageUrl` in the JSON is a valid, direct image URL
- Some sites block hotlinking — use local images instead

**Data not updating?**
- Hard refresh: `Ctrl+Shift+R` (or `Cmd+Shift+R` on Mac)
- Check browser console for JSON parsing errors

**GitHub Pages not showing?**
- Ensure repo is public (private repos need GitHub Pro for Pages)
- Check that `index.html` is at the root (or in `/docs` if using that option)

## 📧 Questions?

Ask Cicero — the dashboard is automatically maintained as part of your watch hunt!