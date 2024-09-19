products=[
    ["laptop","mouse","keyboard"],
    ["monitor","printer"],
    "Sony XYZ",
    "Beats Fit Pro",
    "Apple Magic Keyboard",
    "Logitech MX Master 3",
    12,
    33,
    34,
]

def print_items(items):
    for item in items:
        if not type(item)==list:
            print(item)
  
print_items(products)