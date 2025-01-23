# tw-scraper-sigpipe-reprod
 
Reproduction for https://github.com/mnwato/tradingview-scraper/issues/19

Run dockerised version with:
```
docker build -t tw-scraper-sigpipe-reprod . && docker run -it --rm --name sigpipe-reprod tw-scraper-sigpipe-reprod
```