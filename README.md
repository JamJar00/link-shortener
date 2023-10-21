# Link Shortener

This is the link shortener deployed at [https://go.jread.dev](https://go.jread.dev). It 'shortens' links through a simple lookup of the path after the URL.

The link shortener is deployed as a DigitalOcean App platform function, it stays well within the free pricing tier.

## Deploying
To deploy the link shortener:
1. In DigitalOcean [create an App](https://cloud.digitalocean.com/apps/new)
2. Set the source repository to this repository (you probably want to have a fork of the repo, else you'd just be able to shorten my links... which is probably not not very useful to you...)
3. Setup the DNS so you have a nice URL
4. Go to the link-shortener component's settings and change the `HTTP Request Routes` so that `/` routes to `/link-shortener/go/`. This will shorten the URL that you need to call to hit the shortener
5. Test by going to `/goog`. It should take you to Google.
