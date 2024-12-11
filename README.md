# ScatterShot Games

<p align="center">
<img src=".\ReadMe_Images\ssg_final_product.png" alt="ssg final product image">
</P>
<br>

<p align="center">
<img src=".\ReadMe_Images\ssg_final_product_2.png" alt="ssg final product image">
</P>
<br>

## Overview

### Purpose

<p align="center">
<img src=".\ReadMe_Images\ssg_logo.jpg" alt="ssg logo">
</P>
<br>

ScatterShot Games, is an Indie Board Games Creator. With already 4+ custom board games created in house and available to purchase.
The purpose of this project is to create a full stack web application to allow ScatterShot to gain some online presence
and build the brand as well as the business in general.

The web application created as part of this project, will showcase Games, News/Blog articles and general information about ScatterShot and their business.

### Target Audience

With regards to a target audience, ScatterShot already has a following within the board game enthusiast space.
There is no official target audience for this project other than to promote this growing Indie business and the great products they create.

## User Stories

### Must-Have User Stories

-   **User Story 1:** HomePage, As a Site Owner, I want a Homepage, where I can highlight recent business activity and games,
    This will allow me to provide potential featured topics and games of my choosing.
    <br><br>
    **Acceptance Criteria:**

    1. Create a Main Homepage
    2. Display Business Activity and Games
    3. Create "Is Featured" functionality to filter model content on the homepage

---

-   **User Story 2:** Blog Page, As a Site Owner, I want a News or Blog page. The page should allow me as the owner to add posts and for general users to comment on those posts.
    Also, once registered and signed in, users should be able to comment, edit and delete their own comments.
    All comments must be approved before being made live on the respective post.
    So that I can keep my users and fans up to date with ScatterShot Games updates
    <br><br>
    **Acceptance Criteria:**

    1. Create a Blog Page
    2. Site Owner/Admin Post creation
    3. User Register/Login functionality
    4. User can comment, edit and delete their comments (after registering and/or login)
    5. Comments must be approved before made live

---

-   **User Story 3:** Blog Information Page, As a User, I want to view a blog post content on its own page.
    So that I can get a full grasp of the article and enjoy the read.
    <br><br>
    **Acceptance Criteria:**

    1. Create blog details pages
    2. Pages should be dynamic due to how data is pulled from the models

---

-   **User Story 4:** Blog Details Page, As a Site Owner, I want a more dedicated page for each blog post.
    So that I can showcase the full details of that particular blog post
    <br><br>
    **Acceptance Criteria:**

    1. Create Blog Details page
    2. Pages should be dynamically created as posts will be pulled from the database models

---

-   **User Story 5:** Games Page, As a Site Owner, I want a page to display all my games
    So that I can have a catalogue of all my games
    <br><br>
    **Acceptance Criteria:**

    1. Create a Games page
    2. Pull all game data from the model
    3. Display all Games, possibly paginate

---

-   **User Story 6:** Game Information Page, As a User, I want to see a more specific page which is tailored to one game at a time
    So that I can obtain more specific information about a certain game.
    <br><br>
    **Acceptance Criteria:**

    1. Create a Games Details page
    2. Pages should be dynamically created as games will be pulled from the database models

---

-   **User Story 7:** Game Details Page, As a Site Owner, I want a more dedicated page for each Game displayed.
    So that I can showcase the full details of that particular game.
    <br><br>
    **Acceptance Criteria:**

    1. Create a Games Details page
    2. Pages should be dynamically created as games will be pulled from the database models

---

-   **User Story 8:** Registration Page, As a Site Owner, I want to be able to allow users to register for the Scattershot Games site
    So that my users and fanbase access the site fully and participate in commenting on blog posts,
    this will allow my fanbase to grow in general.
    <br><br>
    **Acceptance Criteria:**

    1. Create Registration Page
    2. Registration Functionality
    3. Notifications regarding success or failure of registration
    4. Validation on the registration form, (Checking for existing Username, email, and matching password)

---

-   **User Story 9:** User Registration, As a User, I want to be able to register for Scattershot games
    So that I can access the site fully and participate in commenting on blog posts
    <br><br>
    **Acceptance Criteria:**

    1. Create Registration Page
    2. Registration Functionality
    3. Notifications regarding success or failure of registration
    4. Validation on the registration form, (Checking for existing Username, email, matching password)

---

