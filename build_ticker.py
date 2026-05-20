import random
from datetime import datetime, timezone

# Simulated /ES Data
price = 7220.50 + round(random.uniform(-10, 10), 2)
volume = random.randint(1200000, 1800000)
poc = round(price - random.uniform(2, 5), 2)

# Generate pseudo-volume profile bars (Horizontal)
bars = ""
for i in range(15):
    width = random.randint(10, 150)
    # Highlight the Point of Control (POC)
    color = "#FF6B35" if i == 7 else "#30363d"
    bars += f'<rect x="400" y="{40 + (i*8)}" width="{width}" height="6" fill="{color}" rx="2"/>\n'

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="200">
    <style>
        .text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
        .mono {{ font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; }}
    </style>
    <rect width="600" height="200" rx="10" fill="#0d1117" stroke="#21262d" stroke-width="2"/>

    <text x="30" y="45" fill="#c9d1d9" font-size="22" font-weight="bold" class="text">/ES Futures</text>
    <text x="30" y="65" fill="#8b949e" font-size="12" class="mono">E-mini S&P 500 Matrix</text>

    <text x="30" y="110" fill="#c9d1d9" font-size="32" class="mono">{price:.2f}</text>
    <text x="30" y="135" fill="#8b949e" font-size="14" class="mono">Vol: {volume:,}</text>
    <text x="30" y="160" fill="#FF6B35" font-size="14" class="mono">POC: {poc:.2f}</text>

    <text x="400" y="25" fill="#8b949e" font-size="10" class="mono" text-anchor="start">TPO / VOL PROFILE</text>
    {bars}

    <text x="570" y="185" fill="#484f58" font-size="10" class="mono" text-anchor="end">Last Updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</text>
</svg>"""

with open("assets/es_ticker.svg", "w") as f:
    f.write(svg_content)

print("es_ticker.svg updated.")
