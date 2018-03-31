# glucovis
Visualization for personal blood glucose data

## How to Use

This projects assumes blood glucose data is kept in a
[VimWiki](https://vimwiki.github.io/) table, organized by columns for Date,
Time, Glucose Reading (mg/dL), and an optional Note.

To use this visualizer, follow these steps:

1. Pipe the VimWiki file through `vimwiki2csv.py` and save the result in a file
   named `glucose.json`. Examine this file to ensure it contains reasonable
   looking data.
2. Start a webserver in the root directory of the cloned repository (e.g. via
   `python2 -m SimpleHTTPServer 8000` or `python3 -m http.server 8000`).
3. Point your browser to http://localhost:8000 and give it a few seconds to hook
   everything up.
