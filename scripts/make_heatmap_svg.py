import urllib.request
import re

def generate_heatmap_svg(github_username="PeterAyman"):
    # استخدام رابط المساهمات المباشر من GitHub
    url = f"https://github-contributions-api.johannchopin.fr/{github_username}"
    
    # محاولة جلب SVG المساهمات عبر الخدمة المباشرة
    fallback_url = f"https://ghchart.rshah.org/40c463/{github_username}"
    
    req = urllib.request.Request(fallback_url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            svg_raw = response.read().decode('utf-8')
            
            # تغليف الخريطة داخل تصميم التيرمينال الشفاف
            svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 120" width="720" height="120">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }}
  </style>
  <rect class="bg" width="100%" height="100%" />
  <g transform="translate(15, 15)">
    {svg_raw}
  </g>
</svg>"""
            
            with open("heatmap.svg", "w", encoding="utf-8") as f:
                f.write(svg_content)
            print("✅ Generated Heatmap SVG: heatmap.svg")
            
    except Exception as e:
        print(f"❌ Error fetching contributions: {e}")

if __name__ == "__main__":
    generate_heatmap_svg()