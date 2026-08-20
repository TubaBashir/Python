import pycountry

def get_country_code(country_name):
    try:
        # Search for the country by name (handles fuzzy matches like 'USA' or 'United States')
        country = pycountry.countries.search_fuzzy(country_name)[0]
        
        return {
            "country_name": country.name,
            "alpha_2": country.alpha_2,  # e.g., 'IN'
            "alpha_3": country.alpha_3,  # e.g., 'IND'
            "numeric": country.numeric   # e.g., '356'
        }
    except LookupError:
        return f"Error: Country '{country_name}' not found."

# Test layout
print(get_country_code("India"))
print(get_country_code("United States"))
