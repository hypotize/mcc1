import tkinter as tk
import requests

def get_poke(id):
  data=dict()
  # PokeApiにリクエスト、レスポンスをjson形式で受け取る
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
  pokeapi = response.json()

  # 各種データをレスポンスから取得
  data["weight"] = float(pokeapi["weight"]) / 10
  data["height"] = float(pokeapi["height"]) / 10
  data["img_url"] = pokeapi["sprites"]["other"]["official-artwork"]["front_default"]

  species_url = pokeapi["species"]["url"]
  response = requests.get(species_url)
  pokeapi_species = response.json()

  # 日本語の名前取得
  names = pokeapi_species["names"]
  for name in names:
      if name["language"]["name"] == "ja":
          data['ja_name'] = name["name"]
          break

  # 日本語のフレーバーテキスト取得
  flavor_text_entries = pokeapi_species["flavor_text_entries"]
  for text in flavor_text_entries:
      if text["language"]["name"] == "ja":
          data['flavor_text'] = text["flavor_text"]
          break
  return data

def btn_click():
  global tk_image # 画像が消失しないようにglobalにする
  id=int(t_entry.get())
  data=get_poke(id)

  #画像をバイナリデータとして取得
  bin=requests.get(data["img_url"]).content
  tk_image=tk.PhotoImage(data=bin)
  
  canvas.delete('pic')
  canvas.create_image(0,0,anchor='nw',image=tk_image,tag='pic')
  result_text.delete("1.0",tk.END)
  result_text.insert("1.0",data['ja_name']+'\n\n')
  result_text.insert("3.0",f'身長:{data["height"]}m,体重:{data["weight"]}kg\n\n')
  result_text.insert("5.0",data['flavor_text']+'\n')

root=tk.Tk()
t_label=tk.Label(text='図鑑番号:')
t_label.pack()
t_entry=tk.Entry(width=10)
t_entry.pack()
t_button =tk.Button(text='検索',command=btn_click)
t_button.pack()
canvas=tk.Canvas(width=475,height=475)
canvas.pack()
result_text=tk.Text(width=50,padx=20,pady=20,font=('Arial',12))
result_text.pack()

root.mainloop()
