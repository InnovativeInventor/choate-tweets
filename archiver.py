from archive import ArchiveTweet

# Consumer API, Consumer secret, Access token, Access token secret
archiver = ArchiveTweet('ram5ry9JGyleYXnm0x3wrkgZk',
                        '2PnlOACLHGN3BDodpaV3RvaYOuCcDRCygcamDoJ6Q8SuucM5db',
                        '944986243296882688-QwaMJx5UBB3Uj2o8Qjd2gjKzDp5GRKx',
                        'jZ5RquDuBLR4RcpSz2lv4Acgyk4L4IUVkSOhuzDDUX31C')

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

# Related tweets
with open("related_terms.txt", "r") as filename:
    for each_hashtag in filename:
        ids = archiver.archive_hashtag(
            each_hashtag.rstrip(), full_backup=False)
        ids += archiver.archive_hashtag(
            '#' + each_hashtag.rstrip(), full_backup=False)
        archiver.write_data('related_tweets.txt', ids)
        print(each_hashtag.rstrip(), '#' + each_hashtag.rstrip(), len(ids))
