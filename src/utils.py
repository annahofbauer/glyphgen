import math

def luminance(rgb):
    """
     Berechnet die wahrgenommene Helligkeit eines RGB-Pixels 
    basierend auf der gewichteten Luminanzformel nach ITU-R BT.601.

    Args:
        rgb (tuple[int, int, int]): Ein RGB-Tupel mit Werten von 0–255 
                                    für (rot, grün, blau).

    Returns:
        float: Die Helligkeit (Luminanz) als Gleitkommazahl.
        """
    r, g, b = rgb
    return 0.299 * r + 0.587 * g + 0.114 * b

def clustersize(glyph_size, height, width):
    """
    Berechnet die Größe eines Clusters (Zelle), sodass das Bild vollständig 
    und ohne Ränder in gleich große Blöcke aufgeteilt werden kann. 
    Jeder Block ist mindestens so groß wie `glyph_size`, 
    und die Clustergröße ist ein echter Teiler von Bildhöhe/-breite.

    Args:
        glyph_size: Größe der Glyphen in Pixel
        height (int): Höhe des Bildes in Pixel
        width (int): Breite des Bildes in Pixel 
        
    Returns:
        tuple[float, float]: Höhe und Breite eines Clusters in Pixeln 
                             (cluster_height, cluster_width)."""
    
    cluster_y = math.floor(height / glyph_size)
    cluster_x = math.floor(width / glyph_size)

    cluster_height = height / cluster_y
    cluster_width  = width / cluster_x
    return cluster_y, cluster_x, cluster_height, cluster_width