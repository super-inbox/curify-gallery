# Image generation specification

Mode: built-in `image_gen`, one generated frame per wardrobe variant. This is a reproducible normalized prompt specification, not a verbatim transcript of each tool call. Original selected images are saved in the batch's Gallery `frames/` directory.

## Shared prompt

Single cinematic photorealistic vertical 9:16 full-length head-to-toe portrait. One original adult woman aged 28 with chestnut brown hair, warm fair skin, refined oval face and hazel eyes. Relaxed natural arms and anatomically plausible hands. Dark warm olive seamless studio, painterly soft key light, realistic skin and detailed textiles. Neutral or slightly three-quarter stance, calm expression. Keep identity, body, camera framing, light and background consistent. Whole garment visible. No text, labels, logos, watermarks, collage, props or additional people. Original historical-style interpretation, not a replica of a named designer or a museum object.

The base frame is `fashion-1900.png`. Every other generation references that image and changes outfit/hairstyle while requesting identity and framing preservation. Generated hairstyle continuity sometimes favors the shared pinned-up style over the requested period variation; garments and silhouette are the film's main focus, not an authoritative hairstyle study.

| Frame | Wardrobe direction |
|---|---|
| fashion-1900 | Early-1900s British/French affluent daywear; cream high-neck lace blouse, restrained full sleeves, fitted waist, long burgundy gored skirt, brooch, pinned Edwardian-inspired hair. |
| fashion-1925 | Mid-1920s Paris-inspired teal straight tubular dress, dropped waist, restrained silver geometric beading, midcalf length, T-strap shoes; request waved bob. |
| fashion-1950 | Cobalt short-sleeved fitted-waist day dress, full midcalf petticoat-supported skirt, plain pumps, soft waves. |
| fashion-1975 | Caramel suede fitted jacket, cream pointed-collar blouse, high-waisted flared trousers, platforms, long chestnut hair. |
| fashion-2000 | Short charcoal blazer, opaque ivory camisole, indigo bootcut jeans, narrow belt, pointed ankle boots, shoulder-length hair. |
| gowns-1550 | Italian Renaissance-inspired garnet velvet, square neckline with white chemise edge, fitted bodice, gold brocade sleeves, long skirt, delicate chain; no fantasy crown. |
| gowns-1750 | French Rococo-inspired dusty-rose silk brocade, sideways pannier volume, stomacher, open overskirt/petticoat, elbow lace sleeves; no towering late-century hairstyle. |
| gowns-1810 | British/French Empire-inspired ivory silk, restrained gold embroidery, high waist under bust, puff sleeves, long narrow draped skirt, flat satin shoes. |
| gowns-1860 | French/British emerald taffeta ballgown, fitted natural waist, bell-shaped crinoline skirt, off-shoulder short sleeves and lace trim; no later bustle. |
| gowns-1950 | Midnight-navy satin evening gown, fitted waist, bateau neckline, cap sleeves, sculptural full floor-length skirt, restrained earrings. |
| bridal-1920 | British white bridal inspiration, ivory crepe, dropped waist, pearl-like geometric beading, calf-length skirt, Juliet cap and long veil; no bouquet. |
| bridal-1950 | Ivory fitted-waist satin, full tea-length skirt, modest lace bateau neckline, elbow sleeves, short veil and plain headpiece. |
| bridal-1980 | Ivory taffeta, voluminous puff sleeves, high lace collar, fitted waist, full skirt and veil; no exact royal-gown copy or tiara. |
| bridal-2000 | Ivory satin, modest straight-across strapless neckline, princess seams, A-line floor-length skirt, small bead detailing, plain long veil. |
| bridal-2020 | Minimal opaque ivory crepe, long sleeves, bateau neckline, clean waist, softly straight skirt, short train and plain veil; no celebrity/designer replica. |

Motion prompt, verbatim, is recorded per task in `motion-jobs.json`: restrained shoulder turn, breathing, blink and fabric movement; preserve face, clothes and framing, no transformation, extra accessories or text.
