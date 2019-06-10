import subprocess
from archive import ArchiveTweet

# Consumer API, Consumer secret, Access token, Access token secret
archiver = ArchiveTweet('seGCCQuugKszR7L7BiEOzqP4u',
                        '8e44MhHHQ8FRpFVmimHArwxBdOjOgiv1AcfZVYwTwQg2WR0VVe',
                        '944986243296882688-QUq9xA5DbjqRlmBN6qlwvd1SxkGT1NO',
                        '4WKlluWkwuAKEJrBnzTvMCpOa517i1VVHoN68h3RdV0ju')

# Official tweets
with open("official_accounts.txt", "r") as filename:
    for each_account in filename:
        ids, hashtags = archiver.archive_account(each_account)
        hashtags = [
            x for x in hashtags if "choate" in x.lower() or "crh" in x.lower()
            or "wildboar" in x.lower()
        ]
        print(len(ids))
        archiver.write_data('official_tweets.txt', ids)
        archiver.write_data('related_tweets.txt', ids)
        archiver.write_data('related_terms.txt', hashtags)

subprocess.run("bash clean.sh", shell=True)

# Related tweets
with open("related_terms.txt", "r") as filename:
    for each_hashtag in filename:
        ids = archiver.archive_hashtag(
            each_hashtag.rstrip(), full_backup=False)
        ids += archiver.archive_hashtag(
            '#' + each_hashtag.rstrip(), full_backup=False)
        archiver.write_data('related_tweets.txt', ids)
        print(each_hashtag.rstrip(), '#' + each_hashtag.rstrip(), len(ids))
