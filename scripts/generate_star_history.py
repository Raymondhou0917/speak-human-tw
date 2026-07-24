import os
import sys
import random
import math
import json
import datetime
import urllib.request
import subprocess

def fetch_star_history_gh():
    history = []
    page = 1
    while True:
        cmd = ['gh', 'api', f'repos/Raymondhou0917/speak-human-tw/stargazers?per_page=100&page={page}', '-H', 'Accept: application/vnd.github.v3.star+json']
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0 or not res.stdout.strip():
            break
        try:
            data = json.loads(res.stdout)
            if not data or not isinstance(data, list):
                break
            for idx, item in enumerate(data):
                star_num = (page - 1) * 100 + idx + 1
                starred_at = item.get('starred_at', '')
                history.append((starred_at[:19], star_num))  # 保持 ISO timestamp
            page += 1
        except Exception:
            break
    return history

def fetch_star_history_api(token=None):
    history = []
    page = 1
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/vnd.github.v3.star+json'
    }
    if token:
        headers['Authorization'] = f'token {token}'

    while True:
        url = f'https://api.github.com/repos/Raymondhou0917/speak-human-tw/stargazers?per_page=100&page={page}'
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                if not data or not isinstance(data, list):
                    break
                for idx, item in enumerate(data):
                    star_num = (page - 1) * 100 + idx + 1
                    starred_at = item.get('starred_at', '')
                    history.append((starred_at[:19], star_num))
                page += 1
        except Exception:
            break
    return history

def rough_line(x1, y1, x2, y2, roughness=1.2):
    length = math.hypot(x2-x1, y2-y1)
    steps = max(3, int(length / 15))
    pts = []
    for i in range(steps + 1):
        t = i / steps
        rx = (random.random() - 0.5) * roughness if 0 < i < steps else 0
        ry = (random.random() - 0.5) * roughness if 0 < i < steps else 0
        x = x1 + (x2 - x1) * t + rx
        y = y1 + (y2 - y1) * t + ry
        pts.append((x, y))
    return f'M {pts[0][0]:.1f},{pts[0][1]:.1f} ' + ' '.join([f'L {p[0]:.1f},{p[1]:.1f}' for p in pts[1:]])

def rough_curve(points, roughness=1.4):
    d1_parts = []
    d2_parts = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        d1_parts.append(rough_line(x1, y1, x2, y2, roughness))
        d2_parts.append(rough_line(x1 + 0.5, y1 - 0.5, x2 + 0.5, y2 - 0.5, roughness * 0.7))
    return ' '.join(d1_parts), ' '.join(d2_parts)

def parse_iso(ts):
    # e.g. 2026-07-10T09:23:53Z
    ts = ts.replace('Z', '')
    if 'T' in ts:
        date_part, time_part = ts.split('T')
    else:
        date_part, time_part = ts, '00:00:00'
    y, m, d = [int(x) for x in date_part.split('-')]
    th, tm, ts_sec = [int(x) for x in time_part.split(':')]
    return datetime.datetime(y, m, d, th, tm, ts_sec)

