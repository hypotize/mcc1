import folium

map = folium.Map(location=[35.16817344893199, 139.64131772580964],
                 zoom_start=16)

popup = folium.Popup("インド料理うみのかみさまサイサガール", max_width=200)
folium.Marker([35.18633611331341, 139.65328306022533], popup=popup).add_to(map)

map.save("ちず.html")
