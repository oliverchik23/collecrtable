   if anime_ul is None or isinstance(anime_ul, NavigableString):
        msg = f"Could not find and anime with name {anime_name}"
        raise ValueError(msg)#good
    anime_li = anime_ul.children]

    anime_list = []
    for anime in anime_li:
        if isinstance(anime, Tag):
            anime_url = anime.find("a")
            if anime_url is None or isinstance(anime_url, NavigableString):
                continue
            anime_title = anime.find("a")
            if anime_title is None or isinstance(anime_title, NavigableString):
                continue#anime

            anime_list.append({"title": anime_title["title"], "url": anime_url["href"]})

    return anime_list

  for episode in episode_page_li:
        if isinstance(episode, Tag):
            url = episode.find("a")
            if url is None or isinstance(url, NavigableString):
                continue
            title = episode.find("div", {"class": "name"})
            if title is None or isinstance(title, NavigableString):
                continue
