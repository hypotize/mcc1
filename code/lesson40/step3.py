import folium

# 地図の作成
map = folium.Map(location=[35.16817344893199, 139.64131772580964], zoom_start=14)

# マーカーの位置とポップアップのテキストのリスト
locations = [
    {"coords": [35.18633611331341, 139.65328306022533], "popup": "インド料理うみのかみさまサイサガール"},
    {"coords": [35.17777652195682, 139.63299483125246], "popup": "三崎口駅"},
    {"coords": [35.144393289687386, 139.62078541581485], "popup": "三浦市役所"}
]

# マーカーの追加
for location in locations:
    popup = folium.Popup(location["popup"], max_width=200)
    folium.Marker(location["coords"], popup=popup).add_to(map)

# 地図の保存
map.save("ちず.html")
