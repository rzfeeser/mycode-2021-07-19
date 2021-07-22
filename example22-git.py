# move into where linux likes to store keys
cd ~/.ssh

# generate a new key pair
ssh-keygen -f id_rsa_github

# display the public key
cat id_rsa_github.pub

# copy the public key and paste into your github repo --> settings --> deploy keys (remember r/w access)

# set metadata for commits
git config --global user.email "z@users.noreply.github.com"
git config --global user.name "rzfeeser"

# clone your code from github (https://github.com/rzfeeser/mycode)
git clone git@github.com:rzfeeser/mycode


# ONLY if you clone incorrectly (i.e. origin gets messed up), you can fix the definition of "origin" with the
# command below
git remote set-url origin git@github.com:rzfeeser/mycode

# You're back!
