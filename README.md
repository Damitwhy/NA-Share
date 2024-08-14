# NA-SHARE  
A Narcotics Anonymous Sharing Community.  

![Am I Responsive Image.](/project_readmes/images/ui.dev2.png)  

## Overview  
Project to create a Django social platform for members of Narcotics Anonymous (NA) and all those effected by addiction.  
Service users can post their stories as 'shares' so as to share their experiences and comment on other user 'shares' in a supportive environment, message other users or comment on comments.  with full C.R.U.D functionality to Create, Read, Update and Delete shares and comments, admin will approve posts.  
The NA-Share project hopes to utilize the same benefits found in the process of sharing found at Narcotics Anonymous meetings, to create a cathartic experience for users, allowing them to express and share their emotions freely, leading to a sense of relief and connection.  

## User Experience Design (UX)
- **UX Design Process**:  
  - Based on User-centricity NA-Share addresses user's needs via User Stories. focusing on the needs of those Users who would like a place to share and balancing what can be achieved to meet those needs within an agile methodology and within a time frame for completion.  
  
- **Consistency**  
  - Users have shown what they will expect of NA-Share with experience of other social sites and is reflected within their user stories, keeping NA-Share consistent with those technologies is an important factor in its design and functionality.  

- **Hierarchy**
  - Keeping the site simple helps Users navigate NA-Share intuitively, having most of the action on the Home page allows users to find the shares and sharing experience without complication but still having navigation within easy reach via NA=Share's Nav-Bar keeping users informed.  

- **Context**
  - How users interact with NA-Share is important, so responsive design is the foundation of NA-Share's structure, making NA-Share accessible to most if not all devices.  
  
- **User Control**
  - User stories tell us how much control users need, actions that might be made in error should be limited, good confirmation before action taken is important.  

- **Accessibility**
  - Making NA-Share accessible to many requires best practices including alt text for screen reader, aria labeling and high contrasting visual appearance.  

- **Usability**  Aim to with agile approach to test of design concept at inception.
  - Easy to learn!
  - Memorable
  - Efficient
  - Error recovery
  - Satisfaction  
- **User Satisfaction**
  - NA-Share's aim is to give Users the feeling they want, so they keep coming back.  Delivering the service of sharing in a safe, welcoming environment.
- **User Stories**
  - User stories were collected first, numbering 28, top ten posted here and the full list can be found in the User_stories.txt here [User Stories](/project_readmes/User_stories.txt), Stories in this README express the full CRUD functionality of NA-Share.  
    - As a new user, I want to register an account with my email and password so that I can log in and use the site.  
    - As a registered user, I want to log in with my email and password so that I can access my account.
    - As a logged-in user, I want to create and submit a new share so that I can tell my story.
    - As a user, I want to edit my own share so that I can update or correct my story.
    - As a user, I want to delete my own share so that I can remove content I no longer want to be public.
    - As any visitor, I want to view a list of shares so that I can read other user's stories.
    - As an admin, I want to approve or reject new shares before they are posted so that I can ensure the content is appropriate.
    - As a logged-in user, I want to comment on a share so that I can provide feedback or support.
    - As a user, I want to edit my comment so that I can correct or update my feedback.
    - As a user, I want to delete my comment so that I can remove feedback I no longer want to share.

- **MoSCoW Priority List**
  - Filtering through the user's stories required an Ideation list, full copy as pdf file [here](project_readmes/Ideation-table.pdf), once each user story was assessed by value added, against difficulty to create, User stories were categorized as either Must, Should, Could or Won't.  User stories were added to the project Kanban Board/Backlog as Issues and labeled accordingly.  
    - ![MoSCoW prioritized User Stories](/project_readmes/images/MoSCoW-kanban.png)  

