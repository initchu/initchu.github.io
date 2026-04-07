import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def generate_image_sitemap(image_dir, site_url, output_file):
    # Standard XML namespace for Image Sitemaps
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    urlset.set("xmlns:image", "http://www.google.com/schemas/sitemap-image/1.1")

    # Add the main site page or subpages that contain these images
    # For simplicity, we link all images to the base URL or their specific pages
    # Here we assume images in docs/images are general assets
    
    # Let's list some key pages that use images
    pages = {
        "/": ["proc2.webp"],
        "/about/me/": ["proc1.webp"]
    }

    for page_path, images in pages.items():
        url_node = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_node, "loc")
        loc.text = f"{site_url.rstrip('/')}{page_path}"

        for img in images:
            img_node = ET.SubElement(url_node, "image:image")
            img_loc = ET.SubElement(img_node, "image:loc")
            img_loc.text = f"{site_url.rstrip('/')}/images/{img}"
            
            # Add titles based on filename
            img_title = ET.SubElement(img_node, "image:title")
            img_title.text = "Initchu Site Asset - " + img.split('.')[0]

    # Pretty print the XML
    xml_str = ET.tostring(urlset, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="  ")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(pretty_xml)
    print(f"Image Sitemap generated at {output_file}")

if __name__ == "__main__":
    SITE_URL = "https://www.chucz.asia"
    IMAGE_DIR = "docs/images"
    OUTPUT = "docs/image_sitemap.xml"
    generate_image_sitemap(IMAGE_DIR, SITE_URL, OUTPUT)
