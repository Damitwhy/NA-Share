# NA-SHARE  
A Narcotics Anonymous Sharing Community.  

![Am I Responsive Image.](/project_readmes/images/ui.dev2.png)  

## Overview  
Project to create a Django social platform for members of Narcotics Anonymous (NA) and all those effected by addiction.  
Service users can post their stories as 'shares' so as to share their experiences and comment on other user 'shares' in a supportive environment, message other users or comment on comments.  with full C.R.U.D functionality to Create, Read, Update and Delete shares and comments, admin will approve posts.  
The NA-Share project hopes to utilize the same benefits found in the process of sharing found at Narcotics Anonymous meetings, to create a cathartic experience for users, allowing them to express and share their emotions freely, leading to a sense of relief and connection.  

## User Experience Design (UX)
- **UX Design Process**:  
  - Based on User-centricity NA-Share address user's needs via User Stories. focusing on the needs of those Users who would like a place to share and balancing what can be achieved to meet those needs within an agile methodology and given a time frame for completion.  
  
- **Consistency**  
  - Our users have shown what they would expect of NA-Share with experience of other social sites and reflected that within their user stories, keeping NA-Share consistent with those technologies is an important factor in our design and functionality.  

- **Hierarchy**
  - Keeping the site simple helps Users navigate NA-Share intuitively, having most of the action on the Home page allows users to find the shares and sharing experience without complication but still having navigation within easy reach via our Nav-Bar keeping our users informed.  

- **Context**
  - How our users interact with NA-Share is important, so responsive design is the foundation of NA-Share's structure, making NA-Share accessible to most if not all devices.  
  
- **User Control**
  - Our User stories tell us how much control users need, actions that might be made in error should be limited, good confirmation before action is taken is important.  

- **Accessibility**
  - Making NA-Share accessible to many requires best practices including alt text for screen reader, aria labeling and high contrasting visual appearance.  

- **Usability**  
Aim with agile approach is testing of design concept.
  - Easy to learn!
  - Memorable
  - Efficient
  - Error recovery
  - Satisfaction  
- **User Satisfaction**
  - Our aim is to give our users the feeling they want to keep coming back for.

##  Agile  
- ****

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
- **Sharing Stories**: Users share personal recovery stories and experiences as a Share, much in the same way a user does in an Narcotics Anonymous meeting.  Story board is set in a BootStrap column down the left hand side of the Home Page.  Given the space, Stories/Shares are displayed with a restriction on word count number and page is paginated to display only three shares, a full detailed Share view can be obtained by clicking on the 'view detail' link for each Share. each share also shows how many comments have been made on that share and a created at date and time.  Option for HUMANIZE function for date and time could be added later but atm it looks good and is readable.  
   ![Not Logged in](/project_readmes/images/story-board.png) 
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
  - Comment on comment form. When accessing the 'reply' to comment button users are taken to a comment on comment form with, welcome message and share that the parent comment was made on, then parent comment that user wishes to comment on, a simple text-area with '@*parent-user*' username pre-populated so it allows user and parent comment user to be referenced.
    ![Comment on Comment](/project_readmes/images/comment-on-comment.png)  
- **Approve Feature**: Admin have rights!
  - Admin will need to approve shares before they're displayed, the functionality is present but for the purpose of project assessment this feature has been disabled, looking at the detail view of each share will show the share's 'Status' with values of either Approved, Pending or Rejected.  
- **About Page**: More Information.  
  - Provides a little more information on the purpose and reasoning behind the NA-Share project, detailing some of the processes of the Narcotics Anonymous program and what parts of that process NA-Share benefits from.  
  ![about Page](/project_readmes/images/about-page.png)
- **Contact Us**: Any visitor has ability to contact.
  - Contact page consists of a form with Name, Email and Message text input areas, each value is required before message will be uploaded to the Database, functionality uploads message with created at date and boolean read value set as null so when Admin receives it they can see it need attention.  Page is thoughtfully set out in a div with background image with hands reaching up, text "please feel free to reach out to us"  
  ![Contact Page](/project_readmes/images/contact-us.png)
- **Accessed Counter**: How many Homepage hits?
  - So out of interest a page hit counter has been set up which increments a database entry by 1 each time the home page is landed. it was buggy to begin with adding two entries each hit but is now working, database entry can not be changed by admin or superuser so the value is there to stay.  
  ![Counter](/project_readmes/images/counter.png)  
- **Modal reminder**: Are you logged-in?
  - Set as a reminder to inform Anonymous users to be logged-in and in turn be registered users, modal will display when ever Anonymous heading is hovered over in Home and Stories_detail pages.  
  ![Modal](/project_readmes/images/modal.png)  
- **Notifications**: have you signed in? have you signed out? system error? 
  - Use of Django-messages takes care of informing users when they have made an action such as sign out, logged-in, message sent, you are now registered... 
  - Website error pages 400, 403, 404 and 500 have been created styled and include NA-share header and footer so navigation is not lost.
- **Font Awesome Social Media**: 
    - Is ever more important to link to social media, it seems its the best place to advertise and having a presence means you could get lot of foot fall come your way.
- **Anonymity**: Ensure user anonymity and privacy.  
  - NA-Share conforms to the data-protection act.  
  - Users may report Shares via our contacts page.  
  - there are no account settings as of yet but when there are we will consider Privacy settings.  
## Technologies Used  

- **Frontend**: HTML, CSS, BootStrap, JavaScript, Django
- **Backend**: Django, Python
- **Database**: PostgreSQL
- **Authentication**: To Be Decided JWT (JSON Web Tokens)
- **Hosting**: Heroku  

## Testing  
- ****
## Deployment

## Usage

- Register an account or log in if you already have one.
- Sharing your recovery journey.
- Comment on other's Shares to help others in the community.
- Connect with other members through private messages.


## Credits


## Contributing
We welcome contributions! Please read our Contributing Guidelines for more details.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
For any questions or suggestions, please open an issue or contact us at kenneth.cox@students.codeinstitute.net

---

*Note: This project is inspired by the principles of Narcotics Anonymous and aims to provide a safe and supportive online community for its members.*
