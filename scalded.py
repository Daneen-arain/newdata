from PIL import Image, ImageDraw

# Room dimensions in meters
room_width = 3.2
room_height = 3.0

# Scale: 1m = 100px for drawing
scale = 100
img_width = int(room_width * scale)
img_height = int(room_height * scale)

# Create white background
img = Image.new("RGB", (img_width + 60, img_height + 60), "white")
draw = ImageDraw.Draw(img)

# Draw room outline
draw.rectangle([30, 30, 30 + img_width, 30 + img_height], outline="black", width=3)

# Furniture dimensions (in meters)
furniture = {
    "Bed": (2.05, 1.05),  # length x width
    "Mattress": (1.88, 0.92),
    "Lamp Table": (0.55, 0.55),
    "Chair": (0.4, 0.385),
    "Mirror": (0.45, 1.67),  # width x height (height not to scale in top view)
    "Bookcase": (0.6, 1.8)
}

# Placement coordinates (top-left x, y in meters)
# Keeping bed in same spot: along left wall, head at top
placements = {
    "Bed": (0.1, 0.1),
    "Mattress": (0.1, 0.1),
    "Lamp Table": (2.5, 0.1),
    "Chair": (2.5, 1.0),
    "Mirror": (0.1, 2.0),
    "Bookcase": (2.0, 2.0)
}

# Draw furniture
for name, (fw, fh) in furniture.items():
    x, y = placements[name]
    x1 = 30 + x * scale
    y1 = 30 + y * scale
    x2 = x1 + fw * scale
    y2 = y1 + fh * scale
    draw.rectangle([x1, y1, x2, y2], outline="blue", width=2)
    draw.text((x1 + 5, y1 + 5), name, fill="black")

# Save
path = "/mnt/data/room_layout.png"
img.save(path)
path
