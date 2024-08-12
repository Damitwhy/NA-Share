 :# NA-SHARE  
A Narcotics Anonymous Sharing Community.  

![Am I Responsive Image.](/project_readmes/images/ui.dev3.png)  

## Overview  
Project to create a Django social platform for members of Narcotics Anonymous (NA).  
Service users can post their stories as 'shares' so as to share their experiences and comment on other user 'shares' in a supportive environment, message other users or comment on comments.  with full C.R.U.D functionality to Create, Read, Update and Delete shares and comments, admin will approve posts.  
The NA-Share project hopes to utilize the same benefits found in the process of sharing found at Narcotics Anonymous meetings, to create a cathartic experience for users, allowing them to express and share their emotions freely, leading to a sense of relief and connection.  

## Features  

- **Nav Bar**:  
  - Featured on all pages, the fully responsive navigation bar includes links to the Logo, Home page, About page, Services page and Contact page, checks if user is logged in and adds links to Register, Sign in or Log out, this is identical in each page to allow for easy navigation.  
    ![Nav Bar](/project_readmes/images/responsive-nav-small.png)  
    ![Nav Bar](/project_readmes/images/responsive-nav-large.png)  
- **Welcome Banner**  
  - Featured on Home page, is fully responsive, banner includes hero image (as div background) and welcome message with description and link to About page for more information.  
    ![Nav Bar](/project_readmes/images/banner.png)  
- **User**: Personal account.  User account options are yet to be implemented, we envision later adding features such as account editing, account Bio information, Likes, full comment and share history, ability to add users to favourites and an internal messaging service.  
  - **User Authentication**  
     - Use of Django-Allauth template for authentication, utilizing the AUTH_USER_MODEL = 'core.User', Checking user is authenticated or in database then creating user session.  
  - **Sign In**  
     - Use of Django-Allauth template for Sign in linked to its own page including Nav-bar and footer, having edited the default template for use in the NA-Share project, being fully responsive.  Sign in utilizes Django-Allauth authentication method.  
     ![Sign in image](/project_readmes/images/sign-in.png)  
  - **Sign Out**  
    - Use of Django-Allauth template for Sign out linked to its own confirmation page including Nav-bar and footer, having edited the default template for use in the NA-Share project, being fully responsive.  Sign out utilizes Django-Allauth authentication method.
      ![Sign out image](/project_readmes/images/sign-out.png)  
  - **Register/Sign Up**  
    - Use of Django-Allauth template for Registration linked to its own confirmation page including Nav-bar and footer, having edited the default template for use in the NA-Share project, being fully responsive.  Register or Sign up utilizes Django-Allauth authentication method to check user email is unique and User model to add new user to database.  
      ![Sign up imager](/project_readmes/images/register.png)  
- **Sharing Stories**: Share personal recovery stories and experiences as a Share, much in the same way a user does in an Narcotics Anonymous meeting.  
  - Sharing a story/share requires users to be registered to NA-Share. so pressing any link to share or comment when not signed in redirects user to a login with optional link to sign up page.  
    ![Not Logged in](/project_readmes/images/not-logged-in.png)  
  Once logged in a share link is made available or made accessible, to create a comment users are presented with Share your story page form, allowing title and content inputs and a submission button, the content text area utilizes Django-Summernote so creative users can benefit from the extra abilities summer note has, such as ability to use or pass in html code to include URL's to images, links to other resources, freedom of expression.  it is recognized this could be a security issue so all shares should be approved first, see Approve feature ![**Approve-feature**](**Approve-Feature)  
    ![Story Share](/project_readmes/images/share-story.png)  

- **Comment on Stories**: Commenting on Shares is as easy as pressing on available links associated with that Share, these can be found on Home and Stories_detail pages.  
  - When not logged in Comment link will take users to a not logged in page requiring users to be authenticated first.  
    ![Not Logged in](/project_readmes/images/response-unauth-comment.png)  
  - When user is logged in / Authenticated, on pressing the Comment link they will be presented with the Comment page where they see a welcome message specific to user logged in, heading 'Comment on:' with the title of share to be commented on, the Share and a simple text input area with submit button.  
    ![comment-input](/project_readmes/images/comment-input.png)  
- **Comment on Comments**: Service users comment on comments.  
  - When user is not logged in a link to reply on comment is presented but takes user to page that reminds them they are not logged in.  
    ![reply-button](/project_readmes/images/reply-button.png)  
  - When user is logged in they have the reply link, if they are logged in and own that comment they also get link options to edit or delete that comment.  
    ![Reply Comment options](/project_readmes/images/comment-options.png)  
  - Comment on comment form. When accessing the 'reply' to comment button users are taken to a comment on comment form with, welcome message and share that the parent comment was made on, then parent comment that user wishes to comment on, a simple text-area with '@<user>' pre-populated so it allows user and parent comment user to be referenced.
    ![Comment on Comment](/project_readmes/images/comment-on-comment.png)  
- **Approve Feature**:
- **Contact Us**: Any visitor has ability to contact.
- **Anonymity**: Ensure user anonymity and privacy.

## Technologies Used

- **Frontend**: HTML, CSS, BootStrap, JavaScript, Django
- **Backend**: Django, Python
- **Database**: PostgreSQL
- **Authentication**: To Be Decided JWT (JSON Web Tokens)
- **Hosting**: Heroku

## Usage

- Register an account or log in if you already have one.
- Sharing your recovery journey.
- Comment on other's Shares to help others in the community.
- Connect with other members through private messages.





## Contributing
We welcome contributions! Please read our Contributing Guidelines for more details.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
For any questions or suggestions, please open an issue or contact us at kenneth.cox@students.codeinstitute.net

---

*Note: This project is inspired by the principles of Narcotics Anonymous and aims to provide a safe and supportive online community for its members.*
