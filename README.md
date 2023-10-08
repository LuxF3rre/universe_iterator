# 🌌 `universe_iterator`

Dive into the infinite possibilities of visual representation! The `universe_iterator` script churns out every conceivable black and white image. Just think about it — **every image you can fathom exists in this realm**. Your cherished family photo, a frame-by-frame sequence of your favorite movie, iconic texts, or even an image capturing this very instant you're reading about `universe_iterator` — they're all in there.

Given the default configurations, we're looking at a staggering count of roughly 2^1000 potential images. But, when you factor in identical images just oriented differently, the unique count narrows down to approximately (2^1000) / 360.

## 🔧 Requirements

Before you set off on this cosmic journey, ensure you have all the needed dependencies. Use the following command to get everything set up:

```bash
poetry install
```

## 🚀 Usage

Embark on your voyage through the visual universe with:

Usage: `universe_iterator.py [OPTIONS]`

### Options:

- `-i, --image_side INTEGER`  
  Set the length of the image's side (in pixels). Must be >= 1.  
  Default value: 100.

- `-o, --ordinal_numbers INTEGER`  
  Specify ordinal numbers of the image variation. Must be >= 0.  
  This is a **required** field.

- `--help`  
  Need some guidance? Just use this to get a helping hand.

## 🖼️ A Glimpse into the Abyss

Get a sneak peek of the boundless possibilities:

![Example result](sample.png)
