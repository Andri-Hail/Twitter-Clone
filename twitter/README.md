This is a Twitter inspired site created by Andri Hail, Jason Friedman, and Amy Guo that has the following functionalities:
  - Secure log in, sign up, and log out
  - Posting, liking, and deleting tweets
  - Replying to tweets
  - Uploading media content
  - User profile with bio and profile picture
  - Filtering by hashtags
  - Error handling (when DEBUG = False) 
  
Design Considerations:

We wanted to emulate Twitter as much as possible so a clean-looking UI was important to us. We also decided that it would only be possible    to reply to top-level tweets so that the home page wouldn't get too cluttered. We wanted to keep everything as central as possible so we decided to use modals for a lot of features instead of linking to different pages. This ensured our project would be constrained across only four pages: Log in, home, profile, and edit profile. 
 
