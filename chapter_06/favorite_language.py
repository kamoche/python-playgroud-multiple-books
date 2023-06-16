
favorite_language = {
    'kamoche': 'scala',
    'jackson': 'java',
    'githinji': 'python',
    'vic': 'python'
}


for name,language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.upper())

friends = ['kamoche','jackson']
# same as for name in favorite_language
for name in favorite_language.keys():
    print("Key: "+ name.title())

    if name in friends:
        print(name.title() + ", I see your favorite number is " +
        favorite_language[name].title())

if 'sharon' not in favorite_language.keys():
    print("Sharon, please take the poll")

for name in sorted(favorite_language.keys()):
    print(name.title() + " thank you for taking the poll")

print("\nThe following languages have been mentioned")
for language in set(favorite_language.values()):
    print(language.title())

