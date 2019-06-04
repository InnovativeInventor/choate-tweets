## Choate-tweets
The goal of this project is to preserve all tweets pertaining to Choate on Twitter for posterity. Twitter does not display all tweets beyond a certain point, so archiving all tweets could be potentially usefull for future students to analyze.

All tweets are dehydrated (as per [Twitter's devloper policy](https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases.html)). To hydrate the tweets, you can use the following tools:
- [twarc](https://github.com/DocNow/twarc) (CLI tool with other features)
- [Hydrator](https://github.com/DocNow/hydrator) (GUI)

The repo is structured as follows:
```
- official_tweets.txt
- related_tweets.txt (superset of official_tweets.txt) 
- official_accounts.txt 
- related_terms.txt
```

## Code License
```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
```
