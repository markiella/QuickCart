# Generate Product Images

This guide explains how to automatically generate product images based on product names.

## Setup Instructions

### Step 1: Get a Free Pexels API Key

1. Go to **https://www.pexels.com/api/**
2. Click **"Get Started"**
3. Sign up for a free account
4. You'll get your **API Key** immediately
5. Copy your API key

### Step 2: Add API Key to Management Command

Edit the file: `store/management/commands/generate_product_images.py`

Find this line (around line 86):
```python
'Authorization': 'YOUR_PEXELS_API_KEY'  # Get free key from pexels.com/api
```

Replace `YOUR_PEXELS_API_KEY` with your actual Pexels API key:
```python
'Authorization': 'YOUR_ACTUAL_API_KEY_HERE'
```

### Step 3: Install Required Package

Make sure `requests` and `Pillow` are installed:
```bash
pip install requests Pillow
```

They should already be in your `requirements.txt`, but if not:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Command

To generate images for products that don't have images:
```bash
python manage.py generate_product_images
```

To regenerate images for ALL products (even those with existing images):
```bash
python manage.py generate_product_images --force
```

## How It Works

1. **Searches Pexels** for images matching each product name
2. **Downloads** the best matching image
3. **Optimizes** the image (resizes to 500x500, converts to JPEG)
4. **Saves** to the product's image field

## Example Output

```
Found 15 products without images
Generating image for: Tomato... ✓ Done
Generating image for: Milk... ✓ Done
Generating image for: Bread... ✓ Done
...
==================================================
Successfully generated: 15 images
==================================================
```

## Troubleshooting

### "Authorization failed"
- Check your API key is correct
- Make sure you copied the entire key without spaces

### "No images found"
- Some product names might not have matches on Pexels
- Try using more generic names (e.g., "Tomato" instead of "Organic Heirloom Tomato")

### "Connection timeout"
- Check your internet connection
- Pexels API might be temporarily unavailable
- Try again later

## Pexels API Limits

**Free Tier:**
- ✅ 200 requests per hour
- ✅ Unlimited image downloads
- ✅ No credit card required

**Paid Tier:**
- Higher request limits
- Priority support

For most small projects, the free tier is more than enough!

## Alternative Services

If you prefer other services:

### Unsplash
- Website: https://unsplash.com/api
- Free tier: 50 requests/hour
- Requires API key

### Pixabay
- Website: https://pixabay.com/api/
- Free tier: 100 requests/hour
- Requires API key

All services provide similar functionality and are free for development/small projects.
