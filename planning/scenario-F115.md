---
id: F115
title: Real businesses from Napa Valley to Tahoe are listed as unclaimed Pages, waiting with their markets
status: draft
horizon: considering
rank: 140
date: 2026-10-12
depends: [F103, F104]
---
## Story

A member in Davis searches "cheese" and finds eleven makers across the Sacramento market, each with a photo, a sample post marked Sample, and working links. A potter in Calistoga is already listed, unclaimed, and nobody sees her Page until Napa County opens; that day she is on Explore without lifting a finger. Staff set a vantage in Napa and see the market as it will look, under a banner saying it is a preview.

## Acceptance

**Build plan: no data is loaded until this is approved.**

1. **Source: Overture Maps Places** (release named in the run; CDLA Permissive 2.0, the Foursquare part Apache 2.0 with its NOTICE). No Google, Yelp or OpenStreetMap data in any Page.
2. **Filter**: confidence 0.7 or more, not closed, consumer categories only (food and drink, shops and makers, wine, beer and farms, arts, recreation and outdoors, lodging, personal services); duplicates by name within 50 m dropped [guess]; a row with a brand after every row without one.
3. **Wave 1 fills the Sacramento market to about 1,500 Pages. Wave 2** adds about 1,230 across Napa, St. Helena, Calistoga, Yountville, American Canyon, Truckee, South Lake Tahoe, Lodi, Yuba City, Marysville, Colusa and Williams, capped per town and split by category as the research note's table says. Every cap is a guess in a config file.
4. **Each Page meets the unclaimed rules unchanged** (2026-10-05): the business's own credited photo or the category stock fallback, the Unclaimed tag, sample posts marked Sample, claim and remove; the loader's link check drops dead links. The Overture id and release go to `page_sources`.
5. **A Page in a waiting market is on no surface until its market opens** (F104 criterion 4), and its URL is `noindex` until then.
6. **Staff market preview**: a staff permission lets its holder set a vantage in a waiting market and see it as if open, under the banner "Preview: this market is waiting." Members see F105 criterion 4 unchanged.
7. **Monthly refresh**: Overture's permanently closed hides an unclaimed Page; a claimed Page is untouched.
8. **Truckee joins the Tahoe market**: its county subdivision is one `market_members` row (F103 criterion 1), name checked against TIGER first.
9. **Census Places are loaded** for every wave 2 town, and the feed reads `markets`, before wave 2 is checked by town.
10. **A credits page** names Overture and Foursquare. Copy to the PM.

## Not this

Opening any market. Claiming for owners. Reviews or ratings. Scraping Google or Yelp. Street View photos. Changing the unclaimed rules.

## Why

- **Lives somewhere better?** Partly: map apps list businesses; none sit beside local makers' posts and gatherings.
- **Only locals know?** Partly: listings are public; what owners add after claiming is local.
- **Gets people together?** Yes: there is somewhere to go when a market opens.
- **Stays fresh on its own?** Yes: a monthly refresh; owners take over on claim.
- **Who keeps it current?** The refresh job; owners after claim; removals by the business itself.
- **Better as more people join?** Yes: claimed Pages replace samples with the real thing.

**Path: well-worn** for the data (Overture is built for this; Google's and Yelp's terms bar it). Precedents: Overture Places (https://docs.overturemaps.org/guides/places/), Foursquare OS Places (https://docs.foursquare.com/data-products/docs/access-fsq-os-places), Craigslist's regions opened in batches. **Risk for `socialus-legal`**: own-site photos and sample posts at about 2,700 Pages rather than 111. Research: `planning/research/explore-freshness-and-learning-2026-10-12.md` § 4.

[platform none]
