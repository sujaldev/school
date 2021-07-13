cd ./bin || exit
python3 update-website.py
git status
cd ../
git add docs
git commit -m "updated docs"
