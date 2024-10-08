# NA-SHARE  
### A Narcotics Anonymous Inspired - Sharing Community.  

![Am I Responsive Image.](/project_readmes/images/ui.dev2.png)  
Here is a table of contents for your document:


## Table of Contents  

1. [Overview](#overview)
2. [User Experience Design (UX)](#user-experience-design-ux)
3. [Agile - Workflow - Kanban Board](#agile---workflow---kanban-board)
4. [Usage](#usage)
5. [Features](#features)


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
  - Keeping the site simple helps Users navigate NA-Share intuitively, having most of the action on the Home page allows users to find the shares and sharing experience without complication but still having navigation within easy reach via NA-Share's Nav-Bar keeping users informed.  

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
  - User stories were collected first, numbering 28 to begin with but due to the flexibility of Agile workflow that number increased.  Top ten posted here and the full list can be found in the User_stories.txt here [User Stories](/project_readmes/User_stories.txt).   Stories in this README express the full CRUD functionality of NA-Share.  
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

## ERD Diagram  
  - The Entity-Relationship Diagram (ERD) provides a visual representation of the database structure for the NA-Share project. This is broken down and explained in detail in the ERD Read me file [ERD txt](/project_readmes/ERD.txt), Reference to Message, ServiceLink and Rating Database tables have all been implemented in NA-Share model, have not been activated or put to use in project at present but are in place for future iterations.  

  ![ERD Diagram](/project_readmes/images/core_models_ERD.png)      

## Agile - Workflow - Kanban Board.  
- **GitHub**
  - Using GitHub to store NA-Share's repository allows for the use of the included 'Project' application and Project 'Kanban board' designed with Agile workflow in mind.
    - User stories are added to the Back-log column as Issues, labeled and described with acceptance criteria for completion.
      ![KanBan Board](/project_readmes/images/Kanban_board.png)  
      Once an Issue is worked on its passed to the next column in the line of production until it reaches its completed status, tying production to feature pull requests helps track progress.  Completing tasks of user story issues allows closure. Link to [Kanban Board](https://github.com/users/Damitwhy/projects/4)  
    - Agile work flow allows for the staggered production of NA-Share.  By focusing on the Must have issues a Minium Viable Product was reachable, with the MoSCoW priority list taken into consideration, the goal was to focus on completing all CRUD functionality for share's and comment issues, Comments on comments came about as an extra and was decided would, in the short term be of more value and less difficulty than some of the other issues in the backlog, it was easier to include it whilst the work for Commenting on shares was done. User stories were gathered whilst in production. Agile workflow allows for good adaptability with changing needs.

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
  Once logged in a share link is made available or made accessible, to create a comment users are presented with Share your story page form, allowing title and content inputs and a submission button, the content text area utilizes Django-Summernote so creative users can benefit from the extra abilities summer note has, such as ability to use or pass in html code to include URL's to images, links to other resources, freedom of expression.  it is recognized this could be a security issue so all shares should be approved first, see Approval feature.  
    ![Story Share](/project_readmes/images/share-story.png)  

- **Comment on Stories**: Commenting on Shares is as easy as pressing on available links associated with that Share, these can be found on Home and Stories_detail pages.  
  - When not logged in Comment link will take users to a not logged in page requiring users to be authenticated first.  
    ![Not Logged in](/project_readmes/images/response-unauth-comment.png)  
  - When user is logged in / Authenticated, on pressing the Comment link they will be presented with the Comment page where they see a welcome message specific to user logged in, heading 'Comment on:' with the title of share to be commented on, the Share and a simple text input area with submit button.  
    ![comment-input](/project_readmes/images/comment-input.png)  
- **Comment on Comments**: Service users comment on comments.  
  - When user is not logged-in a link to reply on comment is presented but takes user to page that reminds them they are not logged in.  
    ![reply-button](/project_readmes/images/reply-button.png)  
  - When user is logged-in they the reply link is active, if they are logged in and own that comment they also get link options to edit or delete that comment.  
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
- **Middleware**
  - MiddleWare installed to restrict access to the Admin URL unless signed in already as Staff, Admin or Superuser.  
  This is to restrict opportunities and for the security of the NA-Share application. Attempts made by un-authorized users will redirect to NA-Share 403 page.   
- **Font Awesome Social Media**: 
    - Is ever more important to link to social media, it seems its the best place to advertise and having a presence means you could get plenty of foot fall.
- **Anonymity**: Ensure user anonymity and privacy.  
  - NA-Share conforms to the data-protection act.  
  - Users may report Shares via NA-Share's contacts page.  
  - There are no account settings as of yet but when there are we will consider robust Privacy settings and a User policy Agreement.  

## Features Left to Implement  
- **Messaging** work was started on but not completed so the Model exists but is not in use.
  - Create, Delete, View messages to and from Favorite Users.
- **Services**
  - Application that allows staff, admin, superuser to add service links to Services page.
- **Account Profile**  User model contains Bio value which will be implemented in new iteration of future upgrade.
  - Account features, Edit, Delete, Create: Bio, Name, Email, Favorite Users, Profile, stored messages, notifications.
- **Report Content**
  - Ability to fast track a report abuse of service with dated record reporter and Abuser...
- **Policy of Use**
  - With legal research and advice.  
- **Like or Rate**  A rating system was created but bugfixes were holding back basic CRUD progress so this remains in the back log for future upgrade.
  - feature to like or rate, shares, comments and users...

## Testing  
- **Manual Testing**  
  - Java Script testing of script.js via https://www.site24x7.com/tools/javascript-validator.html
  - Register
    - Create functionality tested  
  - Share
    - All Create, Read, Edit and Delete functionality has been tested manually.  
  - Comment
    - All Create, Read, Edit and Delete functionality has been tested manually.  
  - Comment on Comment
    - All Create, Read, Edit and Delete functionality has been tested manually.  
  - URLs
    - Views  
      - No complications or hangs on opening pages, fully functionality noted. A little slow, Chrome Dev-tools Lighthouse shows we're not running on the fastest servers.
  - Security
    - Tested Non-Authenticated User Editing, deletion, Creation for all C.R.U.D calls to action.
    - Created and Tested Middleware to stop access to /admin page issuing a 403 forbidden Access response.  
  - Broswers
    - Ran all CRUD type tests above on following browsers:
      - Google Chrome, Extension was needed on this browser to display site in 'Am I Responsive' sites.
      - Opera
      - Mozilla FireFox
      - Microsoft Edge
  - Google Chrome Dev-Tools
    - Found issue with closing span tag, corrected. found fault with Fontawesome Kit, opened link to URL on Dev-Tool warning, presented with a page that say, 'Only for Pro Version' but Fontawesome Font all work fine and display. 
- **Automatic Testing**  
  - Carried out by Django testing with.
    - tests_models.py, Good results  
    - tests_views.py, Good results  
    - tests_forms.py, Good results    

- **Validator Testing**  
  - HTML tested with https://validator.w3.org/  
    - ![HTML Validation Success](/project_readmes/images/HTML-Validation-13-08-24.png)  
  - CSS Tested with https://jigsaw.w3.org/css-validator/    
    - ![CSS Validation Success](/project_readmes/images/CSS-Validation-13-08-24.png), Throws up warnings on Bootstrap issues but NA-Share's style.css sheet shows no errors.  
  - Contrast Testing with WCAG Color contrast checker as a Chrome Extension. found fault with 'a' links being too small for there current colors. Changed Text-weight to compensate. Found that this app also indicated white text on dark background so I've Asked for peer review on Slack and the ten people who've responded, looked and found no issue with the visibility of current weight change.  
## Bugs & Fixes
- **Open and Un-closed Tag**  
  - I Know Right? So this is the bane of every programmer, coder or what ever we call our selves.  So through the project when testing error messages would indicate that I's missed ending tags or some times i'd notice a div wasn't displaying properly so bugs were a constant manageable reality, These errors in code if missed first whilst working on feature were revealed in the testing stages.
  - CSS can be a nightmare and picking through code line by line is sometimes the only option, at one point Jigsaw-w3 kept telling me that the error was with ID blah and I couldn't for the life of me find it, until I deleted the ID completely only to find I'd cloned the same code at the bottom of the page where the error actually was.
- **Current Errors/Bugs**
  - During testing it has been discovered through Dev-tools and confirmed with Jigsaw-w3 that some Style sheets have issues but these styles are held by FontAwesome and Bootstrap so its difficult to understand why all styles still work and do what they're supposed to...
  - Cookie warning, change to how Chrome will handle Cookies in the future.
- **Contrast**
  - I'm very aware that I've warnings over 'a' Links for contrast issues being the size of text being small, so I'd addressed this by making Links Bolder so as not to change the aesthetic. Site looks great, peer review has not shown there to be a problem but in new iterations this issue will be addressed.
- **Collect Static**
  - What a lot of palaver. In future projects I think I will let Heroku deal with this as so many times I thought I had a bug, made drastic changes only to find I'd not collected static before pushing to the main. Is it a Bug? No but I treat it as such and something to be aware of.

## Installation on your IDE locally

1. **Clone this Repository**:
   - Create a new repository by cloning this NA-Share GitHub repository:
     ```sh
     git clone https://github.com/Damitwhy/NA-Share.git
     ```

2. **Open in VSCode**:
   - Open your new repository in VSCode desktop with the GitHub desktop app or manually open the folder in VSCode.

3. **Create and Activate Virtual Environment**:
   - Create a virtual environment (venv) if it's not already created:
     ```sh
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:
       ```sh
       .\venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```sh
       source venv/bin/activate
       ```

4. **Install Dependencies**:
   - Install all dependencies from the requirements.txt :
     ```sh
     pip install -r requirements.txt
     ```

5. **Run the Server**:
   - Run the server to see the Django opening page:
     ```sh
     python manage.py runserver
     ```

6. **Set DEBUG to False for Deployment**:
   - Remember always to set [`DEBUG`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspace%2FNA-Share%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A242%2C%22character%22%3A28%7D%7D%5D%2C%22dd83b4f9-d516-48dd-ae0a-6cdf25c586f8%22%5D "Go to definition") to [`False`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspace%2FNA-Share%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A242%2C%22character%22%3A39%7D%7D%5D%2C%22dd83b4f9-d516-48dd-ae0a-6cdf25c586f8%22%5D "Go to definition") in `settings.py` before deploying. Hint sites like Heroku are great for testing your deployments.

7. **Handle Migrations**:
   - There tends to be a warning that no migrations have been made when you first run the server, but this doesn't stop the Django page from loading up. I've normally waited to migrate until I've started to fill the `models.py` file with the ERD model that I require moving forward.
  - You will be ready to migrate when you've set up your default database. See the [Database Configuration](#database-configuration) section. When that is done, you can move on to migrations using the following commands:
     - To create migrations:
       ```sh
       python manage.py makemigrations
       ```
     - To apply migrations:
       ```sh
       python manage.py migrate
       ```

## Database Configuration:

- Django's default database is `db.sqlite3`, which is a file in the root directory. However, you may be better off with an off-site database like PostgreSQL, MySQL, or MongoDB NA-Share is already set up to use PostgreSQL database URL.
- To use PostgreSQL, create a `env.py` file in the root directory of your project and add the following environment variables pointing to your Postgresql URL:
  ```sh 
  import os
  os.environ['SECRET_KEY'] = 'your_secret_key'
  os.environ['DATABASE_URL'] = 'postgres://yourusername:yourpassword@yourhost:yourport/yourdatabase'
  ```
- This `settings.py` file is set up to use the `env.py` file. You can verify following code in the `settings.py` file:
  ```sh
  import os
  import environ

  # Load environment variables from env.py
  if os.path.exists('env.py'):
      import env

  SECRET_KEY = os.environ.get("SECRET_KEY")
  DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}
    
  ```
The .gitignore file will already be set up to ignore the env.py file to prevent it from being uploaded to the repository.

### Additional Notes
- Ensure you have Python and pip installed on your system.
- Adjust the repository URL in the clone command to match your actual repository URL.

- For detailed information and troubleshooting, refer to the [Django documentation](https://docs.djangoproject.com/). You can also seek help from the [Django community](https://forum.djangoproject.com/).

- If you encounter any issues, refer to the Django documentation or seek help from the community.

These instructions should help you set up the project in your IDE correctly.

## Deployment to Heroku using the Heroku CLI 

  - Install the Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli).
  - Log in to your Heroku account using the command: `heroku login`
  - Create a new Heroku app with the command: `heroku create <your-app-name>`
  - Add the Heroku remote to your repository with the command: `heroku git:remote -a <your-app-name>`
  - Ensure your `requirements.txt` and `Procfile` are in the root directory of your project. The `Procfile` should contain: `web: gunicorn na_share.wsgi`
  - Add a `runtime.txt` file to specify the Python version, e.g., `Python 3.12.4`
  - Set up the database configuration in `settings.py` using `dj_database_url` and add the `DATABASE_URL` and `SECRET_KEY` config var in Heroku.
  - Having already installed this when setting up NA-Share on you IDE you can verify the following in your `settings.py`:
    ```python
    import dj_database_url
    if os.path.isfile('env.py'):
      import env
    ```
  - Collect static files with the command: 
    ```sh
    python3 manage.py collectstatic
    ```
  - Commit your changes and push to Heroku with the commands:
    ```sh
    git add .
    git commit -m "Prepare for Heroku deployment"
    git push heroku main
    ```
  - Run migrations on Heroku with the command: `heroku run python3 manage.py migrate`
  - Open your app in the browser with the command: `heroku open`

Congratulations you have deployed to Heroku using the commandline interface or terminal window.

## Deployment to Heroku using the Heroku Web UI
- First prep the installation in your IDE by collecting Stactic. making migrations and migrating.
- Once you have signed in to your Heroku account you will be presented with your [Dashboard](https://dashboard.heroku.com/apps) press the `New` tab/button then `create a new app` from the drop down.
 ![Dashboard](/project_readmes/images/Heroku%20deployment%20001.png)
- Add an app-name, choose Region, I've used Europe as I'm deploying from England. Then press create app.
 ![Dashboard](/project_readmes/images/Heroku%20deployment%20002.png)
- goto `settings` tab. then `Config Vars` and `Reveal Vars`.
 
- Now add your key and value pairs for `DATA_BASE`, `SECRET_KEY` and for `DISABLE_COLLECTSTATIC` set value to `1`.
 ![Dashboard](/project_readmes/images/Heroku%20deployment%20003.png)
- Now goto the `deploy` tab click on github in the `Deployment Method` section, when there, follow instructions to find your NA-Share cloned repository app and connect it to the Heroku app.
 ![Dashboard](/project_readmes/images/Heroku%20deployment%20004.png)

- At the bottom of the the Deploy page press on the `Deploy Branch` button in the `Manual Deply` section.
 ![Dashboard](/project_readmes/images/Heroku%20deployment%20005.png)
 
## NA-Share's current deployment links:
 - Heroku deployment... Link to NA-Share [NA-Share](https://na-share-b53b0f36b98a.herokuapp.com/)
 - GitHub Repository... link to repo [NA-Share](https://github.com/Damitwhy/NA-Share)  


## Technologies Used  

- **Frontend**: HTML, CSS, BootStrap, JavaScript, Django
- **Backend**: Django, Python
- **Database**: PostgreSQL, SQLite(Testing)
- **Authentication**: Django-Allauth 
- **Hosting**: Heroku, GitHub  
- **Development IDE**: VS Code, GitPod, GitHub  
- **Research Tools**: GitHub-Copilot, Chat-GPT, 
- **Production Tools**: Balsamiq, Chrome-Dev-Tools, Chrome-Extensions  

## Credits  
- **Images**
  - https://ytcbk-twnex.pyxl.ai/  
    Tool for creating AI generated websites, I choose to research design templates and found this site provides a free tier level set up and all images with design provided were for free use... Love the design but only used some of the design imagery.
  - Other images sourced via Chat-GPT searches.
  - To use the NA logo, individuals or groups typically need to obtain permission from NA World Services. This ensures that the logo is used in a manner that respects the organization’s guidelines and maintains the integrity of the brand. Verbally I have agreed its use is restricted to this capstone project and will not be put into production, I can use here. Having sent for written permission to use on future real world deployments of this Application, Awaiting response.
- **Research**
  - Chat-GPT
  - GitHub Copilot
  - Pyxl.ai Website GPT
  - Code Institute 
  - Google Workspaces
  - Stack over flow  

- **Colleagues**  
 - I'd just like to thank my peers and tutors :kissing_heart: at Code Institute Slack channel, Without whom I'd still be scratching my head wondering how all this works. Thank you for your time and patience, for telling me im wrong and helping me get back up to try again :blush: ...Oh and my assessors! :wink:

## Contributing
I welcome contributions! To the NA-Share project.

## License
This project is licensed under the MIT License. See the LICENSE file for more information. [MIT](/MIT_License.txt)

## Contact
For any questions or suggestions, please open an issue or contact Ken at damitwhy01@gmail.com

---

*Note: This project is inspired by the principles of Narcotics Anonymous and aims to provide a safe and supportive online community for its members.*
