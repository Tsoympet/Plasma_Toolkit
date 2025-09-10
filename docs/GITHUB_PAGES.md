
# Enable GitHub Pages
1. Push this repo to GitHub, branch `main` (ή `master`).
2. Settings → Pages → Build and deployment: *GitHub Actions*.
3. Κάνε ένα push για να τρέξει το workflow `docs` και να δημοσιεύσει τα HTML.
4. Το URL θα δοθεί ως artifact στο job **deploy** (δες Actions).

PDF docs ανεβαίνουν ως artifact `docs-pdf` στο Actions.
