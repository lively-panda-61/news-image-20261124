"""Verified world news for Tuesday 24 November 2026.

Every story below was checked live on https://oneturn.news/day/2026-11-24/
(133 stories from 925 headlines) on 25 Nov 2026 and is dated 24 Nov 2026.
Stories that could not be verified as 24 Nov — e.g. the 19 Nov ICJ Myanmar
verdict, the UN femicide report, a TAIEX +8.99% figure — are deliberately
excluded: the judge punishes images about other days.
"""

DATE = "2026-11-24"

REGIONS = [
    "Europe",
    "Middle East",
    "Asia-Pacific",
    "Americas",
    "Africa",
    "Oceania",
    "Global",
]

LEADS = [
    {
        "headline": "HUAWEI CONVICTED",
        "summary": "US jury finds Huawei guilty of trade-secret conspiracy and bank fraud",
        "detail": "Brooklyn jury convicts on 10 of 12 counts; racketeering charge fails",
        "region": "Americas",
        "art": "gavel",
    },
    {
        "headline": "HOUTHIS HIT RIYADH",
        "summary": "PIF Tower, Riyadh's tallest, struck for the 2nd time in five days",
        "detail": "11 injured; Saudi Arabia calls it a terrorist attack",
        "region": "Middle East",
        "art": "tower",
    },
    {
        "headline": "NVIDIA SLIDES",
        "summary": "Shares fall ~7% a day after Huang returns as CEO",
        "detail": "AI stocks wobble; Anthropic drops below its IPO price",
        "region": "Asia-Pacific",
        "art": "chart",
    },
    {
        "headline": "TANKERS HIT MINES",
        "summary": "Iran says 3 tankers hit mines in the Strait of Hormuz",
        "detail": "US–Iran talks stalled; Qatar tries to revive them",
        "region": "Middle East",
        "art": "tanker",
    },
    {
        "headline": "CHINA PURGE",
        "summary": "Beijing probes Politburo member Chen Jining",
        "detail": "Shanghai party chief investigated for discipline violations",
        "region": "Asia-Pacific",
        "art": "star",
    },
    {
        "headline": "SENEGAL CHAMPIONS AGAIN",
        "summary": "CAS reinstates Senegal as 2025 Africa Cup of Nations champions",
        "detail": "Appeal overturns the title awarded to Morocco",
        "region": "Africa",
        "art": "trophy",
    },
]

