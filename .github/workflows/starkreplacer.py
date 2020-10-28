

name: Sed
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Find and Replace
        uses: jacobtomlinson/gha-find-replace@master
        with:
          find: "userbot"
          replace: "friday-userbot"
      - name: Pull All Updates
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: 'Hmm'
          commit_options: '--no-verify'
          repository: .
          commit_user_name: StarkGang
          commit_user_email: starkgangz@gmail.com
          commit_author: StarkGang <starkgangz@gmail.com>
