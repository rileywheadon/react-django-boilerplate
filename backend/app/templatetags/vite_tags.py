import json
import os
from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def vite_asset(path):
    """
    Load the correct asset path from Vite's manifest.json
    """
    try:
        manifest_path = os.path.join(settings.BASE_DIR, 'static', '.vite', 'manifest.json')
        
        if not os.path.exists(manifest_path):
            # Fallback if manifest doesn't exist
            return static(path)
            
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
            
        # Get the entry for the requested file
        if path in manifest:
            file_path = manifest[path]['file']
            return static(file_path)
        else:
            # Fallback to the original path
            return static(path)
            
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        # Fallback if anything goes wrong
        return static(path)

from django.utils.safestring import mark_safe

@register.simple_tag
def vite_css(entry='src/main.jsx'):
    """
    Get CSS files for a Vite entry point
    """
    try:
        manifest_path = os.path.join(settings.BASE_DIR, 'static', '.vite', 'manifest.json')
        
        if not os.path.exists(manifest_path):
            return mark_safe('')
            
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
            
        if entry in manifest and 'css' in manifest[entry]:
            css_files = manifest[entry]['css']
            css_tags = []
            for css_file in css_files:
                css_tags.append(f'<link rel="stylesheet" href="{static(css_file)}">')
            return mark_safe('\n'.join(css_tags))
            
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        pass
        
    return mark_safe('')