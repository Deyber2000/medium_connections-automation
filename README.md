## Python Medium matcher
Medium has a large amount of content, a large number of users, and an almost overwhelming number of posts. When you try to find interesting users to interact with, you’re flooded with visual noise.

I define an interesting user as someone who is from your network, who is active, and who writes responses that are generally appreciated by the Medium community.

I was looking through the latest posts from users I follow to see who had responded to those users. I figured that if they responded to someone I’m following, they must have similar interests to mine.

This app automates the process for you. Using the Medium's API you can easily find the users that best match with you.

# Intructions
## Instructions

Install the packages

    sudo pip install requests click

Checking how to use the script

    python finder.py --help

Example

    python finder.py --name Radu_Raicea --min-recommendations 10