#!/usr/bin/env bash
VERSION=$(cat pyproject.toml|rg -i version|tr -d 'version = ')
PROJ=$(basename .)
printf "PROJECT: %s\t\tVERSION: %s\n======================================\n" $PROJ $VERSION
printf "Upgrading tools..."
pip install --upgrade setuptools &>/dev/null
pip install --upgrade build &>/dev/null
pip install --upgrade twine &>/dev/null
printf '\t\t\x1b[32mDONE\x1b[m\n'
printf 'Running Tests... '
python -m unittest &> .STATUS_TESTS
[[ -n $(cat .STATUS_TESTS|rg -i '^OK$') ]] && TESTSTATUS='OK' || TESTSTATUS='FAIL'
rm .STATUS_TESTS
printf '\t\t\x1b[32mDONE\x1b[m\t\tRESULT: %s\n' $TESTSTATUS
printf 'building %s v%s ...' $PROJ $VERSION
python -m build &>/dev/null
printf '\t\t\x1b[32mDONE\x1b[m\n'
prinf 'GIT:\t\t|\t\tStaging changes: '
git add . &>/dev/null
printf '\t\t\x1b[32mDONE\x1b[m\t\t|\t\t'
printf 'Committing Changes: '
echo "CURRENT VERSION: $VERSION :: TESTS: $TESTSTATUS :: CHANGED: " > .GITCOMMIT_MESSAGE
git status &>> .GITCOMMIT_MESSAGE
git commit -m "$(cat .GITCOMMIT_MESSAGE)"
printf '\x1b[32mDONE\x1b[m\t\t|\t\t'
git commit -m "$MESSAGE"
echo "Pushing to Remote: "
git push
printf '\t\x1b[32mDONE\x1b[m\t\t|\n'
printf "Uploading to Pypi.."
twine upload  dist/* --verbose  --skip-existing  -u '__token__' -p "$(cat .PYPI_APIKEY)"
printf '\n\n\x1b[1;32mDONE\x1b[m\n\n'

