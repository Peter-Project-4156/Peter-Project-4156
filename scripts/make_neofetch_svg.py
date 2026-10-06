def generate_neofetch_svg():
    user_info = {
        "User": "Peter Ayman",
        "Role": "UI/UX Designer & Front-End Developer",
        "Education": "Business Information Systems (BIS)",
        "Tech Stack": "HTML, CSS, Bootstrap, JavaScript, Figma",
    }

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 220" width="450" height="220">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }}
    .title {{ font-family: monospace; font-size: 14px; fill: #58a6ff; font-weight: bold; }}
    .label {{ font-family: monospace; font-size: 12px; fill: #7ee787; font-weight: bold; }}
    .value {{ font-family: monospace; font-size: 12px; fill: #c9d1d9; }}
    .separator {{ stroke: #30363d; stroke-width: 1px; }}
  </style>
  <rect class="bg" width="100%" height="100%" />
  
  <text x="20" y="30" class="title">peter@github-profile ~ % neofetch</text>
  <line x1="20" y1="40" x2="430" y2="40" class="separator" />

  <text x="20" y="65" class="label">OS:</text>
  <text x="110" y="65" class="value">Web Development &amp; UI/UX</text>

  <text x="20" y="90" class="label">Host:</text>
  <text x="110" y="90" class="value">{user_info['User']}</text>

  <text x="20" y="115" class="label">Role:</text>
  <text x="110" y="115" class="value">{user_info['Role']}</text>

  <text x="20" y="140" class="label">Education:</text>
  <text x="110" y="140" class="value">{user_info['Education']}</text>

  <text x="20" y="165" class="label">Stack:</text>
  <text x="110" y="165" class="value">{user_info['Tech Stack']}</text>

  <text x="20" y="195" class="label">Status:</text>
  <text x="110" y="195" class="value">Building cool web experiences 🚀</text>
</svg>"""

    with open("neofetch.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("✅ Generated Neofetch SVG: neofetch.svg")

if __name__ == "__main__":
    generate_neofetch_svg()