-   **User Story 10:** Login Page, As a Site Owner, I want to be able to log in from the front end, rather than just the admin panel
    So that I can easily log in, add comments and view the website as if a general user.
    <br><br>
    **Acceptance Criteria:**

    1. Create Login Page
    2. Login functionality
    3. Notifications to indicate login was successful or not

---

-   **User Story 11:** Logout Functionality, As a User, I want to be able to log off of my Scattershot account
    So that I can ensure my account is secure and accessed by myself
    <br><br>
    **Acceptance Criteria:**

    1. Logout Functionality
    2. Notifications to show if logout was successful or not

---

-   **User Story 12:** Responsiveness, As a User, I want the site to work well on my tablet and phone
    So that I can view the site on different screen sizes
    <br><br>
    **Acceptance Criteria:**

    1. Ensure Mobile friendly
    2. Ensure Tablet friendly
    3. Use Media queries where needed to keep responsiveness consistent

---

-   **User Story 13:** Wireframing, As a Developer, The creation of wireframing and mock designs is required
    So that a baseline idea and design can be worked towards
    <br><br>
    **Acceptance Criteria:**

    1. Create Wireframes from Mobile, Tablet and Desktop

---

-   **User Story 14:** Documentation, As a Site Owner, I want a detailed document of the inner workings of the website
    So that I can learn how it was made and aid with the maintenance of the ongoing site.
    <br><br>
    **Acceptance Criteria:**

    1. Provide a detailed ReadME.md file
    2. Provide instruction on topics where site maintenance may require site owner/admin to access

---

### Should-Have User Stories

-   **User Story 15:** About Page, As a Site Owner, I want an about page.
    So that I can provide more information to site users about who ScatterShot Games are.
    <br><br>
    **Acceptance Criteria:**

    1. Create About page
    2. Possible Team ScatterShot Model?

---

-   **User Story 16:** Contact Page, As a Site Owner, I want a contact page
    So that users can give feedback and get in touch with me if required.
    At a minimum basic contact information, However perhaps an online form to allow easier contact
    <br><br>
    **Acceptance Criteria:**

    1. Create Contact page
    2. Display relevant contact information
    3. Web form to allow users to submit messages and their details in order to contact the site owner

---

### Could-Have User Stories

-   **User Story 17:** Project Management, As a Developer, I would like to keep the project files organises by breaking the project into various smaller apps within Django.
    So that I can manage the project and keep a cleaner file structure during the development process
    <br><br>
    **Acceptance Criteria:**

    1. Create Multiple Apps within the project
    2. Pages App - Manage majority of general webpages and navigation across the site (home, about, contact etc)
    3. Games App - Manage all functionality for displaying games and related pages
    4. Blog App - Manage all functionality for displaying the blog and related pages
    5. Accounts App - Manage all login, register and user functionality

---

-   **User Story 18:** Page Construction, As a Developer, It would make sense to divide the website pages into logical chunks
    So that the pages can be worked on easier
    <br><br>
    **Acceptance Criteria:**

    1. Create Base.html
    2. Possibly split the nav bar into a separate file for easier management
    3. Possibly split the footer into a separate file for easier management

---

-   **User Story 19:** Cloudinary Image Storage, As a Developer, I want to consider using cloud storage for certain aspects of the project
    So that the project and site when live can serve images more dynamically whilst avoiding any potential pitfalls with hosting platforms such as Heroku.
    <br><br>
    **Acceptance Criteria:**

    1. Consider adding in Cloudinary functionality to serve images for the various content within the project
    2. If summernote is used as part of admin customisation, then enabling cloudinary functionality here also.

---

-   **User Story 20:** Admin Panel Customisation, As a Developer, I would like to provide a custom admin panel, concerning functionality and theme.
    So that Admins and site owners are provided with a better user experience when maintaining the site
    <br><br>
    **Acceptance Criteria:**

    1. Utilise list display, link-editable, list-display-links, and other admin panel features
    2. Add a thumbnail image to add to the staff user experience when using the admin panel
    3. Edit Admin panel theme to match the feel of the rest of the site
    4. Possibly add packages like summernote to allow enhanced staff experience and editing abilities

---

-   **User Story 21:** User Feedback for Site Owner, As a Site Owner, I would like to receive an email or other method of knowing when a user submits a contact form
    So that I can easily keep track of messages from users
    <br><br>
    **Acceptance Criteria:**

    1. Email Feedback
    2. Submitted feedback details are stored in a model in the database

---

