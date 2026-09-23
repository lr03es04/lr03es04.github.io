# Seminar of FST-PDEs Laboratory LR03ES04

Static seminar homepage for GitHub Pages. Director: Professor Slim Tayachi.

## Content and outstanding details

The 88 names and ranks were transcribed from pages 5–15 of the 2025 activity report supplied by the user: 19 Corps A, 31 Corps B, 24 doctoral researchers, 10 postdoctoral researchers/equivalent staff, and 4 research master's students. Given names appear first; original spellings are retained. The member tables contain no email addresses. No upcoming talk information was supplied. Missing information is explicitly labelled, never invented.

Professor Slim Tayachi’s email, `slimtayachi@gmail.com`, is supplied on the report’s cover page and is included. The other 87 email addresses remain to be supplied.

The original PDF, rendered pages, identity numbers, and financial records are not part of the website or deployment.

## Edit the homepage

Edit `data/members.json` for names and ranks. Edit `data/content.json` for email addresses, announcements, and talks. Then run `python build.py` and commit the regenerated `index.html` along with your data changes. The deployed site has no runtime dependencies and works without JavaScript.

Example content structure (replace the example values with confirmed information):

```json
{
  "emails": {"Full name exactly as listed": "confirmed@example.org"},
  "announcements": [{"title": "Announcement title", "text": "Announcement text"}],
  "talks": [{
    "title": "Talk title",
    "speaker": "Speaker name and affiliation",
    "date": "15 October 2026",
    "time": "14:00 (Tunis time)",
    "location": "Confirmed building and room",
    "abstract": "Full abstract text."
  }]
}
```

Place the next seminar first in the talks list: the top panel uses its date, time, and location. Move or remove past talks when updating the next seminar. Plain text is escaped safely; HTML is not interpreted. Expandable abstract and member sections work natively in the browser.

## Free GitHub Pages hosting

1. Create a public GitHub repository named `Othman-Echi`.
2. Upload `index.html`, `styles.css`, `favicon.svg`, and `.nojekyll` to its main branch. The data folder, build script, and README may also be committed to make future editing easier. Do not upload `tmp/` or the source PDF.
3. In the repository, open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, select **main** and **/(root)**, and save.
4. Wait for GitHub to show a successful deployment. For the connected account, the expected address is `https://othman-echi.github.io/Othman-Echi/`. This is an expected address, not proof of deployment.

GitHub Pages supports public repositories on GitHub Free: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## Local preview

Open `index.html` directly, or run `python -m http.server 8765 --bind 127.0.0.1` from this directory and visit http://127.0.0.1:8765/.

