from pathlib import Path

import gradio as gr
import modules.shared as shared
import modules.ui as ui_module

from modules.html_generator import get_image_cache

selected_characters = []

def get_available_characters():
    # Remove the normal selected character from list here...
    return sorted(set(map(lambda x : '.'.join(str(x.name).split('.')[:-1]), Path('characters').glob('*.json'))), key=str.lower)

def select_character(characters):
    global selected_characters
    selected_characters = characters

def ui():
    global selected_characters

    with gr.Accordion("Multi-Chat", open=True):
        gr.Markdown(f"{selected_characters}")
        character_options = gr.Dropdown(choices=get_available_characters(), value=selected_characters, label="Additional Characters", multiselect=True)
        character_options.change(select_character, character_options, [])

        refresh = gr.Button("Refresh")
        refresh.click(lambda: character_options.update(choices=get_available_characters()), [], character_options)
