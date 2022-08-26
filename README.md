# download_urls
Program to provide download URLs for specified list of entries

# Installation
This program depends on the Python [Kaltura Native Client Libraries](https://developer.kaltura.com/api-docs/Client_Libraries)
```
pip install KalturaApiClient
```

# Usage
```
python3 download_urls <pId> <userId> <adminSecret> <entriesFileName> <outputFileName>
```
| Parameter        | Description             | Example |
| ---------------- |------------------------ | ------- |
| *pId*              | Your Kaltura Partner ID | 1234567 |
| *userId*           | Your user ID            | ron.raz@kaltura.com |
| *adminSecret*      | Your admin secret from [KMC](https://kmc.kaltura.com/index.php/kmcng/settings/integrationSettings) | *Never share your secret* |
| *entriesFileName* | Name of text file containing entry IDs, one per line | entries.txt |
| *outputFileName* | Name of file to output a TSV-formatted list of ENTRY_ID and DOWNLOAD_URL | myUrls.tsv |

# Example
```
$ cat entries.txt
1_4nbc3kuu
1_6kl9795s
1_tetcwunw

$ python3 download_urls.py 1234567 ron.raz@kaltura.com e0xxxxx74591xxxxxf4bcdxxxxxb3af7 entries.txt myUrls.tsv

$ cat myUrls.tsv
ENTRY_ID     DOWNLOAD_URL
1_4nbc3kuu   https://cfvod.kaltura.com/pd/p/.../flavorId/1_gruercd4/fileName/Pes1_(Basic_Small_-_WEB_MBL_(H264_600)).mp4/name/a.mp4
1_6kl9795s   https://cfvod.kaltura.com/pd/p/.../flavorId/1_8a6ihk7o/fileName/_Social_Video_Portal_(SD_Large_-_WEB_MBL_(H264_1500)).mp4/name/a.mp4
1_tetcwunw   https://cfvod.kaltura.com/pd/p/.../flavorId/1_n2q3r9v9/fileName/_Monetizing_Videos_on_the_Web_(HD_1080_-_WEB_(H264_4000)).mp4/name/a.mp4
```
