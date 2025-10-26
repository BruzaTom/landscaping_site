import os

folder = "static/images/landscaping"
max_images = 6
def gen_head():
    nav = '<nav class="navbar"><ul class="link-list"><li><a href="contact.html" class="abbreviate">Contact</a></li><li><a href="index.html">Home</a></li><li><a href="payments.html">Payments</a></li></ul></nav>'
    head = f'<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title> Gallery </title><link href="static/index.css" rel="stylesheet"></head><body><article><div><h1>Gallery</h1>{nav}<div class="pagination">'
    for i in range(len(os.listdir(folder))//max_images):
        head += f'<a href="gallery{i}.html">{i}</a>'
    head += '</div><div class="gallery">'
    return head
tail = '</div></div></article></body></html>' 

page = 0
count = 0
for filename in os.listdir(folder):
    if count == max_images:
        html += tail
        with open(f"gallery{page}.html", "w") as f:
            f.write(html)
        page += 1
        count = 0
    if count == 0:
        html = gen_head() 
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        html += f'  <img src="{folder}/{filename}" alt="{filename}">\n'
    count += 1




