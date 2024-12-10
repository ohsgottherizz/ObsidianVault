import os
import re
from pathlib import Path


def find_markdown_links(content):
    # Find [[wiki-style]] and [markdown-style](links)
    wiki_links = re.findall(r'\[\[(.*?)\]\]', content)
    markdown_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    return wiki_links + [link[0] for link in markdown_links]


def generate_mermaid():
    vault_path = '.'
    nodes = set()
    connections = set()

    for file in Path(vault_path).rglob('*.md'):
        if '.obsidian' in str(file):
            continue

        filename = str(file.stem)
        nodes.add(filename)

        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            links = find_markdown_links(content)
            for link in links:
                connections.add((filename, link.split('|')[0].strip()))

    # Generate Mermaid diagram
    mermaid = ["graph TD"]
    for node in nodes:
        node_id = f"node_{len(mermaid)}"
        mermaid.append(f'    {node_id}["{node}"]')

    for source, target in connections:
        source_id = f"node_{list(nodes).index(source) + 1}"
        target_id = f"node_{list(nodes).index(target) + 1}"
        mermaid.append(f"    {source_id} --> {target_id}")

    return "\n".join(mermaid)


def update_graph_file():
    mermaid_content = generate_mermaid()
    with open('graph.md', 'w') as f:
        f.write("```mermaid\n")
        f.write(mermaid_content)
        f.write("\n```")


if __name__ == "__main__":
    update_graph_file()