- **Wire Frame Work**
  - An essential part of the UX design and Agile processes is Wire framing, user stories tell us what is required to start with and give ideas as to what is needed in the layout and structure.
    - **Layout**
      - Nav-bar, un-cluttered with ease of use navigation.
      - Simple area to display Shares
      - visible representation that User is logged in and area to show and navigate their contributions.
      - Pages: Home page, about page, services page, contact page.
      - information and Social Media Links  
      - Responsive design, Mobile first principle.  
  - Using Balsamiq Wireframes, low definition wire frames are made, sketching out NA-Share's desired look/layout.  
    - Home Page  
      - ![Home Page.](/project_readmes/images/home-wire.png)  
    - About Page  

      - ![About page.](/project_readmes/images/about-wire.png)  
    - Services Page  
      - ![Services page.](/project_readmes/images/services-wire.png)  

## Agile - Workflow - Kanban Board.  
- **GitHub**
  - Using GitHub to store NA-Share's repository allows for the use of the included Project application and Project Kanban board designed with Agile workflow in mind.
    - User stories are added to the Back-log column as Issues, labeled and described with acceptance criteria for completion.
      ![KanBan Board](/project_readmes/images/Kanban_board.png)  
      Once an Issue is worked on its passed to the next column in the line of production until it reaches its completed status, tieing production to feature pull requests helps track progress.  Completing tasks of user story issues allows closure. Link to [Kanban Board](https://github.com/users/Damitwhy/projects/4)  
    - Agile work flow allows for the staggered production of NA-Share.  By focusing on the Must have issues a Minium Viable Product was reachable, with the MoSCoW priority list taken into consideration, the goal was to focus on completing all CRUD functionality for share's and comment issues, Comments on comments came about as an extra and was decided would in the short term be of more value and less difficulty than some of the other issues, it was easier to include it whilst the work for Commenting on shares was done. User stories were gathered whilst in production. Agile workflow allows for good adaptability.

## Usage  
- Register an account or log in if you already have one.
- Sharing your recovery journey.
- Comment on other's Shares to help others in the community.
- Contact site Admin via contacts page with any issues.   

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
- **Approval Feature**: Admin have rights!
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
  - Users may report Shares via NA-Share's contacts page.  
  - There are no account settings as of yet but when there are we will consider robust Privacy settings.  

### Features Left to Implement  
- **Messaging**
  - Create, Delete, View messages to and from Favorite Users.
- **Services**
  - Application that allows staff, admin, superuser to add service links to Services page.
- **Account Profile**
  - Account features, Edit, Delete, Create: Bio, Name, Email, Favorite Users, Profile, stored messages, notifications.
- **Report Content**
  - Ability to fast track a report abuse of service with dated record reporter and Abuser...
- **Policy of Use**
  - With legal research and advice.  
- **Like or Rate**
  - feature to like or rate, shares, comments and users...


## Testing  
- **Manual Testing**  
  - Java Script testing of script.js via https://www.site24x7.com/tools/javascript-validator.html
  - 
  - 
  - 
  - 
- **Automatic Testing**  
  - 
  - 
  - 

- **Validator Testing**  
  - HTML tested with https://validator.w3.org/  
    - ![HTML Validation Success](/project_readmes/images/HTML-Validation-13-08-24.png)  
  - CSS Tested with https://jigsaw.w3.org/css-validator/    
    - ![CSS Validation Success](/project_readmes/images/CSS-Validation-13-08-24.png)  
  - Contrast Testing with WCAG Color contrast checker as a Chrome Extension.

## Deployment
## Technologies Used  

- **Frontend**: HTML, CSS, BootStrap, JavaScript, Django
- **Backend**: Django, Python
- **Database**: PostgreSQL, SQLite(Testing)
- **Authentication**: Django-Allauth 
- **Hosting**: Heroku, GitHub  
- **Development IDE**: VS Code, GitPod, GitHub  
- **Research Tools**: GitHub-Copilot, Chat-GPT
- **Production Tools**: Balsamiq, Chrome-Dev-Tools, Chrome-Extensions



## Credits


## Contributing
We welcome contributions! Please read our Contributing Guidelines for more details.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
For any questions or suggestions, please open an issue or contact us at kenneth.cox@students.codeinstitute.net

---

*Note: This project is inspired by the principles of Narcotics Anonymous and aims to provide a safe and supportive online community for its members.*
