# import os, re

# # Remove Gym Food breadcrumb link
# gym_food_pattern = re.compile(
#     r'<a href="[^"]*gym-food[^"]*"[^>]*>\s*Gym Food\s*</a>\s*',
#     re.DOTALL
# )

# # Remove Gym Food from JSON-LD schema
# schema_pattern = re.compile(
#     r',?\{"@type":"ListItem","position":2,"item":\{"name":"Gym Food","@id":"[^"]*"\}\}',
#     re.DOTALL
# )

# count = 0
# for dirpath, dirnames, filenames in os.walk('.'):
#     dirnames[:] = [d for d in dirnames if d != '.git']
#     for fname in filenames:
#         if fname.endswith('.html'):
#             fpath = os.path.join(dirpath, fname)
#             c = open(fpath, 'r', encoding='utf-8', errors='ignore').read()
#             n = gym_food_pattern.sub('', c)
#             n = schema_pattern.sub('', n)
#             if n != c:
#                 open(fpath, 'w', encoding='utf-8').write(n)
#                 count += 1

# print(f'Fixed {count} files!')







import os, re

menu_tab = re.compile(
    r'\s*<li class="mobile-tab-title mobile-pages-title[^"]*"[^>]*>.*?</li>',
    re.DOTALL
)
pages_menu = re.compile(
    r'<ul id="menu-mobile-navigation"[^>]*class="mobile-pages-menu[^"]*"[^>]*>.*?</ul>',
    re.DOTALL
)

count = 0
for dirpath, dirnames, filenames in os.walk('.'):
    dirnames[:] = [d for d in dirnames if d != '.git']
    for fname in filenames:
        if fname.endswith('.html'):
            fpath = os.path.join(dirpath, fname)
            c = open(fpath, 'r', encoding='utf-8', errors='ignore').read()
            n = menu_tab.sub('', c)
            n = pages_menu.sub('', n)
            if n != c:
                open(fpath, 'w', encoding='utf-8').write(n)
                count += 1

print(f'Fixed {count} files!')