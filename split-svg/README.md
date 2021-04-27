# Split SVG

Uses Inkscape to generate single tiles from a grid.

The Grid needs to be on a layer named "Grid" and consists of rectangles (use no
stroke and solid background for precise width and height and easy handling).

Give each grid rectangle you want to get exported an ID that is used for the
file name. Default IDs starting with "rect" are skipped.

See [example.svg](example.svg) for a template with a single 'test' tile.

Now create your tiles in other layers as you like. Hide the grid layer before
saving, so that it won't be visible in the resulting tiles.

Finally you can export the single tiles using

```
split-svg SVG_FILE_NAME
```

The resulting tiles are exported as png-files in the current directory.
