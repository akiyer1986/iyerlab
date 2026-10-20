# Iyer Lab website

A free website you edit through forms, with no coding. Photos are uploaded by dragging them into the editor.

- `index.html` holds the design. You never need to open it.
- `content/` holds every word on the site (people, news, papers, research, openings, links).
- `images/` holds uploaded photos.
- `.pages.yml` tells the Pages CMS editor which forms to show.

## One-time setup (about 15 minutes)

1. **Make a GitHub account** at https://github.com/signup (free).
2. **Create a repository**: click "+" → "New repository", name it `iyerlab-site`, set it to Public, then "Create repository".
3. **Upload the files**: on the new repository page, click "uploading an existing file". Drag in everything from this folder: `index.html`, `.pages.yml`, and the `content` and `images` folders. Then click "Commit changes".
   On a Mac, press Cmd+Shift+. in Finder to show the hidden `.pages.yml` file.
4. **Turn on the website**: in the repository, open Settings → Pages. Under "Branch", choose `main` and `/ (root)`, then Save. After a minute or two the site is live at `https://<your-username>.github.io/iyerlab-site/`.
5. **Open the editor**: go to https://app.pagescms.org, sign in with GitHub, allow access to `iyerlab-site`, and open it.

## Everyday editing

In Pages CMS you'll see Group members, News, Publications, About the PI, Lab details, Former members and Useful links in the sidebar.

- **Add a person or news item**: open the section, click "Add an entry", fill in the form, and drag a photo onto the Photo field.
- **Group photo or home page photo**: open "Lab details, research and openings".
- Click **Save**. The live site updates about a minute later.

## Moving iyerlab.ca to the new site

Do this only once you're happy with the new site.

1. In the repository, open Settings → Pages → Custom domain, enter `www.iyerlab.ca`, and Save. Tick "Enforce HTTPS" once it becomes available.
2. At the company where you bought iyerlab.ca, change the `www` CNAME record to `<your-username>.github.io`.

Your Google Site keeps working until you make step 2.

## Still to fill in
- Photos for the PI, members and news items (the Google Sites images could not be copied automatically).
- Full titles for older publications.
- Google Scholar and LinkedIn links (About the PI → Profile links).

## Page addresses

Each page has its own address (www.iyerlab.ca/research/, /team/, /publications/, /news/, /join-us/, /resources/). The folders with those names hold copies of `index.html`. After changing `index.html`, run `python3 tools/build_pages.py` to refresh the copies, the redirects for old addresses and `sitemap.xml`. Editing content in Pages CMS does not need this step.
