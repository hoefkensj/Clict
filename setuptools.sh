#!/usr/bin/env bash
echo "Upgrading tools..."
pip install --upgrade setuptools &>/dev/null
pip install --upgrade build &>/dev/null
pip install --upgrade twine &>/dev/null
echo 'building ...'
python -m build &>/dev/null
echo 'Staging changes'
git add . &>/dev/null
cat pyproject.toml|rg -i version|tr -d 'version = ' &> .GITCOMMIT_MESSAGE
echo -e "\n--------------\n\n" &>> .GITCOMMIT_MESSAGE
python -m unittest &>> .GITCOMMIT_MESSAGE
echo -e "\n--------------\n\n" &>> .GITCOMMIT_MESSAGE
git status &>> .GITCOMMIT_MESSAGE
MESSAGE="$(cat .GITCOMMIT_MESSAGE)"
echo "Committing Changes..."
git commit --message=$MESSAGE
echo "Pushing changes to remote..."
git push origin

echo "Uploading to Pypi.."
twine upload  dist/* --verbose <<< $(cat .PYPI_APIKEY)
printf '\n\n\x1b[1;32mDONE\x1b[m\n\n'

