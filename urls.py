# INSTRUCTIONS -- IMPORTANT FOR CUSTOM USE
# Put the correct domain (Just the base www.example.com without any extensions) below the "DOMAIN" comment
# Right click where the latest chapter is listed -> inspect element -> right click element in HTML -> copy -> selector
# Paste these selectors in the right string beneath wherever it says PASTE

# Dictionary that maps each domain to the tags for 'current chapter' and 'last updated'
tags = {
    "www.mangaread.org": {
        "current_chapter": "[class*=wp-manga-chapter]",
        "last_updated": "[class*=chapter-release-date]"
    },
    "flamescans.org": {
        "current_chapter": "#post-44782 > div.main-info > div.second-half > div.right-side > div > div.lastend > div:nth-child(1) > a > span.epcur.epcurlast",
        "last_updated": "#chapterlist > ul > li:nth-child(1) > a > div > div > span.chapterdate",
    },
    "manhuaplus.com": {
        "current_chapter": "#manga-chapters-holder > div.page-content-listing.single-page > div > ul > li:nth-child(1) > a",
        "last_updated": "#manga-chapters-holder > div.page-content-listing.single-page > div > ul > li:nth-child(1) > span",
    },
    "www.asurascans.com": {
        "current_chapter": "span[class*=chapternum]",
        "last_updated": "span[class*=chapterdate]",
    },
    "manga1st.online": {
        "current_chapter": "body > div.wrap > div > div.site-content > div > div.c-page-content.style-1 > div > div > div > div.main-col.col-md-8.col-sm-8 > div > div.c-page > div > div.page-content-listing.single-page > div > ul > li:nth-child(1) > a",
        "last_updated": "body > div.wrap > div > div.site-content > div > div.c-page-content.style-1 > div > div > div > div.main-col.col-md-8.col-sm-8 > div > div.c-page > div > div.page-content-listing.single-page > div > ul > li:nth-child(1) > span > i",
    },
    "thelonenecromancer.com": {
        "current_chapter": "li[class*=su-post]",
        "last_updated": "",
    },
    # DOMAIN
    "www.example.com": {
        # PASTE
        "current_chapter": "h3.chapter-name",
        # PASTE
        "last_updated": "p.updated-on",
    },
}

# List of objects to iterate through
objects = [
    {
        "title": "Infinite Level Up in Murim",
        "current_chapter": "Chapter 1",
        "url": "https://www.mangaread.org/manga/infinite-level-up-in-murim/",
        "last_updated": "2022-01-01",
    },
    {
        "title": "Martial Peak",
        "current_chapter": "Chapter 1",
        "url": "https://manhuaplus.com/manga/martial-peak/",
        "last_updated": "2022-01-01",
    },
    {
        "title": "Wandering Warrior of Wudang",
        "current_chapter": "Chapter 1",
        "url": "https://www.asurascans.com/manga/wandering-warrior-of-wudang/",
        "last_updated": "2022-01-01",
    },
    # {
    #     "title": "I Am the Fated Villain",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/i-am-the-fated-villain/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Reaper of the Drifting Moon",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/reaper-of-the-drifting-moon/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Worthless Regression",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/worthless-regression/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Damn Reincarnation",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/damn-reincarnation/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Reformation of the Deadbeat Noble",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/reformation-of-the-deadbeat-noble/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Legend of Asura the Venom Dragon",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/legend-of-asura-the-venom-dragon/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Heavenly Demon Cultivation Simulation",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://flamescans.org/ygd/series/1672354921-heavenly-demon-cultivation-simulation/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Reborn Ranker - Gravity User",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://manga1st.online/manga/reborn-ranker-gravity-user/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Player Who Can't Level Up",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/player-who-cant-level-up/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "The Return of the Crazy Demon",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/the-return-of-the-crazy-demon/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Reincarnation of the Suicidal Battle God",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/reincarnation-of-the-suicidal-battle-god/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Return of the Mount Hua Sect",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://www.asurascans.com/manga/return-of-the-mount-hua-sect/",
    #     "last_updated": "2022-01-01",
    # },
    # {
    #     "title": "Solo Necromancy",
    #     "current_chapter": "Chapter 1",
    #     "url": "https://thelonenecromancer.com",
    #     "last_updated": "2022-01-01",
    # },
]