-   **User Story 22:** User Dashboard, As a User, I would like a profile page, that showcases my activity on the ScatterShot site
    So that I can keep track of my activity, comments and messages
    <br><br>
    **Acceptance Criteria:**

    1. Create a Dashboard page
    2. Display User relevant content, based on logged-in users.

---

-   **User Story 23:** Colour Theme, As a Developer, I would like to set and use some variables within the CSS
    To allow easier colour theme changes on the site, depending on site owner preferences
    <br><br>
    **Acceptance Criteria:**

    1. Define colour variable with root { --theme1 : #000000; }
    2. Use var(--theme) to apply related colour

---

## Design Decisions

### Project Board

To keep the project on track, manage scope and work to Agile methodology a kanban style project board was created.
This project board is continuously updated and utilised throughout the development cycles of the project.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_projectboard_1.png" alt="ssg project board image">
</P>
<br>

<p align="center">
<img src=".\ReadMe_Images\ssg_projectboard_2.png" alt="ssg project board image">
</P>
<br>

### Entity Relationship Diagram

The diagram linked below shows the relationship between all the tables / Models used throughout the project.
The user, once authenticated is referenced at various points in other models.
Each user can comment on a game and blog post, they will ahve control over editing and deleting their own commeents also.
However, no comment will be made Live until an Admin user has approved the comment.
This functionality highlights the <strong>CRUD</strong> abilities within the project.

A brief description of the relationships are as follows:

User from User Model is always a 1 to 1 relationship.
Every Game can have many comments, but a comment can only belong to a single game.
Every Blog Post can have many comments, but a comment can only belong to a single post.
A User can send many messages, but a message can only belong to one user.
The team model is not linked to any other model via a relationship, as this functionality was not required for this project.

<p align="center">
<img src=".\ReadMe_Images\Entity_relationship_diagram.png" alt="ssg project board image">
</P>
<br>

### Wireframes

During the design process of the ScatterShot Web Application, wireframing took place for every page and across 3 view points.

-   Desktop
-   Tablet
-   Mobile

The below design choices were made to ensure the application is responisve across all 3 screen types and a well rounded application.

#### Desktop Wireframes

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_home.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_games.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_games_details.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_about.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_blog.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_post_details.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_contact.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_login.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_signup.png" alt="ssg wireframe desktop image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_desktop_dashboard.png" alt="ssg wireframe desktop image">
</P>
<br>

#### Tablet Wireframes

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_home.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_games.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_games_details.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_about.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_blog.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_post_details.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_contact.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_login.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_signup.png" alt="ssg wireframe tablet image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_tablet_dashboard.png" alt="ssg wireframe tablet image">
</P>
<br>

#### Phone Wireframes

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_home.png" alt="ssg wireframe phone image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_games.png" alt="ssg wireframe phone image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_games_details.png" alt="ssg wireframe phone image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_about.png" alt="ssg wireframe phone image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_blog.png" alt="ssg wireframe phone image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_post_details.png" alt="ssg wireframe phone image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_contact.png" alt="ssg wireframe phone image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_login.png" alt="ssg wireframe phone image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_signup.png" alt="ssg wireframe phone image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\wireframe_phone_dashboard.png" alt="ssg wireframe phone image">
</P>
<br>

### Accessibility Considerations

#### Colour Scheme

The chosen colour scheme, compliments the themes used within Scattershots products as well as pleasing to the eye.

<br>
<p align="center">
<img src=".\ReadMe_Images\colour_scheme_1.png" alt="ssg colour scheme image">
</P>
<br>

#### Colour Contrast

Colour contrast was considered during the colour scheme selection. 
Details show how the lighter end of contrast as well as the darker end below.

<br>
<p align="center">
<img src=".\ReadMe_Images\colour_contrast_1.png" alt="ssg colour contrast image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\colour_contrast_2.png" alt="ssg colour contrast image">
</P>
<br>

#### Fonts

Robotto is one of the chosen Fonts used for this project.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_font_1.png" alt="ssg font image">
</P>
<br>

#### LightHouse Scores

Lighthose also knwon as PageSpeed Insights, scores are shown below. Performance is lacking across the site, however this is due to unoptimised images.
These will be addressed in future iterations of project.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_lighthouse_1.png" alt="ssg lighthouse score image">
</P>
<br>


## Features Implementation

### Core Features (Must-Haves)

-   **Feature 1:** Homepage, with featured Games and Blog posts shown

The <strong>Homepage</strong> is the entry point to the website and highlight all the latest information and products on offer from Scattershot Games.
Key points to highlight are the filtering and displaying of selected data from various models.
For example, the site admin has the ability to flag any game or blog post as <strong>"Featured"</strong>, once tagged the data will be presented on the homepage.
This allows a conveinent way for the admin to mange their site content.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_home.png" alt="ssg feature image">
</P>
<br>

---

-   **Feature 2:** Dedicated Games Page

The <strong>Games Page</strong>, is a dedicated page that shows all products available from Scattershot Games.
By default the page will show 4 games at once and sorted alphabetically if there are more than 4 games to be displayed then pagination will take place.
Each game has its own details page, which is a dedicated page to that particualr game, on this page all authenicated users will be able to comment on the game.
Only authenticated users can comment, once authenticated it allows the user to comment and manage their own comment, such as editing and deleting them.
Worth noting all comments must be <strong>approved</strong> via a site admin in the admin panel before they become Live for all to see.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_gamepage.png" alt="ssg feature image">
</P>
<br>

<p align="center">
<img src=".\ReadMe_Images\ssg_feature_gamepage_2.png" alt="ssg feature image">
</P>
<br>

---

-   **Feature 3:** Dedicated Blog Page

The <strong>Blog Page</strong>, is another dedicated page which is utilised to highlight all blog articles Scattershot want to share.
This page will show all blog posts that are tagged as <strong>published</strong>, this addition to this feature allows the site admin to manage their content with ease.
Each blog post has its own details page, which is a dedicated page to that particualr blog post, on this page all authenicated users will be able to comment on the articles.
Only authenticated users can comment, once authenticated it allows the user to comment and manage their own comment, such as editing and deleting them.
Worth noting all comments must be <strong>approved</strong> via a site admin in the admin panel before they become Live for all to see.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_blogpage.png" alt="ssg feature image">
</P>
<br>

<p align="center">
<img src=".\ReadMe_Images\ssg_feature_blogpage_2.png" alt="ssg feature image">
</P>
<br>


---

-   **Feature 4:** Registration page

The <strong>Registration Page</strong>, allows site visitors to sign up to the Scattershot site. Which in turn grants them additional abilities.
Such as commenting on all games and blog posts being displayed on the site.
Visitors will have the ability to signup in a conventional sense via the form or they can choose to signup via their <strong>Facebook</strong> or <strong>Google</strong> account also.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_signup.png" alt="ssg feature image">
</P>
<br>

---

-   **Feature 5:** Login and Logout Functionality

<strong>Login, Logout Functionality</strong> is a must have feature for any website nowadays. Scattershot is no exception.
Via the login screen a registered user can login with their username and password or via their <strong>Facebook</strong> and or <strong>Google</strong> account.
Thus giving the user a variety of login method, depending on their preference.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_login.png" alt="ssg feature image">
</P>
<br>

---

### Advanced Features (Should-Haves)

-   **Feature 1:** Contact Form

Having a <strong>Contact Form</strong> on the Scattershot site opens up various opportunities,
such as allowing the user to submit feedback as well as potential game ideas or even collaboration oportunities.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_contact.png" alt="ssg feature image">
</P>
<br>

---

-   **Feature 2:** About Page

By providing an <strong>About Page</strong> on the Scattershot site this allows the visitor and or User to find out more about the inner workings of Scattershot.
Who is involved ? who makes the games? Who manages the site ?

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_about.png" alt="ssg feature image">
</P>
<br>

---

### Optional Features (Could-Haves)

-   **Feature 1:** Cloudinary Storage for all images

Utilising <strong>Cloud Storage</strong> is a great method of handling any and all image storage requirements.
Cloudinary is the storage source of choice for this project.
Cloudinary handles all storage of images for all games, blog posts and summernote editor images.
It simply stores a link in the <strong>Postgres Database</strong> to the resource in cloudinary

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_cloudinary.png" alt="ssg feature image">
</P>
<br>

---

-   **Feature 2:** Admin Panel Customisation

By <strong>Customising</strong> the admin panel, this allows a much greater user experience for all of Team Scattershot, who will be managing the site.
When talking about customisation,

-   Additional <strong>Search Abilities</strong>
-   <strong>Filtering</strong> based on relevant data e.g date or author.
-   <strong>Thumbnails</strong> of any images to enhance user experience.
-   Extra <strong>Clickable</strong> Fields, for easier access.
-   Additional Headings Displayed to show more information.
-   <strong> Editable Fields </strong>, allowing staff to toggle values at any time.
-   Summernote, which enables <strong>Rich Text Editor Functionality</strong> in various models to allow enhanced editing abilties.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_admin.png" alt="ssg feature image">
</P>
<br>

<p align="center">
<img src=".\ReadMe_Images\ssg_feature_admin_2.png" alt="ssg feature image">
</P>
<br>

---

-   **Feature 3:** User Feedback and Notification

<strong>User feedback and Notification</strong>, this feature ties into the contact form functionality.
Various messages are utilsed to inform the user of success or failure depending on the operation being conducted.
E.g, if a User registers successfully or not.
Other features of this topic include the <strong>Storage</strong> of the message submitted by the Visitor / User.
By storing the message this allow staff to keep a record of the message and tag messages as read and or replied too.
Additionally <strong>Emails</strong> are sent to all site admins and the email address of the Visitor / User who left the message.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_feedback_1.png" alt="ssg feature image">
</P>
<br>

<p align="center">
<img src=".\ReadMe_Images\ssg_feature_feedback_2.png" alt="ssg feature image">
</P>
<br>

---

-   **Feature 4:** User Dashboard

Having a <strong>User Dashboard</strong>, not only gives polish to the web application but it provides a lcoation on the site that is unique to each User.
The dashboard contains,

-   Access to <strong>Admin Panel</strong>, for all signed in Admin/Staff accounts
-   Ability to edit <strong>Acount Details</strong>, Username, Email and Password
-   All <strong>Messages</strong> sent by the user vai the contact form
-   Any <strong>Comments</strong> left on a game by the User, with a link to the relevant page.
-   Any <strong>Comments</strong> left on a blog post by the User, with a link to the relevant page.

By providing this information to the User it gives them a snapshot fo their activity on the Scattershot site.
Also worth mentioning when a site admin tags a message as read or replied, this is shown to the User on their Dashboard, thus providing additonal feedback and a greater <strong>User Experience</strong>.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_feature_dashboard.png" alt="ssg feature image">
</P>
<br>

---

## Testing and Validation

### Testing Results

### Home Page

| Test                                  | Result |
| ------------------------------------- | ------ |
| Home:                                 | Pass   |
| Games: It redirects to games page      | Pass   |
| About: It redirects to about page       | Pass   |
| Blog: It redirects to blog page        | Pass   |
| Contact:It redirects to contact page   | Pass   |
| Sign In: It redirects to sign In page  | Pass   |
| Register:It redirects to registration page | Pass   |
| Displays only games that are featured                | Pass |
| Displays only blog posts that are featured                | Pass |
| Displays correct details about Team Scattershot             | Pass |

### Games Page

| Test                                             | Pass |
| ------------------------------------------------ | ---- |
| Displays all games                  | Pass |
| Paginates after more than 4 games are displayed          | Pass |
| All Pages in Naviagtion bar link correctly            | Pass |


### Games Details Pages

| Test                                             | Pass |
| ------------------------------------------------ | ---- |
| Displays all relevant details about the game in question                | Pass |
| All Pages in Naviagtion bar link correctly          | Pass |
| When logged out user can not comment            | Pass |
| When logged in user can comment, edit and delete their own comments      | Pass |
| Comments are not Live until approved by admin in admin panel | Pass |

### About Page

| Test                                             | Pass |
| ------------------------------------------------ | ---- |
| Displays correct information about scattershot games     | Pass |
| Displays correct details about Team Scattershot   | Pass |
| All Pages in Naviagtion bar link correctly        | Pass |


### Blog Page

| Test                                             | Pass |
| ------------------------------------------------ | ---- |
| Displays all blog posts                          | Pass |
| All Pages in Naviagtion bar link correctly        | Pass |

### Post Details Pages

| Test                                             | Pass |
| ------------------------------------------------ | ---- |
| Displays all relevant details about the post     | Pass |
| All Pages in Naviagtion bar link correctly       | Pass |
| When logged out user can not comment             | Pass |
| When logged in user can comment, edit and delete their own comments      | Pass |
| Comments are not Live until approved by admin in admin panel | Pass |

### Contact Page

| Test                                        | Result |
| ------------------------------------------- | ------ |
| Contact form validates fields correctly                 | Pass   |
| Contact form sends data and stores in model correctly     | Pass   |
| Contact form gets all admin emails and sends notification email to all admins and the email left by the user        | Pass   |
| All Pages in Naviagtion bar link correctly       | Pass |

### Login Page

| Test                                        | Result |
| ------------------------------------------- | ------ |
| Secure Login functionality                  | Pass   |
| Google and Facebook Login functionality     | Pass   |
| Redirect after successful login             | Pass   |
| All Pages in Naviagtion bar link correctly       | Pass |

### Registration Page

| Test                                               | Result |
| -------------------------------------------------- | ------ |
| Secure Registration functionality                  | Pass   |
| Google and Facebook Registration functionality     | Pass   |
| Redirect after successful Registration             | Pass   |
| All Pages in Naviagtion bar link correctly       | Pass |

### Dashboard Page

| Test                                               | Result |
| -------------------------------------------------- | ------ |
| Once logged in User is taken to dashboard                | Pass   |
| Dashboard only shown to logged in User     | Pass   |
| User can change their, username, email and password for their account via dashboard            | Pass |
| Admin can access the Admin Panel via a buttoin through the dashboard when logged in as a Admin | Pass |
| Dashboard displays summary of messages sent via the contact form by the logged in User       | Pass |
| Dashboard displays summary of blog post comments made by the logged in User      | Pass |
| Dashboard displays summary of game page comments made by the logged in User      | Pass |
| All Pages in Naviagtion bar link correctly       | Pass |


## Bugs and Known Issues

### Bugs

-   <strong>Bug 1</strong>: Issues when adding to a model on the deployed site, where cloudinary is used alognside the summernote editor.
-   <strong>Fix</strong>: Cloudinary variables were not set correctly on heroku, DEBUG mode in Django helped figure out which variable was incorrect.

-   <strong>Bug 2</strong>: Issues with Facebook and Google Logins on the deployed sites.
-   <strong>Fix</strong>: Additional callback URLs needed to be added to the appropriate app in Facebook Developers and Google Developers.

-   <strong>Bug 3</strong>: Cloudinary returns HTTP responce rather than HTTPS which causes a console error.
-   <strong>Fix</strong>: Cloudinary will need to update there type of responce given when an image is fetched.

-   <strong>Bug 4</strong>: Password Reset Functionality on the Login page, Email reset link would not load properly
-   <strong>Fix</strong>: Reconfigured URLS for accounts app and project, project URLS now controls the final stages of the reset process.


### Validation

#### HTML Validation
<br>
<p align="center">
<img src=".\ReadMe_Images\html_validator_1.png" alt="ssg html validator image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\html_validator_2.png" alt="ssg css validator image">
</P>
<br>

#### CSS Validation
<br>
<p align="center">
<img src=".\ReadMe_Images\css_validator_1.png" alt="ssg JS linter image">
</P>
<br>

#### Javascript Validation

App.js and comments.js are the only Javascript files I have added code too.
Firstly App.js is a script to initiate all the various third-party JS libraries used and works with JQuery. App.js has be preliminarily Linted but still contains warnings.
Comments.js is the logic created via the the CI blog walkthrough project, therefore this code has also be prelimnarily Linted but still contains warnings.

<br>
<p align="center">
<img src=".\ReadMe_Images\jslint_validator_1.png" alt="ssg JS linter image">
</P>
<br>


#### Python Validation

All Python files have be created alongside the Pylint extension as well as being checked in the CI Python Linter shown Below.
All third-party code, including but not limted to Cloudinary, Summernote, Django and its migration files created for this project have not been Linted, due to they are created via a third party package and or code.
Flake8 was also used to check for errors throughout the project.

<br>
<p align="center">
<img src=".\ReadMe_Images\pylint_validator_1.png" alt="ssg python linter image">
</P>
<br>




## AI Tools Usage

### GitHub Copilot

Github Copilot, has been utilised throughout the project with great success. The AI Pair Programming tool was used to ensure accurate docstrings and comments were applied throughout the project.
Copilot was also extremely helpful when encountering errors, discussing ideas for the project and their related logic.
Generally speaking Copilot was primarily used for fault finding, providing insight as well as explanations and documenting the code.

<br>
<p align="center">
<img src=".\ReadMe_Images\ssg_copilot_1.png" alt="ssg copilot image">
</P>
<br>

## Deployment

### Deployment Process

For the ScatterShot Web Application, Heroku is the deployment option of choice.
Heroku has a few requirements that need to be setup to allow heroku to host properly.

-   Procfile
-   Requirements.txt
-   Runtime.txt

These 3 files tell Heroku what to do, how to do and with what basic settings.
In order to deploy on Heroku firstly GitHub had to be linked to Heroku to allow the Repo be pulled from.
Once linked to GitHub and a Repo selected. Heroku can attempt deployments based on the designated Repo.
Heroku also requires all environment variables to be stored in the settings of the app and to be assigned on heroku itself as a config Var, this allows Heroku to access all areas of the django project.
Such as database url, cloudinary url, email settings etc.

<br>
<p align="center">
<img src=".\ReadMe_Images\heroku_deploy_1.png" alt="ssg heroku deployment image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\heroku_deploy_2.png" alt="ssg heroku deployment image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\heroku_deploy_3.png" alt="ssg heroku deployment image">
</P>
<br>

<br>
<p align="center">
<img src=".\ReadMe_Images\heroku_deploy_4.png" alt="ssg heroku deployment image">
</P>
<br>

### Deploying to a Custom Domain

As a requirement for the client of this project hosting the finalised web app on a custom domain was needed.
The client provided access to Wix, their domain provider.
First, the domain must be setup in the settings section on heroku.

<br>
<p align="center">
<img src=".\ReadMe_Images\domain_deploy_1.png" alt="ssg heroku deployment image">
</P>
<br>

Next ensuring the settings.py file is correctly setup, providing a site ID, and allowed hosts.

<br>
<p align="center">
<img src=".\ReadMe_Images\domain_deploy_2.png" alt="ssg heroku deployment image">
</P>
<br>

Followed by ensuring the django admin has the domain setup correctly.

<br>
<p align="center">
<img src=".\ReadMe_Images\domain_deploy_3.png" alt="ssg heroku deployment image">
</P>
<br>

Fianlly accessing the domain providers records and linking them up.


## Code Attribution and Credit

### Jquery, Gallery, SlickSlide etc

To create a more polished and interactive experience I utilised various javascript scripts to create the image galleries, magnification effect, and scroll-up functionality.

**Sources** <br> <br>
[Slick.js](http://kenwheeler.github.io) <br> Slick provides a smooth side scroll function for the website<br>
[Light Gallery](http://sachinchoolur.github.io/lightGallery/) <br> Light Gallery, alongside Magnific Pop Up provides a great looking image gallery utilised across the site<br>
[Jquery Magnific Popup](http://dimsemenov.com/plugins/magnific-popup/) <br> Magnific provides an interactive image zoom and pop up functionality which works alongside the gallery.<br>
[Jquery](https://www.jqueryscript.net/) <br> Core Jquery code to allow jquery plugins to work properly<br>
[Scroll Up](https://markgoodyear.com/2013/01/scrollup-jquery-plugin/) <br> Scroll Up is another Jquery plugin that allows the user to jump back to the top of the page<br>
[Bootstrap](https://getbootstrap.com) <br> Bootstrap used for responsiveness, styling and required for the above plugins and functionality<br>


All third party code has not been Linted and will most likely not meet any relevant standard, whether that be PEP8 or ES6

## Reflection on Development Process

### Successes

This project had many successes, firstly th correct filtering of models in various sections of the web application works very well, particularly the homepage as this gives the owner the ability to highlight their content.
CoPilot was an invaluable tool used during the project, it allows extensive fault finding and explainations of how to go about creating the required logic and processes needed throughout the project.

### Challenges

There were various challenges throughout the project. One in particular was the fact the project is for an actual friend and client, so the MVP was a benchmark that had to be pushed past to en extent,
Another challenge was intergrating the external javascript gallery and libraries as well as intergrating the blog setup which was taken from the blog walkthrough, once implemented various tweaks changes and adaptations were made.

### Final Thoughts

The end result of ScatterShotGames.com has turned out great, yes the project is not perfect. However as an extended MVP and first iteration of the web application this is more that sufficient for the clients needs.
With the creation, hosting and configutation of the ScatterShotGames App, it will furfill its purpose and allow the ScatterShotGames to grow its online presence. 

## Future Improvements

Potential future improvements could be refining the styling as a colour scheme wasnt really decided upon from the client so colours were taken as inspiration from one of their game products.
Another improvement would be more extensive responsiveness fixes as on different mobile screens the games details can be cut off and not as refined, this would require alot more gradular media queries to be setup for more accurate screen sizes.