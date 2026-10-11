# The three rings in four other places (2026-10-11)

Stress test of `product/systems/places.md` § The three rings, asked for by the PM. Two dense, two sparse. Facts about places are general knowledge [A] unless marked; verify against Census TIGER before seeding anything.

## Williamsburg, Brooklyn (dense, car-free)
- **Breaks first:** the town ring. New York city is one Census Place of 8.3 million across five counties. "Town = Census Place" gives every New Yorker the same home community, which is useless for money and for order.
- **Fix:** for a Place above a population threshold (say 250k [A]) or spanning counties, the town ring is the city's own official neighbourhood layer: NYC's Neighborhood Tabulation Areas or community districts (NYC Open Data, free). Chicago's 77 community areas, LA's neighbourhood councils, Houston's super neighbourhoods and Philadelphia's planning districts are the same kind of layer. Platform-curated, as places already are.
- **Rings:** hood none (sub-neighbourhoods unlisted); town Williamsburg; area New York City (the market: five boroughs, and Hudson County NJ if its subdivisions are added). Order by adjacency: Greenpoint, Bushwick, Bedford-Stuyvesant first; Lower East Side needs a **curated bridge edge** because polygons do not touch across the East River; Staten Island is ten-plus hops away, which is honest. A car-free member's feed fills from two hops and never widens.
- **Money:** a Williamsburg bakery's give-back goes to a Williamsburg fund, pending until one organises. More honest than "New York City".
- **Gate:** 50 makers and 250 finders for 8.3 million people opens an empty-feeling city. Thresholds must scale with population; the per-market tunable exists, the default should be a share with a floor, set from Sacramento's data.

## The Mission, San Francisco (dense, metro region)
- **Breaks first:** the area. San Francisco is one consolidated city-county; Oakland is across the bay, Daly City touches it. One market for the whole Bay Area is nine counties and 7.7 million people; one market per city is dozens of markets that each feel small.
- **Fix:** Craigslist's division has held for 25 years: one Bay Area with sub-areas (city, east bay, peninsula, north bay, south bay, Santa Cruz). Each sub-area is an area here, built from county subdivisions; the whole bay is the labelled wider section.
- **Rings:** hood none; town the Mission (DataSF analysis neighbourhoods, 41 of them, free); area San Francisco (the city plus northern San Mateo subdivisions if added). Order: Bernal Heights, Noe Valley, SoMa, the Castro; Oakland appears only in the wider section or by vantage.
- **Money:** the Mission's fund. **Gate:** scales as above.

## Alturas, Modoc County (sparse, car-dependent)
- **Breaks first:** the gate and the area. Modoc County has 8,700 people over 4,200 square miles; 250 finders is 3% of everyone. People drive to Klamath Falls, Oregon, or two and a half hours to Redding.
- **Fix:** the area is several counties: Modoc, Lassen, eastern Siskiyou subdivisions, with Klamath Falls in the wider section if the state-line question allows. The gate scales down with population, floored at 10 live Pages (the existing aggregate floor).
- **Rings:** hood none; town Alturas (city, 2,700) or the Modoc County remainder for ranch families; area Northeast California. Order: Canby, Cedarville, Likely; then Adin, Davis Creek, Tulelake; then Susanville. The floor of 10 widens to the whole area almost at once, then stops; online and shippable makers matter more here than anywhere.
- **Money:** Alturas fund; "Modoc County, unincorporated" fund for the remainder. Both pending for a long time; the ledger still attributes.

## Markleeville, Alpine County (sparse, cross-state, no town)
- **Breaks first:** everything but the model. Alpine County has 1,200 people, no incorporated city, a few CDPs (Markleeville, Bear Valley, Mesa Vista), and its shops, schools and doctors are in South Lake Tahoe and in Gardnerville and Minden, Nevada.
- **Fix:** none needed beyond what Tahoe already needs. Alpine's subdivisions join the Tahoe area with one row each; the area opens as a whole, so Alpine never has to clear a gate alone.
- **Rings:** hood none; town Markleeville CDP or the Alpine remainder; area Tahoe. Order: Woodfords, South Lake Tahoe, Gardnerville (if the Nevada shore is in the area), Kirkwood.
- **Money:** Markleeville or the Alpine remainder, per state; a Carson Valley fund never receives Alpine money unless the state-line question's answer C is chosen.

## What the four say together
1. **Town = Census Place needs two exceptions, both already in the model's spirit:** official city neighbourhood layers for very large Places; county remainders for the unincorporated. Both are platform-curated, free, and published by a government.
2. **Adjacency needs a few curated bridge edges** where water or a freeway separates neighbours that cross daily (East River, the Bay, the American River at Folsom). One-time human edits, like Nextdoor's boundary fixes.
3. **Market gates scale with population.** A share with a floor of 10 Pages; the per-market tunable exists; Sacramento's data sets the share.
4. **The state-line question is the normal rural case, not a Tahoe curiosity:** Klamath Falls, Carson Valley, Reno for Truckee, and across the country Fargo-Moorhead, Kansas City, Texarkana. Answer A in F103 (discovery crosses, money does not) holds up in all four.
5. **The money unit held everywhere:** Williamsburg, the Mission, Alturas, Markleeville. Funds form where people organise; pending elsewhere; nothing pooled.
6. **Dense places never widen; sparse places widen at once and stop at the area.** The same rule, no density band, produces both, because the floor of 10 does the work. Density bands stay later, if ever.
