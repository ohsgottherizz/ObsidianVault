import os
import re
from pathlib import Path


def find_markdown_links(content):
    # Improved regex for Obsidian-style links
    wiki_links = re.findall(r'\[\[(.*?)(?:\|.*?)?\]\]', content)
    return wiki_links


def generate_mermaid():
    vault_path = '.'
    connections = []
    nodes = set()

    # First pass: collect all files
    for file in Path(vault_path).rglob('*.md'):
        if '.obsidian' in str(file) or 'graph.md' in str(file):
            continue

        current_file = file.stem
        nodes.add(current_file)

        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            links = find_markdown_links(content)

            for link in links:
                link = link.split('|')[0].strip()
                connections.append((current_file, link))
                nodes.add(link)

    # Generate Mermaid diagram
    mermaid = ["```mermaid", "graph TD"]

    # Add nodes with cleaned names
    node_map = {}
    for i, node in enumerate(nodes):
        clean_id = f"id{i}"
        node_map[node] = clean_id
        mermaid.append(f'    {clean_id}["{node}"]')

    # Add connections
    for source, target in connections:
        if source in node_map and target in node_map:
            mermaid.append(f"    {node_map[source]} --> {node_map[target]}")

    mermaid.append("```")
    return "\n".join(mermaid)


def update_graph_file():
    with open('graph.md', 'w', encoding='utf-8') as f:
        f.write(generate_mermaid())


if __name__ == "__main__":
    update_graph_file()
