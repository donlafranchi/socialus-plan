# Map markers: pins for addresses, discs for areas (2026-10-07)

PM ruled option A and added: "make sure it looks different than the rest", with the classic teardrop pin for exact addresses. Decision line: `DECISIONS.md` 2026-10-07. Issue: `socialus-web` #475. Path: new territory (brought as A/B/C).

## Rule
- **Exact public address:** teardrop pin (round head tapering to a point), navy; gold when selected.
- **Area only (metro, city, neighbourhood):** soft translucent disc with the item count inside; no point, no tail, no edge ring like a pin's.
- **Same centroid:** items group into one disc; tapping opens a list. **Same address:** pins spread apart.
- **Distinct from everything else on the map:** clusters stay solid circles with a count (a different fill and an opaque edge), and any boundary outline is a line, never a filled disc.

## Why
The map is for "is anything going on around me" (run clubs, social events), not precise location. A point marker on an area-only place implies a front door that is not public.

## Precedents
- [Airbnb](https://www.airbnb.com): listings show an approximate-location circle until booking, not a pin.
- [Google Maps](https://maps.google.com): the teardrop is the exact-place marker.
- [Zillow](https://www.zillow.com): neighbourhoods are areas, homes are points.

## Options
- **A. Translucent disc with count (chosen).** Simplest, works at every grain, cannot read as a point.
- **B. Shaded boundary outline with count.** Most honest about extent, but heavier, and boundaries are loaded only for Sacramento.
- **C. Name chip ("Midtown · 4").** Readable, but no shape on the map to tell area from address at a glance.

## Trade-off
A discs hide the true extent of an area (B would show it) and rely on the count and the tap-to-list to say what is there. Accepted: for beta one metro, simplicity and not implying an address outweigh drawing extents.
