from PIL import Image

def image_to_ascii_svg(image_path="source-prepped.png", output_svg="avi-ascii.svg", width=100):
    # الرموز المستخدة للرسم من الأفتح للأغمق
    RAMP = " .`:-=+*cs#%@"
    
    img = Image.open(image_path).convert("L")
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.55)
    img = img.resize((width, height))
    
    pixels = img.getdata()
    ascii_rows = []
    
    for y in range(height):
        row = ""
        for x in range(width):
            pixel_val = pixels[y * width + x]
            char_idx = int((pixel_val / 255) * (len(RAMP) - 1))
            char = RAMP[char_idx]
            row += "&nbsp;" if char == " " else char
        ascii_rows.append(row)
        
    char_w, char_h = 7, 12
    svg_w = width * char_w + 20
    svg_h = height * char_h + 20
    
    text_elements = []
    for idx, row in enumerate(ascii_rows):
        y_pos = 20 + idx * char_h
        delay = idx * 0.05
        text_elements.append(
            f'<text x="10" y="{y_pos}" class="ascii-row" style="animation-delay: {delay:.2f}s;">{row}</text>'
        )
        
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; ry: 8px; }}
    text {{ font-family: monospace; font-size: 10px; fill: #8b949e; white-space: pre; opacity: 0; animation: fadeIn 0.1s forwards; }}
    @keyframes fadeIn {{ to {{ opacity: 1; }} }}
  </style>
  <rect class="bg" width="100%" height="100%" />
  {"\n  ".join(text_elements)}
</svg>"""

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ Generated ASCII SVG: {output_svg}")

if __name__ == "__main__":
    image_to_ascii_svg()