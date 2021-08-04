import os

total_commits = 1024 # including the "bad" one
index_of_bad_commit = 729 # from 0 (inclusive) to total_commits (exclusive) 

def commit_with_message(msg: str):
    os.system('git add .')
    os.system(f'git commit -m "{msg}"')

def append_text_to_file(text: str, filename: str):
    os.system(f'echo {text} >> {filename}')

def make_good_commit_with_range(start: int, end: int):
    for i in range(start, end):
        text = f'good at idx: {i}'
        append_text_to_file(text, 'good.txt')
        commit_with_message(text)

def main():
    if not (0 <= index_of_bad_commit < total_commits):
        print('Total commits should be more than 0 and bad commit index should be in the range [0, total_commits)')
        return

    # Just so that commits are not associated to my email
    os.system('git config user.email "<>"')

    # Make good commits until bad commit index
    make_good_commit_with_range(0, index_of_bad_commit)

    # Make bad commit
    text = f'bad at idx: {index_of_bad_commit}'
    append_text_to_file(text, 'bad.txt')
    commit_with_message(text)

    # Make good commits afterwards
    make_good_commit_with_range(index_of_bad_commit + 1, total_commits)

if __name__ == '__main__':
    main()
