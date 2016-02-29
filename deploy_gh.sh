echo "Generating site content......"

# git subtree add --prefix=public git@github.com:simonpatrick/simonpatrick.github.io.git gh-pages --squash
# git subtree pull --prefix=public git@github.com:simonpatrick/simonpatrick.github.io.git gh-pages
hugo -t robust

# Add everything
git add -A

# Commit and push to master
git commit -m "$1" && git push origin master

git subtree push --prefix=public git@github.com:simonpatrick/simonpatrick.github.io.git gh-pages
