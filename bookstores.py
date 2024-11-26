import json

# 讀取 JSON 檔案
with open("emapOpenDataAction.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 準備 GeoJSON 格式
geojson = {
    "type": "FeatureCollection",
    "features": []
}

for item in data:
    # 確保經緯度存在且有效
    if item.get("longitude") and item.get("latitude"):
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(item["longitude"]), float(item["latitude"])]
            },
            "properties": {
                "name": item.get("name", ""),
                "address": item.get("address", ""),
                "intro": item.get("intro", ""),
                "cityName": item.get("cityName", ""),
                "phone": item.get("phone", ""),
                "email": item.get("email", ""),
            }
        }
        geojson["features"].append(feature)

# 儲存為 GeoJSON 檔案
with open("output.geojson", "w", encoding="utf-8") as file:
    json.dump(geojson, file, ensure_ascii=False, indent=2)

print("GeoJSON 轉換完成！檔案已存為 output.geojson")

