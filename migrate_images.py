import json
import base64
import os
import time

def migrate():
    json_path = 'projects.json'
    assets_dir = 'assets/images'
    
    # Ensure assets dir exists
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
        print(f"Created directory: {assets_dir}")

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            projects = json.load(f)
        
        updated = False
        
        for p in projects:
            img_data = p.get('image', '')
            
            if img_data.startswith('data:image'):
                print(f"Migrating image for project: {p.get('title', 'Unknown')}")
                
                # Extract extension
                header, encoded = img_data.split(',', 1)
                ext = 'jpg' 
                if 'png' in header: ext = 'png'
                elif 'jpeg' in header: ext = 'jpg'
                elif 'webp' in header: ext = 'webp'
                
                # Create filename
                filename = f"{p['id']}-{int(time.time())}.{ext}"
                file_path = os.path.join(assets_dir, filename)
                
                # Save file
                with open(file_path, 'wb') as img_f:
                    img_f.write(base64.b64decode(encoded))
                
                # Update JSON path (use forward slashes for web)
                p['image'] = f"assets/images/{filename}"
                updated = True
                print(f"Saved to: {p['image']}")

        # ALSO check within 'details' and 'details_en' for markdown images
        import re
        # Pattern for markdown image: ![alt](data:image/png;base64,...)
        # We capture: 1=alt, 2=mime, 3=base64
        pattern = re.compile(r'!\[(.*?)\]\(data:image/(.*?);base64,(.*?)\)')

        for key in ['details', 'details_en']:
            content = p.get(key, '')
            if not content: continue
            
            def replace_match(match):
                nonlocal updated
                alt_text = match.group(1)
                ext = match.group(2)
                if ext == 'jpeg': ext = 'jpg'
                b64_data = match.group(3)
                
                # Unique filename
                # Use a counter or specific ID to avoid collision if multiple images
                timestamp = int(time.time() * 1000) 
                
                # simple hash of data to avoid duplicates/collisions if needed, 
                # but timestamp + random suffix is usually enough. 
                # Let's use project id + key + partial timestamp
                filename = f"md-{p['id']}-{key[:3]}-{timestamp}.{ext}"
                file_path = os.path.join(assets_dir, filename)
                
                try:
                    with open(file_path, 'wb') as img_f:
                        img_f.write(base64.b64decode(b64_data))
                    print(f"Migrated markdown image: {filename}")
                    updated = True
                    return f"![{alt_text}](assets/images/{filename})"
                except Exception as e:
                    print(f"Failed to save markdown image: {e}")
                    return match.group(0) # return original if fail

            new_content = pattern.sub(replace_match, content)
            if new_content != content:
                p[key] = new_content

                
        if updated:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(projects, f, indent=4, ensure_ascii=False)
            print("Successfully migrated images! projects.json updated.")
        else:
            print("No base64 images found to migrate.")
            
    except Exception as e:
        print(f"Error during migration: {e}")

if __name__ == "__main__":
    migrate()
