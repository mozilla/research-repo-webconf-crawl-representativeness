# The representativeness of automated Web crawls as a surrogate for human browsing: companion repository

This repository contains or links to all assets relevant to the WWW'20 paper: [The representative of automated Web crawls as a surrogate for human browsing](https://dl.acm.org/doi/abs/10.1145/3366423.3380104). All listed assets will be made publicly available pending internal privacy/trust audit processes required prior to data release. For specific inquiries pertaining to data access and collaborations on privacy enhancing technologies research please reach out to the corresponding authors listed on the manuscript.

* Lists used for crawls: under [lists](./lists/) directory
* Trexa repo: https://github.com/mozilla/trexa
* Crawl preparation (pre crawl and depth crawl code): https://github.com/mozilla/crawl-prep
* Crawl database: [Google Doc](https://docs.google.com/spreadsheets/d/1HlocB39Ujaw2JH4Nm_0lXFqQ6GcQjJ7ONHHLFq-NReI/)
* Crawl downloads: all the crawl data is stored in a S3 bucket. The total size of the data is __184.2GB__ comprised of:
    + 18.4GB for the 44 time sequence crawls
    + 36.4GB for the two large companion crawls of ~100k sites
    + 129.4GB for the remaining 60 crawls

    The compressed crawl data (64GB) is available on BitTorrent on
[AcademicTorrents](https://academictorrents.com/details/5e9ef2b5531ce3b965681be6eccab1fbd114af62/tech)
    
* Alternate orchestration repo: https://github.com/birdsarah/faust-selenium
* List comparison analysis: under [list-comparison](./list-comparison/top-site-list-comparison.ipynb) directory
* DP-protected top-level domain ranking for opt-in human users [August-2019]: under [human-browsing-top-sites](./human-browsing-top-sites/top_dp_domains_human_browsing.csv) directory

If you find any of the resources contained int his repository valuable for your research please cite the original manuscript for which this work was produced:

```
@inproceedings{10.1145/3366423.3380104,
author = {Zeber, David and Bird, Sarah and Oliveira, Camila and Rudametkin, Walter and Segall, Ilana and Wolls\'{e}n, Fredrik and Lopatka, Martin},
title = {The Representativeness of Automated Web Crawls as a Surrogate for Human Browsing},
year = {2020},
isbn = {9781450370233},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3366423.3380104},
doi = {10.1145/3366423.3380104},
booktitle = {Proceedings of The Web Conference 2020},
pages = {167–178},
numpages = {12},
keywords = {Web Crawling, Online Privacy, Tracking, Browser Fingerprinting, World Wide Web},
location = {Taipei, Taiwan},
series = {WWW ’20}
}
```
