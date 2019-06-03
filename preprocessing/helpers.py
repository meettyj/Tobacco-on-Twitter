

from pipelines.helpers import ExplodingRecordJoiner

ready_made_exploder = ExplodingRecordJoiner(user=[
    'created_at',
    'favourites_count',
    'followers_count',
    'friends_count',
    'statuses_count',
    'verified'
])



# class ReadyMadeHeirarchy:
#     clf_alch = load(open(
#         "./clfs/LogisticRegression|label:alcohol|accuracy:0.7970909090909091|f1:0.8367466354593329|feature:['text', "
#         "'user', 'age']"
#         , "rb+"))
#     clf_frst = load(open(
#         "./clfs/LogisticRegression|label:first_person|accuracy:0.6640826873385013|f1:0.721030042918455|feature:["
#         "'text', 'user', 'age']"
#         , "rb+"))
#     clf_fstl = load(open(
#         "./clfs/LogisticRegression|label:first_person_level|accuracy:0.4703196347031963|f1:0.46356955515952386"
#         "|feature:['text']"
#         , "rb+"
#     ))
#
#     root = Taxonomy(
#         "alcohol",
#         {
#             0: "non_drinking",
#             1: "drinking"
#         },
#         clf_alch["clf"]
#     )
#
#     first_person = Taxonomy(
#         "first_person",
#         {
#             0: "alcohol_related",
#             1: "first_person"
#         },
#         clf_frst["clf"]
#     )
#
#     first_person_level = Taxonomy(
#         "first_person_level",
#         {
#             0: "first_person_casual",
#             1: "first_person_looking",
#             2: "first_person_reflecting",
#             3: "first_person_heavy"
#         },
#         clf_fstl["clf"]
#     )
#
#
#     first_person.add_children({1: first_person_level})
#     root.add_children({1: first_person})
