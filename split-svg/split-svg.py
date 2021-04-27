#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import click
import subprocess

ns = {
        "": "http://www.w3.org/2000/svg",
        "dc": "http://purl.org/dc/elements/1.1/",
        "cc": "http://creativecommons.org/ns#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "svg": "http://www.w3.org/2000/svg",
        "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
        "inkscape": "http://www.inkscape.org/namespaces/inkscape",
        }


@click.command()
@click.argument('svgfile')
def split(svgfile):
    click.echo(f"Splitting file: {svgfile}", err=True)
    tree = ET.parse(svgfile)
    root = tree.getroot()
    grid = root.find(".//g[@inkscape:label='Grid']", ns)
    if not grid:
        click.echo("No layer named 'Grid' found.", err=True)
        return
    if grid.get("style") != "display:none":
        click.echo("WARNING: Grid layer is visible!", err=True)
    skipped = 0
    for rect in grid.findall("rect", ns):
        if rect.get("id").startswith("rect"):
            skipped += 1
            continue
        svg_id = rect.get("id")
        outfile = f"{svg_id}.png"
        click.echo(outfile)
        subprocess.run(
                ["inkscape", svgfile, "-o", outfile, "-i", svg_id],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                ) 
    click.echo(f"Skipped {skipped} rectangles with id 'rect...'", err=True)


if __name__ == '__main__':
    split()