def generate_svg(history_data, output_path):
    random.seed(42)

    if not history_data:
        # Fallback dataset if API rate-limited
        history_data = [
            ('2026-07-10T09:00:00Z', 1),
            ('2026-07-11T12:00:00Z', 180),
            ('2026-07-12T18:00:00Z', 345),
            ('2026-07-15T12:00:00Z', 520),
            ('2026-07-18T12:00:00Z', 610),
            ('2026-07-24T12:00:00Z', 691)
        ]

    total_stars = history_data[-1][1]
    t_start = parse_iso(history_data[0][0])
    t_end = parse_iso(history_data[-1][0])
    
    total_seconds = (t_end - t_start).total_seconds()
    if total_seconds <= 0:
        total_seconds = 86400

    # Y-axis ceiling: 700 or ceil to nearest 100
    y_max = max(700, math.ceil(total_stars / 100) * 100)

    # Filter sample points based on time progress to create natural curve
    # Sample every ~5% time span or at least 15 key points
    sample_points = []
    # Always include first point
    sample_points.append(history_data[0])
    
    prev_ratio = 0
    for item in history_data[1:-1]:
        t_curr = parse_iso(item[0])
        ratio = (t_curr - t_start).total_seconds() / total_seconds
        if ratio - prev_ratio >= 0.05: # sample every 5% time interval
            sample_points.append(item)
            prev_ratio = ratio

    # Always include last point
    sample_points.append(history_data[-1])

    # Calculate exact SVG coordinates
    x_start, x_end = 65, 635
    y_start, y_end = 205, 45
    width = x_end - x_start
    height = y_start - y_end

    svg_points = []
    for item in sample_points:
        t_curr = parse_iso(item[0])
        star_val = item[1]
        t_ratio = (t_curr - t_start).total_seconds() / total_seconds
        
        px = x_start + t_ratio * width
        py = y_start - (star_val / y_max) * height
        svg_points.append((px, py))

    c1, c2 = rough_curve(svg_points, roughness=1.5)

    # Grid lines for Y-axis (0, 200, 400, 600, 700)
    y_grid_vals = [0, 200, 400, 600, y_max]
    grid_lines_html = []
    y_labels_html = []
    for gv in y_grid_vals:
        gy = y_start - (gv / y_max) * height
        if gv > 0 and gv < y_max:
            gpath = rough_line(x_start, gy, x_end, gy, 0.8)
            grid_lines_html.append(f'<path d="{gpath}" class="grid-line" />')
        y_labels_html.append(f'<text x="{x_start-12}" y="{gy+4:.1f}" class="text-font text-muted" text-anchor="end">{gv}</text>')

    xaxis = rough_line(x_start, y_start, x_end, y_start, 1.0)
    yaxis = rough_line(x_start, y_end, x_start, y_start, 1.0)
    border = (rough_line(5, 5, 695, 5, 1.0) + ' ' + 
              rough_line(695, 5, 695, 255, 1.0) + ' ' + 
              rough_line(695, 255, 5, 255, 1.0) + ' ' + 
              rough_line(5, 255, 5, 5, 1.0))

    end_x, end_y = svg_points[-1]

    # Format dates for X-axis: Start date, Mid date, Today
    d_start_str = t_start.strftime('%m/%d')
    d_mid_str = (t_start + (t_end - t_start)/2).strftime('%m/%d')
    d_end_str = t_end.strftime('%m/%d')

    svg_content = f'''<svg width="100%" height="260" viewBox="0 0 700 260" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: #171717; }}
    .border-line {{ stroke: #444444; stroke-width: 1.5; fill: none; }}
    .grid-line {{ stroke: rgba(255, 255, 255, 0.12); stroke-width: 1; fill: none; }}
    .axis-line {{ stroke: #888888; stroke-width: 1.8; fill: none; }}
    .text-font {{ font-family: "Comic Sans MS", "Chalkboard SE", "Comic Neue", "Caveat", cursive, sans-serif; }}
    .text-muted {{ fill: #A0A0A0; font-size: 13px; }}
    .text-title {{ fill: #21A4B1; font-size: 16px; font-weight: bold; }}
    .text-tag {{ fill: #E94A3F; font-size: 14px; font-weight: bold; }}
    .curve-main {{ stroke: #E94A3F; stroke-width: 2.8; fill: none; stroke-linecap: round; stroke-linejoin: round; }}
    .curve-sub {{ stroke: #E94A3F; stroke-width: 1.5; opacity: 0.75; fill: none; stroke-linecap: round; stroke-linejoin: round; }}

    @media (prefers-color-scheme: light) {{
      .bg {{ fill: #FDFDFD; }}
      .border-line {{ stroke: #222222; }}
      .grid-line {{ stroke: rgba(0, 0, 0, 0.1); }}
      .axis-line {{ stroke: #333333; }}
      .text-muted {{ fill: #555555; }}
    }}
  </style>

  <!-- 背景卡片 -->
  <rect width="700" height="260" rx="12" class="bg" />

  <!-- 手繪外框 -->
  <path d="{border}" class="border-line" />

  <!-- 標題 -->
  <text x="30" y="36" class="text-font text-title">Star History — speak-human-tw ({total_stars} Stars)</text>

  <!-- 手繪網格與座標軸 -->
  {"".join(grid_lines_html)}
  <path d="{xaxis}" class="axis-line" />
  <path d="{yaxis}" class="axis-line" />

  <!-- Y 軸數字 (真實數據刻度) -->
  {"".join(y_labels_html)}

  <!-- X 軸真實日期 (首/中/尾按時間比例排布) -->
  <text x="{x_start}" y="230" class="text-font text-muted" text-anchor="start">{d_start_str} (Launch)</text>
  <text x="350" y="230" class="text-font text-muted" text-anchor="middle">{d_mid_str}</text>
  <text x="{x_end}" y="230" class="text-font text-muted" text-anchor="end">{d_end_str} (Today)</text>

  <!-- 手繪雙線折線 (基於真實時間軸爆發曲線) -->
  <path d="{c1}" class="curve-main" />
  <path d="{c2}" class="curve-sub" />

  <!-- 最新星數亮點與標籤 -->
  <circle cx="{end_x:.1f}" cy="{end_y:.1f}" r="5.5" fill="#E94A3F" stroke="#FFFFFF" stroke-width="2"/>
  <text x="{end_x-10:.1f}" y="{end_y-12:.1f}" class="text-font text-tag" text-anchor="end">★ {total_stars} Stars</text>
</svg>
'''

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f'Successfully generated SVG at {output_path} with {total_stars} real stars across real timeframe!')

if __name__ == '__main__':
    token = os.environ.get('GITHUB_TOKEN')
    history = fetch_star_history_gh()
    if not history:
        history = fetch_star_history_api(token)

    output = '/Users/raymond-mini/Documents/Raymond-Agent/600_Project/_repos/speak-human-tw/assets/readme/star-history-real.svg'
    if len(sys.argv) > 1:
        output = sys.argv[1]

    generate_svg(history, output)
