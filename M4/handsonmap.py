import folium

def create_interactive_map():
    # 1. Set the baseline coordinates (Latitude, Longitude) for the map center
    # Example: Center coordinates over Jammu, India
    center_lat, center_lon = 32.7266, 74.8570
    
    # 2. Create the base hands-on map object
    # zoom_start defines the initial magnification layer (1-20)
    my_map = folium.Map(location=[center_lat, center_lon], zoom_start=13)
    
    # 3. Add custom markers with interactive popup windows
    # Marker 1: General City Marker
    folium.Marker(
        location=[32.7266, 74.8570],
        popup="<b>Jammu City Center</b><br>Welcome to the City of Temples!",
        tooltip="Click for details",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(my_map)
    
    # Marker 2: A secondary point of interest nearby (e.g., Bahu Fort area)
    folium.Marker(
        location=[32.7290, 74.8872],
        popup="<i>Bahu Fort Area</i><br>Historic fortress and gardens.",
        tooltip="Hover tooltip text",
        icon=folium.Icon(color="green", icon="cloud")
    ).add_to(my_map)
    
    # 4. Add a decorative circular zone (e.g., radius boundary ring)
    folium.Circle(
        location=[32.7266, 74.8570],
        radius=1000, # Radius size defined in meters
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.1,
        popup="1 KM Boundary Zone"
    ).add_to(my_map)
    
    # 5. Save the final layout structure as a local HTML webpage
    output_filename = "hands_on_map.html"
    my_map.save(output_filename)
    
    print("=" * 45)
    print(f"🎉 Success! Your interactive map has been created.")
    print(f"👉 Open the file '{output_filename}' in any web browser to explore it!")
    print("=" * 45)

if __name__ == "__main__":
    create_interactive_map()