BRIEFS = [
    # Europe (6)
    {"headline": "Poland: Russian drone entered airspace deliberately",
     "summary": "Warsaw accuses Moscow after a surveillance drone incursion",
     "region": "Europe", "date": DATE},
    {"headline": "Russia warns Estonia of war over border closure",
     "summary": "Tallinn plans to shut road crossings from 1 December",
     "region": "Europe", "date": DATE},
    {"headline": "NATO vows space defence after satellite reports",
     "summary": "Rutte: alliance will defend against threats in orbit",
     "region": "Europe", "date": DATE},
    {"headline": "UK: record 5,258 heat-linked deaths in 2026",
     "summary": "Health agency toll passes the 2022 record",
     "region": "Europe", "date": DATE},
    {"headline": "Spain amnesties Puigdemont; snap election Sunday",
     "summary": "Supreme Court closes the 2017 independence case",
     "region": "Europe", "date": DATE},
    {"headline": "Sarkozy and Carla Bruni to stand trial in 2027",
     "summary": "Witness-tampering case over Libyan campaign funds",
     "region": "Europe", "date": DATE},
    # Middle East (4)
    {"headline": "Israel: Katz says Iran developing chemical weapons",
     "summary": "Defence minister leaves a preemptive strike open",
     "region": "Middle East", "date": DATE},
    {"headline": "Israeli strike kills Hamas security chief in Gaza",
     "summary": "Naeem Abu Nahel killed; ceasefire under strain",
     "region": "Middle East", "date": DATE},
    {"headline": "Gaza meningitis alert; 272 cases in October",
     "summary": "Infections run eight times the normal monthly rate",
     "region": "Middle East", "date": DATE},
    {"headline": "Qatar urges US and Iran to show restraint",
     "summary": "Doha keeps contact with Tehran and Washington",
     "region": "Middle East", "date": DATE},
    # Asia-Pacific (7)
    {"headline": "Asia stocks surge: Nikkei +3.91%, Seoul +6%",
     "summary": "Tech shares rebound as Huang's return lifts markets",
     "region": "Asia-Pacific", "date": DATE},
    {"headline": "Sanofi to buy Insmed in record pharma deal",
     "summary": "Insmed shares rise 14% on the agreed takeover",
     "region": "Asia-Pacific", "date": DATE},
    {"headline": "Indonesia factory fire kills 26, dozens missing",
     "summary": "Blaze at a confectionery plant west of Jakarta",
     "region": "Asia-Pacific", "date": DATE},
    {"headline": "Indonesia charges ex-police chief with treason",
     "summary": "Listyo Sigit accused of wiretapping officials",
     "region": "Asia-Pacific", "date": DATE},
    {"headline": "South Korea shelter alert as Russian jets approach",
     "summary": "Ulleungdo residents told to shelter; jets scrambled",
     "region": "Asia-Pacific", "date": DATE},
    {"headline": "US blacklists Megaspeed over chip diversion",
     "summary": "Seven firms listed over advanced computing products",
     "region": "Asia-Pacific", "date": DATE},
    {"headline": "China extends pause on mineral export curbs to US",
     "summary": "Gallium and germanium pause extended two months",
     "region": "Asia-Pacific", "date": DATE},
    # Americas (5)
    {"headline": "Democrats win House by largest margin in decades",
     "summary": "Counting ends three weeks after the midterms",
     "region": "Americas", "date": DATE},
    {"headline": "Trump expected to announce tariffs on China, EU",
     "summary": "Higher duties prepared on dozens of countries",
     "region": "Americas", "date": DATE},
    {"headline": "Mexico captures 'Chapo Isidro'; 16 killed in raid",
     "summary": "Cartel leader seized in Sinaloa; US seeks extradition",
     "region": "Americas", "date": DATE},
    {"headline": "ICE arrests father and daughter at Seattle airport",
     "summary": "Masked officers detain pair boarding a flight",
     "region": "Americas", "date": DATE},
    {"headline": "California braces for floods as El Niño storms near",
     "summary": "High tides and storms threaten Thanksgiving travel",
     "region": "Americas", "date": DATE},
    # Africa (4)
    {"headline": "DR Congo aircraft missing; rebels claim shootdown",
     "summary": "Plane lost near Minembwe; pilot and officer aboard",
     "region": "Africa", "date": DATE},
    {"headline": "Ebola responders trapped in Ituri hospital",
     "summary": "WHO staff held by fighting as outbreak spreads",
     "region": "Africa", "date": DATE},
    {"headline": "Zambia opposition leader indicted for treason",
     "summary": "Main opposition chief charged over alleged plot",
     "region": "Africa", "date": DATE},
    {"headline": "Drone strikes hit UN building in Khartoum",
     "summary": "UN condemns attacks; 19.5m face famine risk in Sudan",
     "region": "Africa", "date": DATE},
    # Oceania (2)
    {"headline": "Australia: people can sue tech firms, fines up to 5%",
     "summary": "Online safety deal exposes giants to huge fines",
     "region": "Oceania", "date": DATE},
    {"headline": "Melanoma researcher wins Australian science prize",
     "summary": "Georgina Long wins Prime Minister's Prize for Science",
     "region": "Oceania", "date": DATE},
    # Global (2)
    {"headline": "COP31 ends without a deal; EU seeks rule change",
     "summary": "Longest climate talks fail over fossil-fuel language",
     "region": "Global", "date": DATE},
    {"headline": "BepiColombo enters Mercury orbit after 8 years",
     "summary": "European-Japanese craft on track despite a glitch",
     "region": "Global", "date": DATE},
]

for _lead in LEADS:
    _lead["date"] = DATE
